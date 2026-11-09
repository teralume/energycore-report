"""Guard AV2 scope, including the live rubric's planned To-Be Sprint Backlog."""
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

# The partial review requires an individual history inside each ABET criterion.
criteria = re.findall(r'^\| \*\*4\.c\.[12] [^|]+\| ([^|]+)\| ([^|]+)\|$', text, re.M)
assert len(criteria) == 2, 'Expected two Student Outcome criteria'
team_codes = {'U20241E406', 'U202418755', 'U202423883', 'U201717085', 'U20241E550'}
for actions, conclusions in criteria:
    members = re.findall(r'· (U[0-9A-Z]+)\*\*(.*?)(?=<br><br>\*\*|$)', actions)
    assert len(members) == 5 and {code for code, _ in members} == team_codes
    for entry in [paragraph for _, paragraph in members] + [conclusions]:
        assert re.findall(r'\*\*(AV1|TB1|AV2):\*\*', entry) == ['AV1', 'TB1', 'AV2'], 'Missing milestone in ABET table'

planning=(root/'planning/sprint-planning-av2.md').read_text(encoding='utf-8')
to_be_plan=planning.split('## Sprint 5:',1)[1].split('## Tablero de seguimiento',1)[0]
report_plan=text.split('#### To-Be Sprint Backlog:',1)[1].split('# Conclusiones',1)[0]
task_pattern=r'^\| ((?:US|TS)-\d+[AB]?-[AB]) \| [^|]+ \| (\d+) \|'
planned_tasks=re.findall(task_pattern,to_be_plan,re.M)
report_tasks=re.findall(task_pattern,report_plan,re.M)
assert len(planned_tasks)==len(report_tasks)==26, 'Expected 26 engineering tasks in both planning and report'
assert len(dict(planned_tasks))==26, 'Duplicate planned task identifiers'
assert dict(planned_tasks)==dict(report_tasks), 'Report and planning estimates differ'
assert all(4<=int(hours)<=8 for _,hours in planned_tasks), 'Rubric requires tasks of 4 to 8 hours'
assert sum(int(hours) for _,hours in planned_tasks)==132
backlog=json.loads((root/'planning/trello-cards.json').read_text(encoding='utf-8'))
story_ids={card['id'] for card in backlog['cards'] if card['type']=='Experimento'}
assert {task.rsplit('-',1)[0] for task,_ in planned_tasks}==story_ids, 'Sprint tasks must cover the To-Be backlog'
assert 'propuestas por iniciar' in report_plan and 'responsables por asignar' in report_plan
assert 'Benchmark de herramientas DevOps' in text
benchmark=(root/'planning/devops-benchmark-av2.md').read_text(encoding='utf-8')
assert all(name in benchmark for name in ('GitHub Actions','GitLab CI/CD','Jenkins','retrospectiva'))

pdf_result=None
if '--pdf' in sys.argv:
    from pypdf import PdfReader
    pdf=root/'output/pdf/upc-pre-202610-1asi0732-9100-teralume-report-av2.pdf'
    reader=PdfReader(pdf)
    pdftext='\n'.join(p.extract_text() or '' for p in reader.pages)
    assert 'Informe de Avance 2' in pdftext
    assert '8.3.2' in pdftext
    assert 'To-Be Sprint Backlog' in pdftext and 'Benchmark de herramientas DevOps' in pdftext
    assert all(task in pdftext for task,_ in report_tasks), 'PDF omits planned engineering tasks'
    for token in ('8.3.3','8.3.4','8.4.1','8.5.1','8.6.1','GEES Framework'):
        assert token not in pdftext,f'Out-of-scope content remains in AV2 PDF: {token}'
    pdf_result={'pages':len(reader.pages),'scope_guard':'PASS'}

print(json.dumps({'required_av2_sections':len(required),'cutoff':'8.3.2 plus rubric-required planned sprint backlog','to_be_tasks':len(report_tasks),'estimated_hours':132,'evidence_gaps_remain':True,'pdf':pdf_result},indent=2))
