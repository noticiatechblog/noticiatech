from pathlib import Path
from collections import Counter
root = Path('public')
paths = []
for p in root.rglob('index.html'):
    rel = p.relative_to(root).as_posix()
    if rel in {'index.html','404.html'}:
        continue
    if rel.startswith(('assets/','js/','images/','page/','categories/','tags/')):
        continue
    paths.append(rel)
print('total generated article pages', len(paths))
print('top-level sections')
for section, count in Counter(p.split('/')[0] for p in paths).items():
    print(section, count)
