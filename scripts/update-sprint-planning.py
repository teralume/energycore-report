"""Refine existing report planning and generate a traceable Trello staging file."""
from __future__ import annotations

import csv
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "20/10/2026"
report_path = ROOT / "README.md"
report = report_path.read_text(encoding="utf-8")
if '### 3.2.1 Historias no funcionales' in report:
    raise SystemExit('Planning already refined; edit existing planning artifacts instead of duplicating sections.')
planning_dir = ROOT / "planning"
planning_dir.mkdir(exist_ok=True)

def section(text, start, end):
    return text.split(start, 1)[1].split(end, 1)[0]

def rows(text):
    return [[c.strip() for c in line.strip().strip('|').split('|')]
            for line in text.splitlines() if re.match(r'^\|\s*\d+\s*\|', line)]

functional = rows(section(report, "## 3.3 Product Backlog", "## 3.4 Impact Mapping"))
functional = [r for r in functional if r[1].startswith('US-')]
future = rows(section(report, "### 8.3.2 To Be Product Backlog", "### 8.3.3 Pipeline Supported"))
assert len(functional) == 21 and sum(int(r[4]) for r in functional) == 95
assert len(future) == 13 and sum(int(r[4]) for r in future) == 53

# A status is scoped: source implementation is not equivalent to production acceptance.
quality = [
    ("NF-01", "Autenticación y autorización", 3, "Verificado en pruebas", "Como titular de una cuenta, quiero que la API proteja mi sesión y permisos para impedir accesos no autorizados.", "0 peticiones protegidas sin token aceptadas; 100 % de casos Owner/Guest de la suite aprobados; BCrypt nunca almacena contraseña en claro.", "IAM: AccessAuthorizationServiceTest, PasswordHashingServiceTest e iam.feature; CI backend del 05/10/2026."),
    ("NF-02", "Consistencia de preferencias concurrentes", 3, "Verificado en pruebas", "Como usuario, quiero conservar mis preferencias cuando hay peticiones simultáneas para no perder cambios.", "24 GET iniciales simultáneos y 24 GET/PUT: una preferencia por usuario, cambios parciales conservados y aislamiento entre cuentas.", "assets/evidence/implemented/preferences-concurrency-smoke.json, 06/09/2026, PostgreSQL local aislado."),
    ("NF-03", "Latencia de consultas energéticas", 3, "Por verificar", "Como usuario, quiero recibir las consultas de dashboard e histórico dentro de un tiempo medible para tomar decisiones con fluidez.", "Objetivo propuesto: p95 <= 2000 ms y errores < 1 % en 100 consultas autenticadas, concurrencia 5; separar arranque frío y caliente y registrar entorno/dataset.", "No existe medición de carga que cierre este objetivo; requiere SPIKE-01."),
    ("NF-04", "Accesibilidad y adaptación de vistas", 3, "Por verificar", "Como usuario que navega con teclado o pantalla pequeña, quiero acceder a los controles esenciales sin perder información.", "Login y dashboard a 390/768/1440 px; 0 controles esenciales inaccesibles por teclado; 0 defectos críticos de accesibilidad en el alcance auditado.", "Hay estructura accesible y capturas; no una auditoría completa de estos criterios."),
    ("NF-05", "Recuperación móvil sin duplicación", 3, "Parcial", "Como usuario móvil, quiero recuperar una operación tras una desconexión sin repetir sus efectos.", "5 ciclos sin red/con red: sesión conservada, reintento visible y exactamente un cambio persistido por comando aceptado.", "Cliente con aviso/reintento; cierre de idempotencia y prueba en teléfono aún no demostrados. Relacionada con US-20A/B."),
    ("NF-06", "Compatibilidad móvil instalable", 3, "Parcial", "Como usuario, quiero instalar la aplicación y usar el mismo backend público desde mi dispositivo.", "APK Android release e iOS simulator compilan; login, lectura, CRUD y reporte ejecutados en Android físico con Wi-Fi/datos y API HTTPS pública.", "CI Android e iOS aprobado el 05/10/2026; distribución a testers y ejecución física de estos flujos no verificadas. Relacionada con TECH-04."),
]
technical = [
    ("TECH-01", "CI reproducible de los cinco repositorios", 5, "Verificado en CI", "Como equipo, queremos verificar cada cambio y publicar sus artefactos para detectar regresiones antes de integrar.", "5 workflows main exitosos en SHA identificable; fallos de tests detienen dependencias; artefactos descargables.", "Workflows main del 05/10/2026; métricas: 88 backend, 5 Angular, 5 Landing, 11 Flutter."),
    ("TECH-02", "Exportación CSV desde la API", 3, "Verificado en pruebas", "Como equipo, queremos exportar lecturas por un contrato HTTP consistente para conectar reportes y clientes.", "GET /api/v1/energy-readings/export devuelve text/csv; escenario de aceptación y manejo del rango aprobados.", "EnergyMonitoringController, EnergyReadingsCsvExporter y energy-monitoring.feature; CI backend."),
    ("TECH-03", "Trazabilidad DDD, JPA y diagramas", 3, "Implementado; revisión abierta", "Como equipo, queremos contrastar modelos y diagramas con el código para conservar coherencia entre capas y datos.", "27 entidades JPA contrastadas con ERD; FK/LFK identificadas; 0 imágenes locales ausentes y 0 bloques Mermaid crudos en reporte.", "Fuentes PlantUML y SVG, scripts/validate-report.py; revisión cruzada ET-06 aún sin acta individual."),
    ("TECH-04", "Distribución Android con API pública", 5, "Por iniciar", "Como equipo, queremos distribuir un APK firmado conectado a Cloud Run para demostrar móvil sin localhost.", "Release identificada por SHA, firma persistente, API_BASE_URL HTTPS pública, instalación desde enlace y 4 flujos verificados en Android físico.", "Existe APK de CI; no hay release de Firebase App Distribution ni evidencia de instalación desde enlace. Depende de SPIKE-03 y NF-06."),
]
spikes = [
    ("SPIKE-01", "Diseñar medición cuantitativa de rendimiento", "NF-03", "¿Cómo medir p95 y errores sin confundir cold start con latencia estable?", "Plan de carga, 100 consultas/5 concurrentes, dataset, versión, comandos y plantilla de resultados; no asignar cifras observadas antes de ejecutar."),
    ("SPIKE-02", "Definir diseño experimental e instrumentación", "TS-01, TS-02A/B, US-19", "¿Qué eventos, asignación y consentimiento permiten comparar variantes sin datos personales?", "ADR con alternativas, esquema mínimo, asignación estable, exclusiones, anonimización y decisión sobre piloto; no presentar 24 participantes propuestos como reclutados."),
    ("SPIKE-03", "Elegir distribución móvil para la demostración", "TECH-04, NF-06", "¿Qué canal permite instalar Android con API pública y qué limita la instalación en iPhone?", "ADR con canal Android, firma, requisitos, costos si aplican y acceso de testers; separar build de simulador, dispositivo físico y tienda."),
]

def table(headers, data):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join([':--']*len(headers)) + ' |'] + ['| ' + ' | '.join(str(c).replace('|','/') for c in r) + ' |' for r in data])

catalog = "### 3.2.1 Historias no funcionales\n\n"
catalog += "Los siguientes criterios convierten calidad en resultados observables. Los umbrales propuestos no se presentan como mediciones realizadas.\n\n"
catalog += table(["ID / SP", "Historia", "Criterio cuantitativo", "Estado y evidencia"], [(f'{x[0]} / {x[2]}',x[4],x[5],x[3]+'. '+x[6]) for x in quality])
catalog += "\n\n### 3.2.2 Technical Stories\n\nLos identificadores TECH identifican infraestructura y habilitadores del producto actual; se conservan TS-01 a TS-05 para el ciclo experimental del capítulo VIII.\n\n"
catalog += table(["ID / SP", "Historia técnica", "Condición de aceptación", "Estado y evidencia"], [(f'{x[0]} / {x[2]}',x[4],x[5],x[3]+'. '+x[6]) for x in technical])
catalog += "\n\n### 3.2.3 Spike Stories\n\nCada spike investiga una pregunta, tiene un límite de **4 horas propuestas** y entrega una decisión o un protocolo. No recibe Story Points y no cuenta como funcionalidad completada. Si no resuelve la pregunta dentro del límite, registra lo aprendido y refina el backlog.\n\n"
catalog += table(["ID", "Pregunta", "Dependencias", "Resultado de salida"], [(x[0],x[3],x[2],x[4]) for x in spikes])
catalog += "\n\nLos tres spikes se registran **Por iniciar**: hay antecedentes técnicos, pero no una investigación cerrada y fechada que cumpla estas condiciones.\n\n"
report = report.replace('## 3.3 Product Backlog',catalog+'## 3.3 Product Backlog',1)

extension = "### 3.3.1 Backlog de calidad, habilitadores e investigación\n\n"
extension += table(["ID", "Tipo", "Prioridad", "SP / timebox", "Estado real"], [(x[0],"No funcional","Must" if i in (0,1,4,5) else "Should",str(x[2])+" SP",x[3]) for i,x in enumerate(quality)] + [(x[0],"Técnica","Must",str(x[2])+" SP",x[3]) for x in technical] + [(x[0],"Spike","Must","4 h máximo propuesto","Por iniciar") for x in spikes])
extension += "\n\nLos **95 SP funcionales** se conservan; se agregan **18 SP no funcionales** y **16 SP técnicos**, separados del To-Be experimental de **53 SP**. Los **12 h de spikes** son límites propuestos de investigación; no se suman a SP ni representan horas trabajadas. Son 47 entradas de backlog: 21 funcionales actuales, 6 no funcionales, 4 técnicas, 3 spikes y 13 To-Be. Las historias relacionadas comparten pruebas de salida sin duplicar resultados ni computar el mismo esfuerzo dos veces. Las nuevas estimaciones requieren ratificación del equipo antes de comprometer capacidad.\n\n"
report = report.replace('## 3.4 Impact Mapping',extension+'## 3.4 Impact Mapping',1)

metrics = """### 5.2.1 Sprint Backlogs

**Actualización de planificación: 20/10/2026.** Se conserva la numeración histórica: Sprints 1-3 de preparación de AV1 y Sprint 4 de revisión TB1. El ciclo experimental continúa en Sprints 5-7; se evita el doble Sprint 4 que existía entre los capítulos V y VIII.

La planificación ampliada se encuentra en [Sprint Planning detallados](planning/sprint-planning.md) y las tarjetas preparadas en [backlog trazable](planning/trello-cards.json). El siguiente registro distingue reconstrucción histórica, revisión documental y trabajo por ejecutar.

#### 5.2.1.1 Datos cuantitativos y criterio de capacidad

| Dato | Valor y alcance | Fuente / fecha |
|:--|:--|:--|
| Backlog funcional | 21 historias / 95 SP | Product Backlog; estimación relativa, no horas ni velocidad observada |
| Verificación automatizada | 109 casos: 88 backend (28 JUnit + 60 BDD), 5 Angular, 5 Landing y 11 Flutter | Ejecuciones y CI main del 05/10/2026; 0 fallos y 0 omitidos en esas suites |
| CI de entrega | 5 repositorios con workflow main exitoso | GitHub Actions del 05/10/2026; evidencia histórica, no una nueva ejecución del 20/10 |
| Concurrencia de preferencias | 24 GET y 24 GET/PUT simultáneos con una fila por usuario | preferences-concurrency-smoke.json; 06/09/2026, PostgreSQL local aislado |
| Consumo de demostración | 1370 W / 3 dispositivos | energy-power-smoke.json; 06/09/2026, datos de demo; no ahorro real ni consumo poblacional |
| Sprint 4 documental | 10 tareas / 52 h estimadas | Desglose heredado del informe; sin tiempos reales para calcular eficiencia |
| Investigación nueva | 3 spikes / 4 h máximas cada uno | Propuesta del 20/10/2026, ejecución no iniciada |

No existen registros verificables de disponibilidad personal, horas reales, fechas de las reuniones o velocidad por sprint. Se registran **No medido** y se solicita al equipo confirmar disponibilidad antes del siguiente compromiso. Capacidad futura = suma de horas disponibles confirmadas por integrante menos ceremonias y ausencias confirmadas. No se deriva capacidad de tener cinco integrantes ni de los 109 tests. Las tareas de 4-8 h son estimaciones de planificación, no registros de ejecución.

#### 5.2.1.2 Sprint Planning por incremento

"""
sprint1 = {'US-01','US-02','US-03','US-04A','US-04B','US-05','US-06','US-10A','US-10B','US-16A','US-16B'}
sprint2 = {r[1] for r in functional} - sprint1
plans = [
 (1,"Base integrada web y API",[r for r in functional if r[1] in sprint1],"Reconstrucción histórica; implementación disponible, sin acta de compromiso original", "Integrar contratos IAM, espacios, dispositivos, energía y planes; conectar CTA y login; comprobar autorización y consultas con datos controlados.","Backend/Angular/Landing y suites actuales. No acredita pruebas históricas de cada sprint.","Confirmar cobertura por historia en UI; el pago sigue siendo académico."),
 (2,"Experiencia móvil y automatización conectadas",[r for r in functional if r[1] in sprint2],"Reconstrucción histórica; funcionalidad disponible, aceptación móvil física abierta", "Conectar grupos, rutinas, modos, alertas, metas y soporte con sedes/dispositivos; conservar permisos e idiomas en Flutter.","Código Flutter, matriz de paridad y CI Android/iOS; no publicación en tienda.","NF-05/NF-06 no se cierran con un build de simulador."),
 (3,"Evidencia de AV1 y trazabilidad técnica",[],"Reconstrucción histórica; artefactos y automatización disponibles", "Mantener reportes, OpenAPI, capturas, fuentes y guías; mapear pruebas a reglas y endpoints; conservar autoría real.","Reportes AV1, 109 tests y workflows. Las historias TECH/NF se formalizan ahora, sin atribuirles fecha retroactiva.","TECH-01/02 y NF-01/02 verificados en su alcance; TECH-03 requiere revisión cruzada."),
 (4,"Revisión TB1 y respuesta a observaciones",[],"Revisión del Sprint Planning registrado; sin inventar una nueva reunión", "Completar criterios medibles, tipos NF/TECH/SPIKE, ERD visible y trazabilidad a evidencias y tablero.","README, fuentes PlantUML, SVG, PDF y validadores.","Revisiones individuales ET-06 a ET-10 no se consideran hechas por tener CI verde."),
 (5,"Preparar medición reproducible",[r for r in future if r[1] in {'TS-01','TS-02A','TS-02B','TS-03','US-19'}],"Propuesto / Por iniciar", "Definir variantes y consentimiento; validar contratos de eventos web/móvil sin PII; versionar dataset reiniciable.","Esquemas, tests de eventos y dataset; aún no existen resultados del piloto.","SPIKE-02 antes de compromiso; sin horas disponibles ni equipo asignado confirmados."),
 (6,"Implementar tratamientos seguros",[r for r in future if r[1] in {'US-17A','US-17B','US-18','US-21'}],"Propuesto / Por iniciar", "Integrar recomendación en Energy Monitoring; delegar acciones a Device Control; mostrar alcance y frescura.","Tests de mapper/componente, feature flag y smoke web/Android por generar.","Depende de Sprint 5 y NF-03/04; no afirmar mejora porcentual sin experimento."),
 (7,"Recuperación y piloto experimental",[r for r in future if r[1] in {'US-20A','US-20B','TS-04','TS-05'}],"Propuesto / Por iniciar", "Probar reintentos idempotentes; ejecutar protocolo consentido; anonimizar resultados, analizar y registrar decisiones.","Dataset y análisis por generar; no hay muestra reclutada o resultados medidos.","Depende de Sprints 5-6, NF-05/06, distribución móvil y disponibilidad de participantes."),
]
metrics += table(["Sprint", "Objetivo", "Historias / estimación", "Estado y salida"], [(str(n),goal, ', '.join(r[1] for r in items)+f' / {sum(int(r[4]) for r in items)} SP' if items else ('TECH-01/02/03, NF-01/02: 17 SP formalizados' if n==3 else 'ET-01 a ET-10 / 52 h estimadas'),state+'. '+evidence) for n,goal,items,state,task,evidence,risk in plans])
metrics += "\n\n#### 5.2.1.3 Control del Sprint 4 y colaboración\n\n"
metrics += "Se conservan las diez tareas ET del Sprint 4 y sus estimaciones originales (52 h). ET-01/02/03/05 tienen artefactos existentes; ET-04 incorpora ahora el refinamiento solicitado. ET-06 (Jean), ET-07 (Jairo), ET-08 (Brayan), ET-09 (Renzo) y ET-10 (todos) mantienen responsables **propuestos**, no desempeño confirmado. La ejecución automática de suites no acredita que Jairo haya realizado una revisión individual. Las horas reales, revisiones firmadas y aceptación de responsables siguen **No registradas**. El detalle y condición de cierre de cada tarea se conservan en el anexo de planificación.\n\n"
metrics += "#### 5.2.1.4 Definition of Ready, Done y actualización del tablero\n\n"
metrics += "**Ready:** problema, tipo, alcance, criterio medible, dependencia, estimación <= 5 SP y responsable que acepta la tarea; spikes con pregunta, 4 h y salida definida. **Done:** criterios aprobados en el entorno declarado, tests y artefacto accesibles, revisión identificada, SHA y enlace de evidencia. Un build no demuestra instalación física ni un porcentaje de ahorro. Una tarjeta sin evidencia de aceptación queda en Implementado / Por verificar, aunque el código exista.\n\n"
metrics += "El tablero se creará como **EnergyCore - Product Backlog y Sprint Planning**. Listas: Backlog; Por iniciar; En curso; Implementado - por verificar; Verificado - pruebas y CI. Etiquetas: Funcional, No funcional, Técnica, Spike, Experimento y Sprint. No se crean responsables, fechas límite o actividad pasada ficticios. La sincronización requiere sesión de Trello y se registrará mediante ID de tablero/tarjeta y lectura posterior; los JSON/CSV locales no se presentan como un tablero ya publicado.\n\n"
old = section(report,'### 5.2.1 Sprint Backlogs','### 5.2.2 Implemented Landing Page Evidence')
(planning_dir/'sprint-4-source-before-refinement.md').write_text(('# Registro anterior conservado\n\n### 5.2.1 Sprint Backlogs'+old).rstrip()+'\n',encoding='utf-8')
report=report.replace('### 5.2.1 Sprint Backlogs'+old,metrics,1)

future_summary = table(['Sprint','Objetivo','Historias','Estimación / estado'],[(str(n),goal,', '.join(r[1] for r in items),f'{sum(int(r[4]) for r in items)} SP / Por iniciar') for n,goal,items,state,task,evidence,risk in plans if n>=5])
start='#### 8.3.3.1 To Be Sprint Backlogs'
end='#### 8.3.3.2 Implemented To Be Landing Page Evidence'
old=section(report,start,end)
report=report.replace(start+old,start+'\n\nLa secuencia continúa después del Sprint 4 TB1. Estos son planes futuros, no incrementos aceptados.\n\n'+future_summary+'\n\nSPIKE-02 precede el Sprint 5. SPIKE-01 y SPIKE-03 habilitan NF-03 y la demostración móvil antes del piloto. La suma To-Be sigue siendo 53 SP; no incluye 12 h de investigación ni suma de nuevo las historias de calidad relacionadas. Ver el [detalle de planificación](planning/sprint-planning.md) para tareas, responsables propuestos, horas, dependencias y cierre.\n\n',1)
version='| TB1.3 | 20/10/2026 | Equipo Teralume | Refinamiento de Sprint Planning, criterios cuantitativos y backlog no funcional, técnico y de investigación; estados vinculados a evidencia y preparación del tablero Trello. |\n'
pos=report.index('\n',report.index('| TB1.2'))+1
report=report[:pos]+version+report[pos:]
report_path.write_text(report,encoding='utf-8')

detail='# Sprint Planning detallados - EnergyCore\n\nActualizado: **20/10/2026**.\n\n'+metrics.split('#### 5.2.1.1',1)[1].split('#### 5.2.1.2',1)[0]
detail += '\n## Reglas de trazabilidad\n\nSprints 1-3: reconstrucción desde artefactos, no actas contemporáneas. Sprint 4: revisión del registro TB1. Sprints 5-7: propuesta futura. Fecha de reunión, inicio/fin, asistentes y capacidad histórica: No registrados. No se fabrican burn-down, velocidad, horas reales o porcentajes de avance. Responsable técnico histórico documentado: Jean Loa; otros apoyos se limitan a evidencia registrada. Los responsables de tareas futuras deben aceptar su asignación en Trello.\n\n'
cards=[]
for n,goal,items,state,task,evidence,risk in plans:
    detail += f'## Sprint {n}: {goal}\n\n**Naturaleza:** {state}.\n\n**Objetivo:** {goal}.\n\n**Entrada:** '+('Artefactos y commits existentes; sin planificación original verificable.' if n<5 else 'Ready completo y disponibilidad confirmada por el equipo; sin compromiso de fechas aún.')+'\n\n'
    if items:
        detail+=table(['ID','Título','SP','Responsable','Estado'],[(r[1],r[2],r[4],'Jean (implementación documentada)' if n<3 else 'Por asignar','Implementado; verificar alcance' if n<3 else 'Por iniciar') for r in items])+'\n\n'
    detail+=f'**Estimación:** {sum(int(r[4]) for r in items)} SP del bloque funcional/experimental.' if items else ('**Estimación formalizada:** 17 SP de calidad/habilitadores, sin contabilizarlos como velocidad histórica.' if n==3 else '**Estimación heredada:** 52 h / 10 tareas ET; tiempos reales no registrados.')
    detail+=f'\n\n**Trabajo integrado:** {task}\n\n**Salida/evidencia:** {evidence}\n\n**Dependencias y riesgos:** {risk}\n\n**Capacidad:** No medida históricamente / por confirmar para compromisos futuros.\n\n'
    if n in (1,2,5,6,7):
        tasks=[]
        for r in items:
            # Work packages are proposed for reproducibility; not a fabricated timesheet.
            tasks.extend([(r[1]+'-A','Revisar contrato, alcance y criterio de '+r[2],4),(r[1]+'-B','Integrar implementación y prueba de '+r[2],8 if int(r[4])==5 else 4)])
        detail+='**Desglose de referencia:** paquetes propuestos, no horas ejecutadas; dos tareas por historia. El equipo debe dividir nuevamente si una tarea excede 8 h al refinar.\n\n'
        detail+=table(['Tarea','Descripción','h estimadas','Responsable','Condición de cierre'],[(a,b,c,'Por asignar','Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva') for a,b,c in tasks])+'\n\n'
        detail+=f'Total de referencia: **{sum(t[2] for t in tasks)} h**, sin evidencia de capacidad para comprometer ese total. No implica duración del sprint ni aceptación del equipo.\n\n'
    if n==4:
        detail+='El registro de tareas original se conserva en [fuente del Sprint 4](sprint-4-source-before-refinement.md). Su estado To do se conserva como Por verificar hasta evidencia individual; el refinamiento actual cierra el documento de ET-04, no una ceremonia histórica.\n\n'

for r in functional:
    cards.append(dict(id=r[1],title=r[2],type='Funcional',sp=int(r[4]),sprint=1 if r[1] in sprint1 else 2,status='Implementado - por verificar',description='Implementación registrada en Product Backlog. No implica aceptación UI end-to-end de todos los criterios. Ver README §3.2, código del contexto y suite correspondiente.',owner=None))
for x in quality+technical:
    status='Verificado - pruebas y CI' if x[3].startswith('Verificado') else ('Implementado - por verificar' if x[3] in {'Parcial','Implementado; revisión abierta'} else 'Por iniciar')
    cards.append(dict(id=x[0],title=x[1],type='No funcional' if x[0].startswith('NF') else 'Técnica',sp=x[2],sprint=3 if status.startswith('Verificado') else None,status=status,description=x[4]+'\n\nAceptación: '+x[5]+'\n\nEvidencia/limitación: '+x[6],owner=None))
for x in spikes:
    cards.append(dict(id=x[0],title=x[1],type='Spike',sp=None,timebox_hours=4,sprint=None,status='Por iniciar',description='Pregunta: '+x[3]+'\n\nDependencias: '+x[2]+'\n\nSalida: '+x[4],owner=None))
for r in future:
    spn=next(n for n,_,items,*_ in plans if n>=5 and r[1] in {t[1] for t in items})
    cards.append(dict(id=r[1],title=r[2],type='Experimento',sp=int(r[4]),sprint=spn,status='Backlog',description='Trabajo To-Be. No implementado/verificado como tratamiento experimental.\n\nCriterio de salida: '+r[5],owner=None))
assert len(cards)==47 and len({c['id'] for c in cards})==47
(planning_dir/'sprint-planning.md').write_text(detail,encoding='utf-8')
payload=dict(updated_at='2026-10-20',board_name='EnergyCore - Product Backlog y Sprint Planning',sync_status='NOT_SYNCED_AUTH_REQUIRED',board_url=None,cards=cards)
(planning_dir/'trello-cards.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (planning_dir/'trello-cards.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','title','type','sp','timebox_hours','sprint','status','description','owner'],extrasaction='ignore');w.writeheader();w.writerows(cards)
print(json.dumps(dict(functional_stories=len(functional),functional_sp=95,new_nf_sp=18,new_technical_sp=16,spikes=3,spike_timebox_hours=12,to_be_sp=53,trello_cards=len(cards)),indent=2))
