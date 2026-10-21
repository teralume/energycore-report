"""Guard the enumerated AV2 cutoff without claiming unfinished activities are complete."""
from pathlib import Path
import re
import json
import sys

root=Path(__file__).resolve().parents[1]
text=(root/'README.md').read_text(encoding='utf-8')
assert '# Informe de Avance 2' in text
required=['6.1','6.1.1','6.1.2','6.1.3','6.1.4','6.2','6.2.1','6.2.1.1','6.2.1.2','6.2.2',
          '6.3','6.3.1','6.3.2','6.3.3','6.4','6.4.1','6.4.1.1','6.4.1.2','6.4.1.3',
          '6.4.2','6.4.2.1','6.4.2.2','6.4.2.3','6.4.2.4',
          '7.1','7.1.1','7.1.2','7.2','7.2.1','7.2.2','7.3','7.3.1','7.3.2',
          '7.4','7.4.1','7.4.2','7.4.3','7.4.4',
          '8.1','8.1.1','8.1.2','8.1.3','8.1.4','8.1.5',
          '8.2','8.2.1','8.2.2','8.2.3','8.2.4','8.2.5','8.2.6','8.2.7','8.2.8','8.3','8.3.1','8.3.2']
headings=re.findall(r'^#{1,6} (\d+(?:\.\d+)*)\s',text,re.M)
assert not(set(required)-set(headings)),f'Missing AV2 headings: {set(required)-set(headings)}'
for number in headings:
    if number.startswith('8.'):
        parts=tuple(map(int,number.split('.')))
        assert parts < (8,3,3),f'Out-of-scope heading for AV2: {number}'
for token in ('# Video App Validation','# Video About the Team'):
    assert token not in text,f'Premature empty video section: {token}'
assert not re.search(r'^\| [567] \|.*(?:SP / Por iniciar|Propuesto / Por iniciar)',text,re.M)
assert 'No se contabiliza como entrevista de validación' in text

pdf_result=None
if '--pdf' in sys.argv:
    from pypdf import PdfReader
    pdf=root/'output/pdf/upc-pre-202610-1asi0732-9100-teralume-report-av2.pdf'
    reader=PdfReader(pdf)
    pdftext='\n'.join(p.extract_text() or '' for p in reader.pages)
    assert 'Informe de Avance 2' in pdftext
    assert '8.3.2' in pdftext
    for token in ('8.3.3','8.3.4','8.4.1','8.5.1','8.6.1','GEES Framework'):
        assert token not in pdftext,f'Out-of-scope content remains in AV2 PDF: {token}'
    pdf_result={'pages':len(reader.pages),'scope_guard':'PASS'}

print(json.dumps({'required_av2_sections':len(required),'cutoff':'8.3.2','evidence_gaps_remain':True,'pdf':pdf_result},indent=2))
