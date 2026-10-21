"""Prepare a reviewable Trello payload; does not contact Trello or create accounts."""
from __future__ import annotations
import json
import csv
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
planning = root / 'planning'
backlog_path = planning / 'trello-cards.json'
payload = json.loads(backlog_path.read_text(encoding='utf-8'))
readme = (root / 'README.md').read_text(encoding='utf-8')
story_section = readme.split('## 3.2 User Stories',1)[1].split('### 3.2.1',1)[0]
acceptance = {}
for line in story_section.splitlines():
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if len(cells)==3 and re.fullmatch(r'US-\d+[AB]?',cells[0]):
        acceptance[cells[0]] = cells[2]
for card in payload['cards']:
    if card['type']=='Funcional':
        assert card['id'] in acceptance
        card['description'] = ('Criterio de aceptación: '+acceptance[card['id']]+'\n\n'
            'Estado: implementación registrada en Product Backlog; aceptación integral de UI por verificar.\n'
            'Evidencia: README §3.2 y §5.2, código del contexto y suites backend/frontend.\n'
            'No atribuir cierre individual ni fecha de ejecución sin evidencia.')
backlog_path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (planning/'trello-cards.csv').open('w',encoding='utf-8-sig',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=['id','title','type','sp','timebox_hours','sprint','status','description','owner'],extrasaction='ignore')
    writer.writeheader()
    writer.writerows(payload['cards'])

plans = (planning / 'sprint-planning.md').read_text(encoding='utf-8')
plan_cards = []
for block in re.split(r'(?=^## Sprint \d+:)',plans,flags=re.M)[1:]:
    first,description=block.split('\n',1)
    number = int(re.search(r'Sprint (\d+):',first)[1])
    plan_cards.append(dict(id=f'PLAN-{number:02}',title=first.removeprefix('## '),type='Planificación',
        sprint=number,sp=None,owner=None,status='Por iniciar' if number>=5 else 'Implementado - por verificar',
        description=description.strip()))
source=(planning/'sprint-4-source-before-refinement.md').read_text(encoding='utf-8')
task_cards=[]
for line in source.splitlines():
    if not line.startswith('| ET-'):continue
    c=[x.strip() for x in line.strip().strip('|').split('|')]
    ident,title,scope,hours,owner,state,evidence=c
    # Done in the previous source denotes an available artifact, not independently accepted work.
    current='Implementado - por verificar' if state=='Done' else 'Por iniciar'
    task_cards.append(dict(id=ident,title=title,type='Engineering Task',sprint=4,sp=None,
        estimated_hours=int(hours.split()[0]),owner=None,status=current,
        description=f'Ámbito: {scope}\nEstimación heredada: {hours}; horas reales no registradas.\n'
                    f'Responsable/frente propuesto en el registro: {owner}; confirmar antes de asignar.\n'
                    f'Cierre: {evidence}\n'
                    'La existencia de artefactos o una ejecución CI no acredita revisión o aceptación individual.'))
assert len(plan_cards)==7 and len(task_cards)==10
operations={**payload,'cards':payload['cards']+plan_cards+task_cards,
    'lists':['Backlog','Por iniciar','En curso','Implementado - por verificar','Verificado - pruebas y CI'],
    'visibility':'private','backlog_count':47,'planning_card_count':7,'engineering_task_count':10}
assert len(operations['cards'])==64
assert len({c['id'] for c in operations['cards']})==64
sync_path = planning/'trello-sync-result.json'
if sync_path.is_file():
    sync = json.loads(sync_path.read_text(encoding='utf-8'))
    remote = {c['id']: c for c in sync['cards']}
    assert len(remote) == 64 and not sync['missing'] and not sync['status_mismatches']
    for item in operations['cards']:
        assert item['status'] == remote[item['id']]['status']
        item['trello_url'] = remote[item['id']]['url']
    for item in payload['cards']:
        item['trello_url'] = remote[item['id']]['url']
    for target in (payload, operations):
        target['board_url'] = sync['board_url']
        target['sync_status'] = 'SYNCED'
        target['verified_at'] = sync['verified_at']
    backlog_path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(planning/'trello-board-prepared.json').write_text(json.dumps(operations,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f"Prepared: 47 backlog cards, 7 planning cards and 10 engineering tasks. {operations['sync_status']}.")
