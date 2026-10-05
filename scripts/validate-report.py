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
    "### 8.3.3 Pipeline Supported Experiment Driven To Be Software Platform Lifecycle", 1
)[0]
story_rows = re.findall(r"^\|\s*\d+\s*\|\s*(?:US|TS)-\d+\s*\|.*$", product_backlog + to_be_backlog, re.MULTILINE)
require(story_rows, "No Product Backlog story rows were found.")
for row in story_rows:
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    points = int(cells[4])
    require(points in {1, 2, 3, 5}, f"Invalid Story Points value in row: {row}")

for member_data in (
    "Rivera Rupay, Fabricio Jose",
    "U202423883",
    "u202423883@upc.edu.pe",
    "Fabricio1924",
):
    require(member_data in README, f"Fabricio profile/outcome data is missing: {member_data}")

result = {
    "story_rows_checked": len(story_rows),
    "local_images_checked": len(local_images),
    "raw_mermaid_blocks": 0,
    "required_assets_checked": len(required_assets),
    "required_sections_checked": len(required_headings),
}
print(json.dumps(result, indent=2))
