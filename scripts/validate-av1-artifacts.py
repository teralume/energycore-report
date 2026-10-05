from __future__ import annotations

import hashlib
import json
import pathlib
import zipfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
ZIP_PATH = (
    ROOT
    / "output"
    / "zip"
    / "upc-pre-202610-1asi0732-9100-teralume-artifacts-av1.zip"
)
PPTX_PATH = (
    ROOT
    / "output"
    / "keynote"
    / "upc-pre-202610-1asi0732-9100-teralume-keynote-av1.pptx"
)
PDF_PATH = (
    ROOT
    / "output"
    / "keynote"
    / "upc-pre-202610-1asi0732-9100-teralume-keynote-av1.pdf"
)


with zipfile.ZipFile(ZIP_PATH) as archive:
    checksum_lines = (
        archive.read("SHA256SUMS.txt").decode("utf-8-sig").splitlines()
    )
    checked = 0
    for checksum_line in checksum_lines:
        expected, name = checksum_line.split("  ", 1)
        actual = hashlib.sha256(archive.read(name)).hexdigest()
        if actual != expected:
            raise RuntimeError(f"Checksum mismatch: {name}")
        checked += 1
    entries = len(archive.namelist())

if PPTX_PATH.read_bytes()[:2] != b"PK":
    raise RuntimeError("The Keynote PPTX does not have a valid ZIP signature.")
if PDF_PATH.read_bytes()[:5] != b"%PDF-":
    raise RuntimeError("The Keynote PDF does not have a valid PDF signature.")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
member_codes = {
    "U20241E406",
    "U202418755",
    "U202423883",
    "U201717085",
    "U20241E550",
}
missing_team_members = sorted(code for code in member_codes if code not in readme)
if missing_team_members:
    raise RuntimeError(
        f"Missing team members in the report: {missing_team_members}"
    )

print(
    json.dumps(
        {
            "zip_bytes": ZIP_PATH.stat().st_size,
            "zip_entries": entries,
            "checksums_verified": checked,
            "keynote_pptx_bytes": PPTX_PATH.stat().st_size,
            "keynote_pdf_bytes": PDF_PATH.stat().st_size,
            "team_members": len(member_codes),
        },
        indent=2,
    )
)
