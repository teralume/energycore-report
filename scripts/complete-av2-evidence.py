"""Update the AV2 report with actual evidence; leave interviews and external attestations alone."""
from pathlib import Path
import json
import re

root=Path(__file__).resolve().parents[1]
file=root/'README.md'
text=file.read_text(encoding='utf-8')
assert 'AV2.2 |' not in text, 'Already applied'
text=text.replace('| AV2.1 | 21/10/2026 | Equipo Teralume | Ajuste del alcance al índice del tercer hito: capítulos VI y VII completos, y VIII hasta 8.3.2; exclusión de contenidos de TB2 y corrección de la procedencia de entrevistas. |',
'''| AV2.1 | 21/10/2026 | Equipo Teralume | Ajuste del alcance al índice del tercer hito: secciones VI y VII, y VIII hasta 8.3.2; exclusión de contenidos de TB2 y corrección de la procedencia de entrevistas. |
| AV2.2 | 21/10/2026 | Loa Rojas, Jean Franck | Incorporación de inspección técnica trazable, comprobación pública de disponibilidad, monitor y workflow preparados, kit de auditoría externa y presentación AV2; sin atribuir entrevistas ni auditorías no realizadas. |''')

review=json.loads((root/'assets/evidence/implemented/av2-review-2026-10-21.json').read_text())
rows='\n'.join(f"| `{r['repository']}` | `{r['local_head'][:7]}` | [success]({r['latest_remote_run'][0]['url']}) |" for r in review['repositories'])
reviewblock='''
**Inspección técnica del 21/10/2026.** Se contrastaron los HEAD locales con la última ejecución remota disponible y se inspeccionó la configuración del backend. Los cinco HEAD coinciden con el commit de CI consultado; el reporte contiene además cambios AV2 locales todavía no publicados. Esta inspección automatizada no equivale a aprobación humana por pares ni a una nueva ejecución completa de los tests.

| Repositorio | Commit base inspeccionado | Última ejecución consultada |
|:--|:--|:--|
'''+rows+'''

| Registro | Observación comprobada | Decisión |
|:--|:--|:--|
| REV-01 | `application-prod.properties` conserva `spring.jpa.hibernate.ddl-auto=update`. | Riesgo abierto: adoptar y verificar migraciones versionadas antes de cambiar el esquema productivo. |
| REV-02 | `HealthController` expone `/health` y `/api/v1/health`. | El monitor utiliza `/api/v1/health`; no se considera público `/actuator/health`. |
| REV-03 | El valor predeterminado de CORS productivo incluye `localhost:4200`. | Revisar la configuración efectiva por entorno antes de retirar orígenes; no se afirma una vulnerabilidad explotada. |

**Registro reproducible:** [inspección de repositorios y CI](assets/evidence/implemented/av2-review-2026-10-21.json), generada con `scripts/collect-av2-review.py`.

'''
text=text.replace('## 6.3 Validation Interviews',reviewblock+'## 6.3 Validation Interviews')
text=text.replace('El paquete de auditoría está compuesto por:', 'El [kit de intercambio de auditorías UX](planning/ux-audit-kit-av2.md) define tres tareas, precondiciones, criterios de éxito, restricciones de seguridad, ficha de hallazgos y acta. Es un instrumento preparado, no una auditoría externa ejecutada. El paquete previsto está compuesto por:')
text=text.replace('**Estado:** actividad programada para la asignación de grupos del curso.', '**Alcance acreditable:** instrumento preparado; no se dispone de grupo auditado confirmado, acta ni hallazgos externos verificables.')
text=text.replace('**Estado:** actividad programada para el intercambio de auditorías.', '**Alcance acreditable:** instrumento preparado; no se ha aportado informe de otro grupo ni acta de devolución.')
monitor=json.loads((root/'assets/evidence/implemented/av2-monitoring-2026-10-21.json').read_text())
assert monitor['passed']
measure='\n'.join(f"| {c['name']} | HTTP {c['http_status']} | {c['elapsed_ms']} ms | PASS |" for c in monitor['checks'])
block='''
**Comprobación pública ejecutada el 21/10/2026:** [`monitor-public-surfaces.py`](scripts/monitor-public-surfaces.py) realizó solicitudes GET sin autenticación ni mutaciones. Conservó estado HTTP, duración y decisión del validador, sin almacenar cuerpos de respuesta, credenciales o datos personales.

| Superficie | Estado | Duración de esta solicitud | Resultado |
|:--|:--|--:|:--:|
'''+measure+'''

**Evidencia:** [resultado JSON](assets/evidence/implemented/av2-monitoring-2026-10-21.json). Las duraciones son observaciones puntuales: no son percentiles, SLA, tiempo de tarea del usuario ni mediciones físicas de energía.

El workflow [`monitoring.yml`](.github/workflows/monitoring.yml) está preparado para ejecución manual, cambios del monitor y una programación de seis horas. Primero prueba las reglas de detección; después verifica salud (`status=UP`), un contrato OpenAPI no vacío y HTML de la Web Application. Un error devuelve código de salida distinto de cero, marca el job como fallido y conserva el JSON como artefacto durante 30 días. Las tres pruebas locales del monitor pasaron; son adicionales a las 109 pruebas históricas del producto.

La programación remota entra en funcionamiento al publicar el workflow en la rama predeterminada; no se presenta como ya activada ni como historial de disponibilidad. El resumen de Actions sirve como canal de diagnóstico; los avisos por correo dependen de las preferencias reales de suscripción de cada usuario, sin configurar ni enviar correo desde este script.

'''
text=text.replace('### 7.4.2 Monitoring Pipeline Components',block+'### 7.4.2 Monitoring Pipeline Components')
text=text.replace('Cada despliegue añade versión, entorno y correlation ID a los registros.', 'Se propone que cada despliegue añada versión, entorno y correlation ID a los registros; la comprobación sintética actual conserva únicamente la ejecución y la URL pública.')
text=text.replace('Los umbrales son iniciales y se ajustarán después de observar una línea base.', 'Los umbrales de esta tabla son propuestas y no políticas cloud configuradas. El monitor sintético actual detecta una respuesta fallida por ejecución; aún no acumula tres fallos consecutivos ni calcula percentiles. Los umbrales se ajustarán después de observar una línea base.')
text=text.replace('En conjunto se ejecutaron **109 pruebas automatizadas sin falllos**.', 'En conjunto se ejecutaron **109 pruebas automatizadas sin fallos**.')
text=text.replace('En conjunto se ejecutaron **109 pruebas automatizadas sin fallos**.', 'La línea base del 05/10/2026 registra **109 pruebas automatizadas sin fallos**; el 21/10/2026 se consultó su CI, sin repetir toda esa suite.')
text=text.replace('También deben incorporarse evidencias audiovisuales, auditoría entre grupos y resultados de experimentación cuando existan.', 'El monitoreo sintético ya cuenta con una comprobación pública y un workflow preparado; faltan su ejecución remota sostenida, la revisión humana por pares y los informes de auditoría entre grupos. No se requieren resultados experimentales adelantados de TB2 en este documento de AV2.')
text=text.replace('## Enlaces importantes', '''## Evidencias nuevas de AV2

- [Revisión técnica y CI por commit](assets/evidence/implemented/av2-review-2026-10-21.json).
- [Comprobación pública de disponibilidad](assets/evidence/implemented/av2-monitoring-2026-10-21.json).
- [Kit para auditorías UX entre grupos](planning/ux-audit-kit-av2.md).
- [Presentación AV2 editable](output/keynote/upc-pre-202610-1asi0732-9100-teralume-keynote-av2.pptx).
- [Presentación AV2 en PDF](output/keynote/upc-pre-202610-1asi0732-9100-teralume-keynote-av2.pdf).

## Enlaces importantes''')
toc_start=text.index('## Contenido')
toc_end=text.index('## Student Outcome',toc_start)
toc=['## Contenido','']
for level,title in re.findall(r'^(#{1,6}) (.+)$',text[toc_end:],re.M):
    slug=re.sub(r'[^\w\s-]','',title.lower()).replace(' ','-')
    toc.append('  '*max(0,len(level)-1)+f'- [{title}](#{slug})')
text=text[:toc_start]+'\n'.join(toc)+'\n\n'+text[toc_end:]
file.write_text(text,encoding='utf-8')
audit=root/'planning/av2-scope-audit.md'
a=audit.read_text(encoding='utf-8').replace('| 7.4 Monitoring/alerting/notifications | Diseño y umbrales objetivo | No atribuir disponibilidad, latencia o alertas operativas medidas |','| 7.4 Monitoring/alerting/notifications | Comprobación pública PASS, tres pruebas del monitor y workflow preparado | Falta activar el workflow remoto y observar historial; sin SLA ni percentiles medidos |').replace('| 6.2 Análisis estático y reviews | Comandos, políticas y CI; falta revisión individual identificable para algunos cierres | Conservar alcance y fecha de cada comprobación |','| 6.2 Análisis estático y reviews | Inspección automática por commit y CI consultado, tres observaciones registradas | No equivale a revisión humana por pares |').replace('| Archivos de AV2 | Reporte corregido como borrador de alcance | Keynote, performance y exposición AV2 deben corresponder a este hito; no renombrar los de TB1 para declararlos nuevos |','| Archivos de AV2 | Reporte y presentación adaptados al alcance | Performance y exposición AV2 requieren su evidencia propia; no renombrar los de TB1 |')
audit.write_text(a,encoding='utf-8')
print('Updated AV2 evidence without modifying section 6.3 or attributing external audits.')
