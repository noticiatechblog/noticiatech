import os, csv, glob
base = r'C:\Users\Aluisio\Desktop\prompts para artigos\Search Console'
for dirn in ['coverage','performance']:
    print('=====DIR', dirn, '=====')
    for path in sorted(glob.glob(os.path.join(base, dirn, '*.csv'))):
        with open(path, 'r', encoding='utf-8-sig', newline='') as f:
            rows = list(csv.reader(f))
        print('FILE', os.path.basename(path), 'rows', len(rows))
        for row in rows[:8]:
            print(row)
        print()
