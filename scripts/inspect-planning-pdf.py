"""Verify new planning content is present in the report PDF and locate QA pages."""
from pathlib import Path
import json
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
reader = PdfReader(root/'output/pdf/upc-pre-202610-1asi0732-9100-teralume-report-tb1.pdf')
pages = [p.extract_text() or '' for p in reader.pages]
required = ['Historias no funcionales','Technical Stories','Spike Stories',
            'Datos cuantitativos y criterio de capacidad','Sprint Planning por incremento',
            'SPIKE-01','TECH-04','NF-06','95 SP','53 SP']
found = {}
for needle in required:
    found[needle] = [i+1 for i,t in enumerate(pages) if needle in t]
    assert found[needle], f'Missing PDF text: {needle}'
sync_path=root/'planning/trello-sync-result.json'
if sync_path.is_file():
    sync=json.loads(sync_path.read_text(encoding='utf-8'))
    links=[]
    for page in reader.pages:
        for ref in page.get('/Annots',[]):
            action=ref.get_object().get('/A')
            if action and action.get('/URI'):
                links.append(str(action['/URI']))
    assert sync['board_url'] in links, 'PDF lacks clickable verified Trello board link'
print(json.dumps({'pages':len(pages),'planning_pages':found},ensure_ascii=False,indent=2))
