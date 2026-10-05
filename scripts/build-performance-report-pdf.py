"""Export the AV1 performance Word file to PDF with identical table layout.

Run build-performance-report.py first. Microsoft Word is required on Windows.
"""

from pathlib import Path
import subprocess


root = Path(__file__).resolve().parents[1]
stem = "upc-pre-202610-1asi0732-9100-teralume-performance-av1"
source = root / "output" / "docx" / f"{stem}.docx"
target = root / "output" / "pdf" / f"{stem}.pdf"

if not source.is_file():
    raise FileNotFoundError(f"Build the Word report first: {source}")
target.parent.mkdir(parents=True, exist_ok=True)


def ps_quote(path: Path) -> str:
    return "'" + str(path).replace("'", "''") + "'"


command = (
    "$ErrorActionPreference='Stop'; "
    f"$source={ps_quote(source)}; $target={ps_quote(target)}; "
    "$word=New-Object -ComObject Word.Application; "
    "try { $word.Visible=$false; $word.DisplayAlerts=0; "
    "$document=$word.Documents.Open($source,$false,$true); "
    "try { $document.ExportAsFixedFormat($target,17) } "
    "finally { $document.Close($false) } "
    "} finally { $word.Quit() }"
)
subprocess.run(["powershell.exe", "-NoProfile", "-Command", command], check=True)
if not target.is_file() or target.stat().st_size == 0:
    raise RuntimeError("Word did not produce a nonempty PDF")
print(target)
