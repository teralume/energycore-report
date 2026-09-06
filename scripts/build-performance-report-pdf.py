from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "upc-pre-202610-1asi0732-9100-teralume-performance-av1.pdf"
UPC_LOGO = ROOT / "assets" / "front-matter" / "upc-logo.png"

GREEN = colors.HexColor("#16884A")
DARK = colors.HexColor("#14231A")
PALE = colors.HexColor("#EAF7EF")
GRAY = colors.HexColor("#5F6B63")
WHITE = colors.white

PAGE = landscape(A4)
WIDTH, HEIGHT = PAGE


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(GREEN)
    canvas.drawRightString(WIDTH - 1.5 * cm, HEIGHT - 1.05 * cm, "TERALUME / ENERGYCORE / AV1")
    canvas.setStrokeColor(colors.HexColor("#C9DED1"))
    canvas.line(1.5 * cm, HEIGHT - 1.25 * cm, WIDTH - 1.5 * cm, HEIGHT - 1.25 * cm)
    canvas.setFillColor(GRAY)
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(WIDTH - 1.5 * cm, 0.85 * cm, f"Página {doc.page}")
    canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="Eyebrow",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10,
    leading=12,
    textColor=GREEN,
    alignment=TA_CENTER,
    spaceAfter=12,
))
styles.add(ParagraphStyle(
    name="CoverTitle",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=28,
    leading=32,
    textColor=DARK,
    alignment=TA_CENTER,
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="CoverSubtitle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=15,
    leading=18,
    textColor=GRAY,
    alignment=TA_CENTER,
    spaceAfter=18,
))
styles.add(ParagraphStyle(
    name="SectionTitle",
    parent=styles["Heading1"],
    fontName="Helvetica-Bold",
    fontSize=21,
    leading=25,
    textColor=DARK,
    spaceAfter=10,
))
styles.add(ParagraphStyle(
    name="BodySmall",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=11,
    textColor=DARK,
))
styles.add(ParagraphStyle(
    name="Body",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=9.5,
    leading=13,
    textColor=DARK,
))
styles.add(ParagraphStyle(
    name="Center",
    parent=styles["BodyText"],
    fontName="Helvetica-Bold",
    fontSize=10.5,
    leading=14,
    textColor=DARK,
    alignment=TA_CENTER,
))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc = BaseDocTemplate(
    str(OUTPUT),
    pagesize=PAGE,
    leftMargin=1.5 * cm,
    rightMargin=1.5 * cm,
    topMargin=1.6 * cm,
    bottomMargin=1.3 * cm,
    title="Participant Performance Report — Teralume EnergyCore — AV1",
    author="Jean Franck Loa Rojas",
    subject="Diseño de Experimentos de Ingeniería de Software",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates(PageTemplate(id="report", frames=[frame], onPage=header_footer))

story = []
if UPC_LOGO.exists():
    logo = Image(str(UPC_LOGO), width=5.0 * cm, height=1.9 * cm, kind="proportional")
    logo.hAlign = "CENTER"
    story.extend([Spacer(1, 0.5 * cm), logo, Spacer(1, 0.65 * cm)])

story.extend([
    Paragraph("DISEÑO DE EXPERIMENTOS DE INGENIERÍA DE SOFTWARE", styles["Eyebrow"]),
    Paragraph("Participant Performance Report", styles["CoverTitle"]),
    Paragraph("Reporte individual de desempeño — Hito AV1", styles["CoverSubtitle"]),
])

cover_data = [
    [Paragraph("<b>Startup</b>", styles["Body"]), Paragraph("<b>Teralume</b>", styles["Body"])],
    [Paragraph("<b>Producto</b>", styles["Body"]), Paragraph("<b>EnergyCore</b>", styles["Body"])],
    [Paragraph("<b>NRC / Entrega</b>", styles["Body"]), Paragraph("<b>9100 / AV1</b>", styles["Body"])],
    [Paragraph("<b>Docente</b>", styles["Body"]), Paragraph("<b>Alex Humberto Sánchez Ponce</b>", styles["Body"])],
]
cover = Table(cover_data, colWidths=[5 * cm, 11 * cm], rowHeights=[0.85 * cm] * 4, hAlign="CENTER")
cover.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), GREEN),
    ("BACKGROUND", (1, 0), (1, -1), PALE),
    ("TEXTCOLOR", (0, 0), (0, -1), WHITE),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 12),
    ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#C9DED1")),
]))
story.extend([
    cover,
    Spacer(1, 0.65 * cm),
    Paragraph("Jean Franck Loa Rojas · U20241E406 · Séptimo ciclo", styles["Center"]),
    Spacer(1, 0.25 * cm),
    Paragraph("Documento elaborado siguiendo la estructura del Anexo B del enunciado del curso.", ParagraphStyle(
        "FootNote", parent=styles["Body"], textColor=GRAY, alignment=TA_CENTER, fontName="Helvetica-Oblique"
    )),
    PageBreak(),
    Paragraph("Evaluación individual del participante", styles["SectionTitle"]),
])

metadata = Table([
    [Paragraph("<b>Startup Name:</b> Teralume", styles["Body"]), Paragraph("<b>Product Name:</b> EnergyCore", styles["Body"])],
    [Paragraph("<b>Delivery:</b> AV1", styles["Body"]), Paragraph("<b>Team Leader:</b> Jean Franck Loa Rojas — U20241E406", styles["Body"])],
], colWidths=[12.5 * cm, 12.5 * cm], hAlign="LEFT")
metadata.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), PALE),
    ("BOX", (0, 0), (-1, -1), 0.6, GREEN),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#C9DED1")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
]))
story.extend([metadata, Spacer(1, 0.45 * cm)])

headers = [
    "Ítem", "Estudiante", "Responsabilidades asignadas", "Cumplió a tiempo",
    "Cumplió tarde", "Cumplió parcialmente", "No cumplió", "Nota",
]
responsibilities = (
    "Configuración de repositorios y GitFlow; rebranding ElectroCorp → EnergyCore; arquitectura DDD y REST API; "
    "frontend Angular; Landing Page; aplicación Flutter Android; diseño UX/UI; pruebas; documentación y preparación "
    "de despliegue Cloud Run, Firebase y Neon."
)
row = [
    "1",
    "Jean Franck Loa Rojas<br/>U20241E406",
    responsibilities,
    "X",
    "",
    "",
    "",
    "20",
]
table_data = [
    [Paragraph(f"<b>{value}</b>", ParagraphStyle("H", parent=styles["BodySmall"], textColor=WHITE, alignment=TA_CENTER)) for value in headers],
    [Paragraph(value, ParagraphStyle(
        f"R{index}", parent=styles["BodySmall"], alignment=TA_LEFT if index in (1, 2) else TA_CENTER,
        textColor=GREEN if index in (3, 7) else DARK, fontName="Helvetica-Bold" if index in (0, 1, 3, 7) else "Helvetica"
    )) for index, value in enumerate(row)],
]
performance = Table(
    table_data,
    colWidths=[1 * cm, 3.2 * cm, 10.2 * cm, 2.2 * cm, 2.0 * cm, 2.35 * cm, 1.8 * cm, 1.2 * cm],
    rowHeights=[1.1 * cm, 3.15 * cm],
    repeatRows=1,
)
performance.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), GREEN),
    ("BACKGROUND", (0, 1), (-1, 1), WHITE),
    ("BACKGROUND", (0, 1), (0, 1), PALE),
    ("BACKGROUND", (3, 1), (3, 1), PALE),
    ("BACKGROUND", (7, 1), (7, 1), PALE),
    ("GRID", (0, 0), (-1, -1), 0.55, colors.HexColor("#94B6A0")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
]))
story.extend([
    performance,
    Spacer(1, 0.3 * cm),
    Paragraph("<b>Escala del Anexo B:</b> 20 = cumplió a tiempo · 16 = cumplió tarde · 13 = cumplió parcialmente · 07/00 = no cumplió.", ParagraphStyle(
        "Legend", parent=styles["Body"], textColor=GRAY
    )),
    Spacer(1, 0.35 * cm),
    Paragraph("<font color='#16884A'><b>Evidencia considerada</b></font>", ParagraphStyle(
        "EvidenceTitle", parent=styles["Body"], fontSize=13, leading=16
    )),
])

evidence = [
    "Implementación presente en los cinco repositorios EnergyCore y ramas GitFlow preparadas para AV1.",
    "Validaciones registradas en el Project Report: backend, Angular y Flutter, con sus límites explícitos.",
    "Wireframes, mockups, flujo de usuario y capturas funcionales incorporados al repositorio del informe.",
    "Preparación reproducible de Cloud Run, Firebase Hosting y PostgreSQL administrado en Neon.",
]
for item in evidence:
    story.append(Paragraph(f"• {item}", styles["Body"]))

observation_table = Table([
    [Paragraph(
        "<i>Observación: esta valoración corresponde al aporte individual documentado para AV1. "
        "La nota definitiva está sujeta a la revisión del docente y a la evidencia publicada en GitHub.</i>",
        ParagraphStyle("Observation", parent=styles["BodySmall"], textColor=GRAY, leading=10),
    )],
], colWidths=[24.5 * cm], hAlign="LEFT")
observation_table.setStyle(TableStyle([
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
]))
signature_table = Table([
    ["_______________________________", "_______________________________"],
    ["Jean Franck Loa Rojas\nTeam Leader", "Fecha de entrega AV1"],
], colWidths=[9 * cm, 9 * cm], hAlign="CENTER", style=TableStyle([
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8.5),
    ("TEXTCOLOR", (0, 0), (-1, -1), DARK),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
]))
story.extend([
    Spacer(1, 0.2 * cm),
    observation_table,
    Spacer(1, 0.25 * cm),
    signature_table,
])

doc.build(story)
print(OUTPUT)
