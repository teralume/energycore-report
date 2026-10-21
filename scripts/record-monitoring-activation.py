"""Record an actually successful main-branch monitoring run and update its documentation."""
import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('run_id',type=int)
args=parser.parse_args()

def gh(*arguments):
    return subprocess.check_output(['gh',*arguments],text=True,encoding='utf-8')

run=json.loads(gh('run','view',str(args.run_id),'--repo','teralume/energycore-report',
                  '--json','databaseId,headSha,headBranch,conclusion,status,url,workflowName,event'))
assert run['headBranch']=='main' and run['conclusion']=='success' and run['status']=='completed',run
assert run['workflowName']=='Public surface monitoring'
workflow=json.loads(gh('api','repos/teralume/energycore-report/actions/workflows/monitoring.yml'))
assert workflow['state']=='active'
directory=root/'tmp'/f'monitoring-{args.run_id}'
directory.mkdir(parents=True,exist_ok=True)
gh('run','download',str(args.run_id),'--repo','teralume/energycore-report',
   '--name',f'monitoring-{args.run_id}','--dir',str(directory))
probe=json.loads(next(directory.rglob('latest.json')).read_text(encoding='utf-8'))
assert probe['passed'] and len(probe['checks'])==3 and all(c['passed'] for c in probe['checks'])
record={'verified_at_utc':datetime.now(timezone.utc).isoformat(),'workflow_state':workflow['state'],
        'default_branch':'main','schedule_utc':'17 */6 * * *','run':run,'probe':probe,
        'limitations':'Activation and a successful synthetic run; no uptime SLA or user validation claim.'}
target=root/'assets/evidence/implemented/av2-monitoring-activation-2026-10-21.json'
target.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')

file=root/'README.md'
text=file.read_text(encoding='utf-8')
text=text.replace('el reporte contiene además cambios AV2 locales todavía no publicados.',
                  'esta tabla conserva la línea base inspeccionada antes de publicar los cambios AV2. La activación remota se acredita por separado en 7.4.')
text=text.replace('El workflow [`monitoring.yml`](.github/workflows/monitoring.yml) está preparado para ejecución manual, cambios del monitor y una programación de seis horas.',
                  'El workflow [`monitoring.yml`](.github/workflows/monitoring.yml) está publicado y activo en `main`: admite ejecución manual, cambios del monitor y una programación de seis horas (minuto 17, UTC).')
text=text.replace('La programación remota entra en funcionamiento al publicar el workflow en la rama predeterminada; no se presenta como ya activada ni como historial de disponibilidad.',
                  f"La activación se verificó mediante el estado `active` del workflow y una [ejecución exitosa en main]({run['url']}). El [registro de activación y resultado remoto](assets/evidence/implemented/av2-monitoring-activation-2026-10-21.json) identifica commit, ejecución y las tres comprobaciones aprobadas. Esta evidencia inicial no constituye historial de disponibilidad ni un SLA.")
text=text.replace('El monitoreo sintético ya cuenta con una comprobación pública y un workflow preparado; faltan su ejecución remota sostenida, la revisión humana por pares y los informes de auditoría entre grupos.',
                  'El monitoreo sintético ya está activo en GitHub Actions y cuenta con una ejecución remota aprobada; faltan acumular historial, la revisión humana por pares y los informes de auditoría entre grupos.')
text=text.replace('monitoreo público verificado y el kit de auditoría UX', 'monitoreo público verificado y el kit de auditoría UX')
file.write_text(text,encoding='utf-8')
audit=root/'planning/av2-scope-audit.md'
text=audit.read_text(encoding='utf-8').replace('Comprobación pública PASS, tres pruebas del monitor y workflow preparado | Falta activar el workflow remoto y observar historial; sin SLA ni percentiles medidos',
    'Comprobación pública PASS, tres pruebas del monitor y workflow activo con ejecución remota PASS | Falta observar historial; sin SLA ni percentiles medidos')
audit.write_text(text,encoding='utf-8')
print(json.dumps({'workflow':'active','run':run['url'],'checks':len(probe['checks'])}))
