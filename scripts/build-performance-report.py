from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "docx" / "upc-pre-202610-1asi0732-9100-teralume-performance-av1.docx"
UPC_LOGO = ROOT / "assets" / "front-matter" / "upc-logo.png"
PROFILE_PHOTO = ROOT / "assets" / "team" / "jean-loa.jpg"

GREEN = "16884A"
DARK = "14231A"
PALE = "EAF7EF"
GRAY = "5F6B63"
WHITE = "FFFFFF"


def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_text(cell, text, *, bold=False, color=DARK, size=9, align=WD_ALIGN_PARAGRAPH.CENTER):
    cell.text = ""
    paragraph = cell.paragraphs[0]
    paragraph.alignment = align
    paragraph.paragraph_format.space_after = Pt(0)
    run = paragraph.add_run(text)
    run.bold = bold
    run.font.name = "Aptos"
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor.from_string(color)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def add_label_value(document, label, value):
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_after = Pt(4)
    label_run = paragraph.add_run(f"{label}: ")
    label_run.bold = True
    label_run.font.color.rgb = RGBColor.from_string(GREEN)
    value_run = paragraph.add_run(value)
    value_run.font.color.rgb = RGBColor.from_string(DARK)


def add_page_number(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = paragraph.add_run("Página ")
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instruction = OxmlElement("w:instrText")
    instruction.set(qn("xml:space"), "preserve")
    instruction.text = "PAGE"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.extend([begin, instruction, end])


document = Document()
section = document.sections[0]
section.top_margin = Cm(1.8)
section.bottom_margin = Cm(1.6)
section.left_margin = Cm(2.0)
section.right_margin = Cm(2.0)

styles = document.styles
styles["Normal"].font.name = "Aptos"
styles["Normal"].font.size = Pt(10.5)
styles["Normal"].font.color.rgb = RGBColor.from_string(DARK)
styles["Title"].font.name = "Aptos Display"
styles["Title"].font.size = Pt(27)
styles["Title"].font.bold = True
styles["Title"].font.color.rgb = RGBColor.from_string(DARK)

header = section.header
header_paragraph = header.paragraphs[0]
header_paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
header_run = header_paragraph.add_run("TERALUME  /  ENERGYCORE  /  AV1")
header_run.bold = True
header_run.font.size = Pt(8)
header_run.font.color.rgb = RGBColor.from_string(GREEN)
add_page_number(section.footer.paragraphs[0])

if UPC_LOGO.exists():
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run().add_picture(str(UPC_LOGO), width=Inches(2.05))

document.add_paragraph()
eyebrow = document.add_paragraph()
eyebrow.alignment = WD_ALIGN_PARAGRAPH.CENTER
eyebrow_run = eyebrow.add_run("DISEÑO DE EXPERIMENTOS DE INGENIERÍA DE SOFTWARE")
eyebrow_run.bold = True
eyebrow_run.font.size = Pt(10)
eyebrow_run.font.color.rgb = RGBColor.from_string(GREEN)

title = document.add_paragraph(style="Title")
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
title.add_run("Participant Performance Report")

subtitle = document.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
subtitle_run = subtitle.add_run("Reporte individual de desempeño — Hito AV1")
subtitle_run.font.size = Pt(15)
subtitle_run.font.color.rgb = RGBColor.from_string(GRAY)

document.add_paragraph()
cover_table = document.add_table(rows=4, cols=2)
cover_table.alignment = WD_TABLE_ALIGNMENT.CENTER
cover_table.autofit = False
cover_table.columns[0].width = Cm(5)
cover_table.columns[1].width = Cm(10)
cover_data = [
    ("Startup", "Teralume"),
    ("Producto", "EnergyCore"),
    ("NRC / Entrega", "9100 / AV1"),
    ("Docente", "Alex Humberto Sánchez Ponce"),
]
for row, (label, value) in zip(cover_table.rows, cover_data):
    shade(row.cells[0], GREEN)
    shade(row.cells[1], PALE)
    set_cell_text(row.cells[0], label, bold=True, color=WHITE, size=10)
    set_cell_text(row.cells[1], value, bold=True, color=DARK, size=10, align=WD_ALIGN_PARAGRAPH.LEFT)

document.add_paragraph()
student = document.add_paragraph()
student.alignment = WD_ALIGN_PARAGRAPH.CENTER
student_run = student.add_run("Jean Franck Loa Rojas  ·  U20241E406  ·  Séptimo ciclo")
student_run.bold = True
student_run.font.size = Pt(12)

note = document.add_paragraph()
note.alignment = WD_ALIGN_PARAGRAPH.CENTER
note_run = note.add_run("Documento elaborado siguiendo la estructura del Anexo B del enunciado del curso.")
note_run.italic = True
note_run.font.size = Pt(9)
note_run.font.color.rgb = RGBColor.from_string(GRAY)

document.add_section(WD_SECTION.NEW_PAGE)
section = document.sections[-1]
section.top_margin = Cm(1.8)
section.bottom_margin = Cm(1.6)
section.left_margin = Cm(1.4)
section.right_margin = Cm(1.4)
section.header.is_linked_to_previous = True
section.footer.is_linked_to_previous = True

heading = document.add_paragraph()
heading_run = heading.add_run("Evaluación individual del participante")
heading_run.bold = True
heading_run.font.size = Pt(21)
heading_run.font.color.rgb = RGBColor.from_string(DARK)

add_label_value(document, "Startup Name", "Teralume")
add_label_value(document, "Product Name", "EnergyCore")
add_label_value(document, "Delivery", "AV1")
add_label_value(document, "Team Leader", "Jean Franck Loa Rojas — U20241E406")

document.add_paragraph()
headers = [
    "Ítem",
    "Estudiante",
    "Responsabilidades asignadas",
    "Cumplió a tiempo",
    "Cumplió tarde",
    "Cumplió parcialmente",
    "No cumplió",
    "Nota",
]
table = document.add_table(rows=2, cols=len(headers))
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.style = "Table Grid"
widths = [0.7, 2.8, 7.8, 1.7, 1.5, 1.8, 1.4, 1.0]
for index, (cell, header_text) in enumerate(zip(table.rows[0].cells, headers)):
    cell.width = Cm(widths[index])
    shade(cell, GREEN)
    set_cell_text(cell, header_text, bold=True, color=WHITE, size=7.5)

responsibilities = (
    "Configuración de repositorios y GitFlow; rebranding ElectroCorp → EnergyCore; "
    "arquitectura DDD y REST API; frontend Angular; Landing Page; aplicación Flutter Android; "
    "diseño UX/UI; pruebas; documentación y preparación de despliegue Cloud Run, Firebase y Neon."
)
values = [
    "1",
    "Jean Franck Loa Rojas\nU20241E406",
    responsibilities,
    "X",
    "",
    "",
    "",
    "20",
]
for index, (cell, value) in enumerate(zip(table.rows[1].cells, values)):
    shade(cell, PALE if index in (0, 3, 7) else WHITE)
    set_cell_text(
        cell,
        value,
        bold=index in (0, 1, 3, 7),
        color=GREEN if index in (3, 7) else DARK,
        size=8.5 if index != 2 else 8,
        align=WD_ALIGN_PARAGRAPH.LEFT if index in (1, 2) else WD_ALIGN_PARAGRAPH.CENTER,
    )

document.add_paragraph()
legend = document.add_paragraph()
legend_run = legend.add_run("Escala del Anexo B: 20 = cumplió a tiempo · 16 = cumplió tarde · 13 = cumplió parcialmente · 07/00 = no cumplió.")
legend_run.bold = True
legend_run.font.size = Pt(9)
legend_run.font.color.rgb = RGBColor.from_string(GRAY)

evidence_heading = document.add_paragraph()
evidence_heading.paragraph_format.space_before = Pt(10)
evidence_run = evidence_heading.add_run("Evidencia considerada")
evidence_run.bold = True
evidence_run.font.size = Pt(14)
evidence_run.font.color.rgb = RGBColor.from_string(GREEN)

for item in [
    "Implementación presente en los cinco repositorios EnergyCore y ramas GitFlow preparadas para AV1.",
    "Validaciones registradas en el Project Report: backend, Angular y Flutter, con sus límites explícitos.",
    "Wireframes, mockups, flujo de usuario y capturas funcionales incorporados al repositorio del informe.",
    "Preparación reproducible de Cloud Run, Firebase Hosting y base de datos PostgreSQL administrada en Neon.",
]:
    paragraph = document.add_paragraph(style="List Bullet")
    paragraph.paragraph_format.space_after = Pt(3)
    paragraph.add_run(item)

observation = document.add_paragraph()
observation.paragraph_format.space_before = Pt(10)
observation_run = observation.add_run(
    "Observación: esta valoración corresponde al aporte individual documentado para AV1. "
    "La nota definitiva está sujeta a la revisión del docente y a la evidencia publicada en GitHub."
)
observation_run.italic = True
observation_run.font.size = Pt(9)
observation_run.font.color.rgb = RGBColor.from_string(GRAY)

signature_table = document.add_table(rows=2, cols=2)
signature_table.alignment = WD_TABLE_ALIGNMENT.CENTER
signature_table.autofit = False
for cell in signature_table.rows[0].cells:
    cell.height = Cm(1.3)
set_cell_text(signature_table.cell(1, 0), "Jean Franck Loa Rojas\nTeam Leader", bold=True, size=9)
set_cell_text(signature_table.cell(1, 1), "Fecha de entrega AV1", bold=True, size=9)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
document.save(OUTPUT)
print(OUTPUT)
