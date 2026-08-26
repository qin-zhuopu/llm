import json, os, re, time, sys
import requests

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, '_raw')
os.makedirs(RAW, exist_ok=True)

with open(os.path.join(BASE, 'posts.json'), encoding='utf-8') as f:
    posts = json.load(f)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

s = requests.Session()
s.headers.update(HEADERS)

failed = []
for p in posts:
    slug = p['path'].strip('/').replace('/', '__')
    if not slug:
        slug = 'index'
    out = os.path.join(RAW, slug + '.html')
    if os.path.exists(out) and os.path.getsize(out) > 500:
        print('skip (cached)', p['path'])
        continue
    for attempt in range(3):
        try:
            r = s.get(p['url'], timeout=40)
            if r.status_code == 200 and len(r.text) > 500:
                with open(out, 'w', encoding='utf-8') as f:
                    f.write(r.text)
                print('OK', p['path'], len(r.text))
                break
            else:
                print('BAD status', r.status_code, len(r.text), p['path'])
                time.sleep(2)
        except Exception as e:
            print('ERR', p['path'], repr(e))
            time.sleep(2)
    else:
        failed.append(p['path'])

print('\nDONE. failed:', failed)
