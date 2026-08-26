import json, os, re, html as htmllib
from bs4 import BeautifulSoup
import html2text

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, '_raw')
OUT = os.path.join(BASE, 'posts_md')
os.makedirs(OUT, exist_ok=True)

with open(os.path.join(BASE, 'posts.json'), encoding='utf-8') as f:
    posts = json.load(f)

h = html2text.HTML2Text()
h.body_width = 0
h.ignore_images = True
h.ignore_emphasis = False
h.ignore_links = False
h.ignore_tables = False
h.unicode_snob = True
h.mark_code = True
h.single_line_break = True

def clean_title(t):
    t = re.sub(r'\s*\|\s*Applied Compute$', '', t or '').strip()
    return t

DATE_RE = re.compile(r'^[A-Za-z]{3,9} \d{1,2}, \d{4}$')

def get_meta(soup):
    title = None
    date = None
    authors = None
    og = soup.find('meta', property='og:title')
    if og and og.get('content'):
        title = clean_title(og['content'])
    h1 = soup.find('h1')
    if h1 and not title:
        title = h1.get_text(' ', strip=True)
    date_span = None
    for sp in soup.find_all('span'):
        t = sp.get_text(' ', strip=True)
        if DATE_RE.match(t):
            date = t
            date_span = sp
            break
    if date_span is not None:
        nxt = date_span.find_next_sibling()
        if nxt is not None and nxt.name == 'span':
            t = nxt.get_text(' ', strip=True)
            if t and t != date and len(t) < 200:
                authors = t
    return title, date, authors

def article_body(soup):
    art = soup.find('article')
    if art:
        return art
    main = soup.find('main')
    if main:
        return main
    # Fallback: try to find the main content div
    body = soup.find('body')
    return body

def convert(html_path):
    with open(html_path, encoding='utf-8', errors='ignore') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    title, date, authors = get_meta(soup)
    body = article_body(soup)
    if body is None:
        return None, title, date, authors, 'no article'
    md = h.handle(str(body))
    md = re.sub(r'\n{3,}', '\n\n', md).strip()
    return md, title, date, authors, None

results = []
for p in posts:
    slug = p['path'].strip('/').replace('/', '__')
    if not slug:
        slug = 'index'
    html_path = os.path.join(RAW, slug + '.html')
    if not os.path.exists(html_path):
        results.append((p['path'], None, None, None, None, 'missing html'))
        continue
    md, title, date, authors, err = convert(html_path)
    if err:
        results.append((p['path'], None, None, None, None, err))
        continue
    fm = []
    fm.append('---')
    if title:
        fm.append(f"title: \"{title.replace(chr(34), chr(92)+chr(34))}\"")
    if date:
        fm.append(f"date: {date}")
    if authors:
        fm.append(f"authors: \"{authors}\"")
    fm.append(f"source: \"{p['url']}\"")
    fm.append('---')
    content = '\n'.join(fm) + '\n\n' + md
    out = os.path.join(OUT, slug + '.md')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(content)
    results.append((p['path'], title, date, authors, len(md), None))

print('=== RESULTS ===')
for r in results:
    print(r)
