from pathlib import Path
root = Path('content')
paths = []
for p in root.rglob('*.md'):
    if p.name == '_index.md':
        continue
    rel = p.relative_to(root).as_posix()
    paths.append(rel)
print('Markdown files:', len(paths))
for p in sorted(paths)[:120]:
    print(p)
