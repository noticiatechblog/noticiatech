from pathlib import Path
root = Path('public')
paths = []
for p in sorted(root.rglob('index.html')):
    rel = p.relative_to(root).as_posix()
    if rel in {'index.html', '404.html'}:
        continue
    if rel.startswith('en/') and '/page/' in rel:
        continue
    if rel.startswith('pt-br/'):
        continue
    if rel.startswith('assets/') or rel.startswith('js/') or rel.startswith('images/') or rel.startswith('page/') or rel.startswith('categories/') or rel.startswith('tags/'):
        continue
    paths.append(rel)
print('public pages', len(paths))
for p in paths[:200]:
    print(p)
