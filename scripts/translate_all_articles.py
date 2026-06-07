import re
import shutil
import unicodedata
import yaml
from pathlib import Path
from deep_translator import GoogleTranslator
from deep_translator.exceptions import NotValidLength, TranslationNotFound

SOURCE_ROOT = Path('content')
TARGET_ROOT = Path('content/en')

CATEGORY_MAP = {
    'negocios': 'business',
    'automacao': 'automation',
    'ferramentas': 'tools',
    'inteligencia-artificial': 'artificial-intelligence',
}


def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = ''.join(ch for ch in unicodedata.normalize('NFKD', text) if not unicodedata.combining(ch))
    return text


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text or 'article'


FRONT_MATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*(?:\n|$)', re.DOTALL)
IMAGE_MARKDOWN_RE = re.compile(r'!\[[^\]]*\]\([^\)]+\)')


def split_front_matter(text: str):
    match = FRONT_MATTER_RE.search(text)
    if match:
        front_matter = match.group(1)
        body = text[match.end():].lstrip('\n')
        return front_matter, body
    return None, text


def split_into_chunks(text: str, max_chars: int = 4000):
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n+', text) if p.strip()]
    chunks = []
    current = ''

    for paragraph in paragraphs:
        candidate = paragraph if not current else current + '\n\n' + paragraph
        if len(candidate) > max_chars and current:
            chunks.append(current)
            current = paragraph
        else:
            current = candidate

    if current:
        chunks.append(current)

    final_chunks = []
    for chunk in chunks:
        if len(chunk) <= max_chars:
            final_chunks.append(chunk)
            continue

        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', chunk) if s.strip()]
        current_sentence = ''
        for sentence in sentences:
            candidate = sentence if not current_sentence else current_sentence + ' ' + sentence
            if len(candidate) > max_chars and current_sentence:
                final_chunks.append(current_sentence)
                current_sentence = sentence
            else:
                current_sentence = candidate
        if current_sentence:
            final_chunks.append(current_sentence)

    return final_chunks or [text]


def translate_text(text: str, source='pt', target='en') -> str:
    text = text.strip()
    if not text:
        return text

    chunks = split_into_chunks(text)
    translated = []

    for chunk in chunks:
        translator = GoogleTranslator(source=source, target=target)
        try:
            translated_chunk = translator.translate(chunk)
            translated.append(translated_chunk or chunk)
        except (TranslationNotFound, NotValidLength):
            # Retry with smaller chunks if the translator refuses the size.
            smaller = split_into_chunks(chunk, max_chars=2000)
            if len(smaller) > 1:
                translated.append(translate_text('\n\n'.join(smaller), source, target))
            else:
                translated.append(chunk)

    return '\n\n'.join(translated)


def preserve_markdown_images(text: str):
    replacements = {}

    def replace(match):
        token = f'__IMG_{len(replacements)}__'
        replacements[token] = match.group(0)
        return token

    preserved = IMAGE_MARKDOWN_RE.sub(replace, text)
    return preserved, replacements


def restore_markdown_images(text: str, replacements: dict) -> str:
    for token, original in replacements.items():
        text = text.replace(token, original)
    return text


def translate_faq(faq_items):
    if not isinstance(faq_items, list):
        return faq_items

    translated = []
    for item in faq_items:
        if isinstance(item, dict):
            translated_item = dict(item)
            if 'pergunta' in translated_item:
                translated_item['pergunta'] = translate_text(translated_item['pergunta'])
            if 'resposta_curta' in translated_item:
                translated_item['resposta_curta'] = translate_text(translated_item['resposta_curta'])
            if 'resposta_longa' in translated_item:
                translated_item['resposta_longa'] = translate_text(translated_item['resposta_longa'])
            translated.append(translated_item)
        else:
            translated.append(item)
    return translated


for source_path in sorted(SOURCE_ROOT.rglob('index.md')):
    parts = source_path.parts
    if len(parts) < 4 or parts[0] != 'content':
        continue
    if parts[1] == 'en' or parts[1] == 'pt':
        continue
    if parts[2] == 'categories':
        continue
    category = parts[1]
    if category.startswith('en') or category.startswith('pt'):
        continue
    if category not in CATEGORY_MAP:
        continue

    title_slug = source_path.parent.name

    raw = source_path.read_text(encoding='utf-8')
    fm, body = split_front_matter(raw)
    if fm is None:
        continue

    try:
        data = yaml.safe_load(fm)
    except yaml.YAMLError as exc:
        print(f'Skipping file with invalid front matter: {source_path} ({exc})')
        continue

    if not isinstance(data, dict):
        continue

    title = data.get('title', '')
    description = data.get('description', '')
    translated_title = translate_text(title) if title else ''
    translated_description = translate_text(description) if description else ''
    translated_slug = slugify(translated_title) if translated_title else title_slug

    target_category = CATEGORY_MAP[category]
    target_dir = TARGET_ROOT / target_category / translated_slug
    if (target_dir / 'index.md').exists():
        continue

    print(f'Translating: {source_path} -> {target_dir}')
    target_dir.mkdir(parents=True, exist_ok=True)

    for asset in source_path.parent.iterdir():
        if asset.is_file() and asset.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.avif', '.bmp'}:
            shutil.copy2(asset, target_dir / asset.name)

    # Preserve the same image references and front matter structure whenever possible.
    data['title'] = translated_title
    if description:
        data['description'] = translated_description
    if 'categories' in data:
        translated_categories = []
        for category in data['categories']:
            mapped = CATEGORY_MAP.get(normalize_text(category), category)
            translated_categories.append(mapped)
        data['categories'] = translated_categories

    if 'cover' in data and isinstance(data['cover'], dict):
        if 'alt' in data['cover'] and isinstance(data['cover']['alt'], str):
            data['cover']['alt'] = translate_text(data['cover']['alt'])
        if 'caption' in data['cover'] and isinstance(data['cover']['caption'], str):
            data['cover']['caption'] = translate_text(data['cover']['caption'])

    if 'faq' in data:
        data['faq'] = translate_faq(data['faq'])

    if 'author' in data and isinstance(data['author'], str):
        data['author'] = translate_text(data['author'])

    data['slug'] = slugify(translated_title) if translated_title else title_slug

    body_for_translation, image_replacements = preserve_markdown_images(body)
    translated_body = translate_text(body_for_translation)
    translated_body = restore_markdown_images(translated_body, image_replacements)

    yaml_text = yaml.safe_dump(data, allow_unicode=True, sort_keys=False)
    target_text = '---\n' + yaml_text + '---\n\n' + translated_body
    (target_dir / 'index.md').write_text(target_text, encoding='utf-8')

print('Translation script completed.')
