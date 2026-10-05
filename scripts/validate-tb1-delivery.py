"""Validate the final TB1 delivery without modifying artifacts."""

from __future__ import annotations

import hashlib
import re
import sys
import zipfile
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[1]
COURSE = REPO.parent
DELIVERY = COURSE / "Entregables" / "TB1"
EXPECTED = {
    "upc-pre-202610-1asi0732-9100-teralume-report-tb1.pdf",
    "upc-pre-202610-1asi0732-9100-teralume-keynote-tb1.pptx",
    "upc-pre-202610-1asi0732-9100-teralume-keynote-tb1.pdf",
    "upc-pre-202610-1asi0732-9100-teralume-performance-tb1.docx",
    "upc-pre-202610-1asi0732-9100-teralume-performance-tb1.pdf",
    "upc-pre-202610-1asi0732-9100-teralume-artifacts-tb1.zip",
    "upc-pre-202610-1asi0732-9100-teralume-expo-tb1.mp4",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


files = {path.name for path in DELIVERY.iterdir() if path.is_file()}
require(files == EXPECTED, f"Delivery contents differ: {sorted(files ^ EXPECTED)}")
for name in EXPECTED:
    require((DELIVERY / name).stat().st_size > 0, f"Empty file: {name}")

report = DELIVERY / "upc-pre-202610-1asi0732-9100-teralume-report-tb1.pdf"
report_reader = PdfReader(str(report))
report_text = "\n".join(page.extract_text() or "" for page in report_reader.pages)
require(len(report_reader.pages) >= 80, "Report unexpectedly short")
for needle in ("TB1.1", "About-the-Product", "Sprint 2", "28 pruebas JUnit", "109 pruebas automatizadas", "exposición consolidada de AV1"):
    require(needle.casefold() in report_text.casefold(), f"Report text missing: {needle}")
report_links = []
for page in report_reader.pages:
    for annotation_ref in page.get("/Annots", []):
        annotation = annotation_ref.get_object()
        action = annotation.get("/A")
        if action and action.get("/URI"):
            report_links.append(str(action.get("/URI")))
require(any("4HOjUHXYUsA" in link for link in report_links), "Report lacks About-the-Product YouTube link")

keynote_pdf = DELIVERY / "upc-pre-202610-1asi0732-9100-teralume-keynote-tb1.pdf"
require(len(PdfReader(str(keynote_pdf)).pages) == 21, "Keynote PDF must have 21 pages")

performance_pdf = DELIVERY / "upc-pre-202610-1asi0732-9100-teralume-performance-tb1.pdf"
performance_reader = PdfReader(str(performance_pdf))
require(len(performance_reader.pages) == 1, "Performance PDF must have one page")
performance_text = performance_reader.pages[0].extract_text() or ""
for needle in ("TB1", "U20241E406", "U202418755", "U202423883", "U201717085", "U20241E550"):
    require(needle.casefold() in performance_text.casefold(), f"Performance text missing: {needle}")
require(performance_text.count("20") >= 5, "Performance report lacks five scores of 20")

pptx = DELIVERY / "upc-pre-202610-1asi0732-9100-teralume-keynote-tb1.pptx"
with zipfile.ZipFile(pptx) as archive:
    slides = [
        name for name in archive.namelist()
        if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)
    ]
require(len(slides) == 21, "Keynote PPTX must have 21 slides")

artifact_zip = DELIVERY / "upc-pre-202610-1asi0732-9100-teralume-artifacts-tb1.zip"
with zipfile.ZipFile(artifact_zip) as archive:
    bad_entry = archive.testzip()
    require(bad_entry is None, f"Corrupt ZIP entry: {bad_entry}")
    names = set(archive.namelist())
    for required in (
        "MANIFEST.md",
        "SHA256SUMS.txt",
        "report/README.md",
        "presentation/test-demo-guide-tb1.md",
        "deployment/deployment-result.local.json",
        "evidence/openapi-live.json",
        "evidence/energy-power-smoke.json",
        "evidence/preferences-concurrency-smoke.json",
        "mobile/app-release.apk",
        "mobile/app-release.apk.sha1",
    ):
        require(required in names, f"ZIP entry missing: {required}")

source_expo = COURSE / "Entregables" / "AV1" / "upc-pre-202610-1asi0732-9100-teralume-expo-av1.mp4"
source_about = COURSE / "About the product" / "upc-pre-202610-1asi0732-9100-teralume-about-the-product-sprint-1.mp4"
delivery_expo = DELIVERY / "upc-pre-202610-1asi0732-9100-teralume-expo-tb1.mp4"
require(sha256(source_expo) == sha256(delivery_expo), "Reused AV1 exposition hash differs")
require(source_about.is_file() and source_about.stat().st_size > 0, "About-the-Product source video is unavailable")

readme = (REPO / "README.md").read_text(encoding="utf-8")
require(not re.search(r"\b(?:pendiente|pendientes|faltante|faltantes)\b", readme, re.I), "README contains pending wording")

print(f"PASS: {len(EXPECTED)} delivery files")
print(f"PASS: report_pages={len(report_reader.pages)}")
print("PASS: keynote_slides=21")
print("PASS: performance_pages=1")
print("PASS: ZIP integrity and required entries")
print(f"PASS: expo_sha256={sha256(delivery_expo)}")
print(f"PASS: about_source_sha256={sha256(source_about)}")
