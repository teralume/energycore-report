from __future__ import annotations

import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
README = README_PATH.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


for raw_marker in ("```mermaid", "flowchart LR", "flowchart TB", "flowchart TD", "erDiagram", "classDiagram"):
    require(raw_marker not in README, f"Raw Mermaid marker remains: {raw_marker}")

required_headings = (
    "# Capítulo III Requirements Specification",
    "# Capítulo V Product Implementation",
    "# Capítulo VI Product Verification and Validation",
    "# Capítulo VII DevOps Practices",
    "# Conclusiones",
    "# Bibliografía",
    "# Anexos",
)
for heading in required_headings:
    require(heading in README, f"Required report section is missing: {heading}")

required_assets = (
    "assets/team/fabricio-rivera.jpeg",
    "assets/architecture/architecture-overview.svg",
    "assets/architecture/c4-context.svg",
    "assets/architecture/c4-container.svg",
    "assets/architecture/c4-api-components.svg",
    "assets/architecture/c4-client-components.svg",
    "assets/architecture/class-diagram.svg",
    "assets/architecture/database-core.svg",
    "assets/architecture/database-support.svg",
    "assets/architecture/database-billing.svg",
    "assets/architecture/database-notifications.svg",
)
for asset in required_assets:
    require((ROOT / asset).is_file(), f"Required asset is missing: {asset}")

local_images: set[str] = set()
local_images.update(re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', README))
local_images.update(re.findall(r'!\[[^\]]*\]\(([^)]+)\)', README))
missing_images = []
for image in sorted(local_images):
    clean_image = image.split("#", 1)[0].split("?", 1)[0]
    if clean_image.startswith(("http://", "https://", "data:")):
        continue
    if not (ROOT / clean_image).is_file():
        missing_images.append(clean_image)
require(not missing_images, f"Missing local images: {missing_images}")

product_backlog = README.split("## 3.3 Product Backlog", 1)[1].split("## 3.4 Impact Mapping", 1)[0]
to_be_backlog = README.split("### 8.3.2 To Be Product Backlog", 1)[1].split(
    "# Conclusiones", 1
)[0]
story_rows = re.findall(r"^\|\s*\d+\s*\|\s*(?:US|TS)-\d+[AB]?\s*\|.*$", product_backlog + to_be_backlog, re.MULTILINE)
require(story_rows, "No Product Backlog story rows were found.")
for row in story_rows:
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    points = int(cells[4])
    require(points in {1, 2, 3, 5}, f"Invalid Story Points value in row: {row}")

planning_file = ROOT / 'planning' / 'trello-cards.json'
require(planning_file.is_file(), 'Missing traceable planning backlog')
planning = json.loads(planning_file.read_text(encoding='utf-8'))
cards = planning['cards']
require(len(cards) == 47, 'Expected 47 distinct backlog items')
require(len({card['id'] for card in cards}) == len(cards), 'Duplicate planning identifiers')
for prefix, count, total in (('US-', 21, 95), ('NF-', 6, 18), ('TECH-', 4, 16)):
    selected = [c for c in cards if c['id'].startswith(prefix) and c['type'] != 'Experimento']
    require(len(selected) == count, f'Unexpected count for {prefix}')
    require(sum(c['sp'] for c in selected) == total, f'Unexpected points for {prefix}')
spikes = [c for c in cards if c['type'] == 'Spike']
require(len(spikes) == 3 and all(c['sp'] is None and c['timebox_hours'] == 4 for c in spikes),
        'Spikes require a four-hour timebox and no story points')
experimental = [c for c in cards if c['type'] == 'Experimento']
require(len(experimental) == 13 and sum(c['sp'] for c in experimental) == 53, 'To-Be scope changed')
require(all(c['status'] == 'Backlog' for c in experimental), 'Unverified experiment marked as completed')
for c in cards:
    require(c['sp'] is None or c['sp'] in {1,2,3,5}, f'Invalid estimate: {c["id"]}')
    require(c['description'].strip(), f'Missing acceptance or evidence: {c["id"]}')
require(planning.get('board_url') or planning['sync_status'] == 'NOT_SYNCED_AUTH_REQUIRED',
        'Trello sync must have a real board URL or a truthful authentication state')
if planning['sync_status'] == 'SYNCED':
    sync = json.loads((ROOT/'planning/trello-sync-result.json').read_text(encoding='utf-8'))
    require(sync['actual_cards'] == 64 and len(sync['cards']) == 64, 'Incomplete Trello board')
    require(len({c['id'] for c in sync['cards']}) == 64, 'Duplicate Trello identifiers')
    require(not sync['missing'] and not sync['status_mismatches'] and not sync['missing_descriptions'],
            'Trello synchronization discrepancies')
    require(all(c['description_saved'] and c['url'].startswith('https://trello.com/c/') for c in sync['cards']),
            'Trello cards missing verified description or URL')
    require(planning['board_url'] in README, 'Report lacks verified Trello board URL')

team_members = {
    "Loa Rojas, Jean Franck": "U20241E406",
    "Jairo Mathias Santiago Atanacio": "U202418755",
    "Rivera Rupay, Fabricio Jose": "U202423883",
    "Renzo Zamir Revilla Quispe": "U201717085",
    "Brayan Benjamin Huerta Cardenas": "U20241E550",
}
for member_name, member_code in team_members.items():
    require(member_name in README, f"Team member is missing: {member_name}")
    require(member_code in README, f"Team member code is missing: {member_code}")

result = {
    'planning_cards_checked': len(cards),
    'spikes_checked': len(spikes),
    "story_rows_checked": len(story_rows),
    "local_images_checked": len(local_images),
    "raw_mermaid_blocks": 0,
    "required_assets_checked": len(required_assets),
    "required_sections_checked": len(required_headings),
    "team_members_checked": len(team_members),
}
print(json.dumps(result, indent=2))
