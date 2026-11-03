"""Refresh the report's four-level contents without indexing code comments."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
path = root / 'README.md'
text = path.read_text(encoding='utf-8')
start = text.index('## Contenido\n')
end = text.index('## Student Outcome\n', start)
body = text[end:]
entries = ['## Contenido', '']
seen = {}
fence = None
for line in body.splitlines():
    marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
    if marker:
        value = marker.group(1)
        if fence is None:
            fence = value
        elif value[0] == fence[0] and len(value) >= len(fence):
            fence = None
        continue
    if fence:
        continue
    match = re.match(r'^(#{1,4}) (.+)$', line)
    if not match:
        continue
    level, title = match.groups()
    slug = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
    count = seen.get(slug, 0)
    seen[slug] = count + 1
    if count:
        slug += f'-{count}'
    entries.append('  ' * (len(level) - 1) + f'- [{title}](#{slug})')
path.write_text(text[:start] + '\n'.join(entries) + '\n\n' + body, encoding='utf-8')
print(f'Updated {len(entries) - 2} contents entries; code comments excluded.')
