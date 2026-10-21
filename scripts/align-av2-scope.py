"""Apply the AV2 enumerated structure (assignment pp. 42-43), preserving TB1 exports."""
from pathlib import Path
import re
import json

root=Path(__file__).resolve().parents[1]
path=root/'README.md'
text=path.read_text(encoding='utf-8')
if '# Informe de Avance 2' in text:
    raise SystemExit('AV2 scope already applied; edit the current version rather than reapplying.')

# The final increment remains recoverable in Git and the existing TB1 PDF/ZIP.
start=text.index('### 8.3.3 Pipeline Supported')
end=text.index('# Conclusiones',start)
excluded=text[start:end]
text=text[:start]+text[end:]
start=text.index('# Video App Validation')
end=text.index('# Bibliografía',start)
text=text[:start]+text[end:]
text=text.replace('# Informe de Trabajo Parcial','# Informe de Avance 2',1)
text=text.replace('## Inventario de artefactos acumulativos para TB1','## Inventario acumulativo de antecedentes y alcance AV2',1)
text=text.replace('## 5.3 Video About the Product','## 5.3 Video About the Product',1)
version='| AV2.1 | 21/10/2026 | Equipo Teralume | Ajuste del alcance al índice del tercer hito: capítulos VI y VII completos, y VIII hasta 8.3.2; exclusión de contenidos de TB2 y corrección de la procedencia de entrevistas. |\n'
at=text.index('\n',text.index('| TB1.3'))+1
text=text[:at]+version+text[at:]

scope='''## Alcance de Avance 2

El documento conserva los capítulos previos como antecedentes corregidos del proyecto acumulativo. El incremento de AV2 sigue la estructura enumerada del tercer hito del Enunciado, páginas 42-43: capítulo VI (6.1-6.4), capítulo VII (7.1-7.4) y capítulo VIII desde 8.1 hasta **8.3.2 To-Be Product Backlog**, además del registro de versiones, Student Outcome, avance de conclusiones, bibliografía y anexos.

Las estimaciones, umbrales de calidad y tamaños de muestra de 8.1-8.2 son propuestas de diseño. No constituyen resultados observados, participantes reclutados ni validación ejecutada. Los enlaces audiovisuales conservados de AV1/TB1 son antecedentes identificados con su entrega de origen; no se presentan como una exposición nueva de AV2.

'''
text=text.replace('## Project Report Collaboration Insights',scope+'## Project Report Collaboration Insights',1)

# Restrict the earlier planning summary to completed increments; experimentation backlog stays in VIII.
lines=[]
for line in text.splitlines():
    if re.match(r'^\| [567] \|',line) and ('SP / Por iniciar' in line or 'Propuesto / Por iniciar' in line):
        continue
    lines.append(line)
text='\n'.join(lines)+'\n'
text=text.replace('El ciclo experimental continúa en Sprints 5-7; se evita el doble Sprint 4 que existía entre los capítulos V y VIII.',
                  'Esta versión incluye los planes de los incrementos 1-4; el trabajo experimental se presenta en AV2 como historias y Product Backlog, sin desarrollar su ejecución.')
text=text.replace('[Sprint Planning detallados](planning/sprint-planning.md)',
                  '[Sprint Planning de antecedentes AV2](planning/sprint-planning-av2.md)')
text=text.replace('El siguiente registro distingue reconstrucción histórica, revisión documental y trabajo por ejecutar.',
                  'El siguiente registro distingue reconstrucción histórica y revisión documental.')
text=text.replace('No existen registros verificables de disponibilidad personal, horas reales, fechas de las reuniones o velocidad por sprint.',
                  'No existen registros verificables de disponibilidad personal, horas reales, fechas de las reuniones o velocidad por sprint.')

old='El diseño utiliza los guiones definidos en 2.2.1 para contrastar hogares y pequeños negocios. La muestra prevista es de seis participantes: tres por segmento. Hasta ahora existe una entrevista real del segmento pequeño negocio; faltan cinco sesiones para completar la muestra. No se redactan respuestas, participantes ni consentimientos ficticios.'
new='La validación requiere sesiones con personas de los dos segmentos que interactúen con el producto y permitan evaluar tareas y heurísticas. Se propone una muestra de seis participantes, tres por segmento; aún no se aportan registros de estas sesiones. El guion de needfinding de 2.2.1 es un antecedente de investigación, no sustituye un guion de validación de uso. La planificación no se presenta como validación ejecutada.'
assert old in text
text=text.replace(old,new,1)
old='La entrevista realizada por Jairo Mathias Santiago Atanacio y su análisis se encuentran en 2.2.2 y 2.2.3. Los cinco enlaces audiovisuales restantes y la síntesis comparativa se incorporarán únicamente después de realizar las sesiones reales.'
new='La entrevista de Jairo Mathias Santiago Atanacio documentada en 2.2.2 y 2.2.3 corresponde a needfinding. No se contabiliza como entrevista de validación ni demuestra interacción con las tareas del producto. Esta sección no cuenta aún con sesiones de validación, consentimientos ni enlaces audiovisuales verificables.'
assert old in text
text=text.replace(old,new,1)
text=text.replace('| 4 | Suite completa | Eliminar el filtro temporal, ejecutar los 60 escenarios y obtener cero fallos. |\n','')
text=text.replace('La hipótesis principal se ha convertido en un experimento reproducible:',
                  'La hipótesis principal cuenta con un diseño experimental propuesto:')
text=text.replace('Se recomienda implementar los workflows de CI, migraciones de base de datos, instrumentación anonimizada, observabilidad y rollback antes de automatizar producción.',
                  'Los workflows de CI existentes aportan evidencia técnica. Aún se requieren pruebas de cierre para las capacidades solo descritas y completar la validación con usuarios y el intercambio de auditorías exigidos por AV2.')
text=text.replace('- dataset anonimizado, análisis y decision log del piloto experimental;\n','')
text=text.replace('- URLs de Video App Validation y About-the-Team después de su grabación;\n','- exposición de AV2 con contenido y participantes correspondientes a esta entrega;\n')
text=text.replace('- testimonios de los integrantes vinculados con responsabilidades sustanciales del proyecto.',
                  '- actualización individual de Student Outcome, sustentada en contribuciones verificables.')

# Regenerate the contents so excluded future sections do not survive as dangling headings.
toc_start=text.index('## Contenido')
toc_end=text.index('## Student Outcome',toc_start)
body=text[toc_end:]
toc=['## Contenido','']
for level,title in re.findall(r'^(#{1,4}) (.+)$',body,re.M):
    slug=re.sub(r'[^\w\s-]','',title.lower()).replace(' ','-')
    toc.append('  '*max(0,len(level)-1)+f'- [{title}](#{slug})')
text=text[:toc_start]+'\n'.join(toc)+'\n\n'+text[toc_end:]

assert not re.search(r'^#{1,6} 8\.(?:3\.[3-9]|[4-9])\b',text,re.M)
assert '### 8.3.2 To Be Product Backlog' in text
path.write_text(text,encoding='utf-8')

planning=(root/'planning/sprint-planning.md').read_text(encoding='utf-8')
planning=planning.split('## Sprint 5:',1)[0].rstrip()+'\n'
planning=planning.replace('# Sprint Planning detallados - EnergyCore','# Sprint Planning de antecedentes - AV2',1)
planning=planning.replace('Sprints 5-7: propuesta futura. ','')
planning+='\n## Tablero de seguimiento\n\n[EnergyCore en Trello](https://trello.com/b/kFru7uh2/energycore-product-backlog-y-sprint-planning). Los planes mostrados en este documento corresponden a los incrementos 1-4. Las tarjetas futuras del tablero no constituyen evidencia de ejecución ni se desarrollan como nuevos Sprint Backlogs experimentales en esta entrega.\n'
(root/'planning/sprint-planning-av2.md').write_text(planning,encoding='utf-8')

audit='''# Auditoría de alcance AV2 - 21/10/2026

Fuente normativa: `../Enunciado.pdf`, tercer hito, páginas físicas/impresas 42-43. La estructura de TB2 aparece en la página física 44 (rotulada 43/53). Inspeccionada la página 43 renderizada para confirmar el límite.

## Decisión aplicada

AV2 conserva los capítulos previos corregidos y desarrolla VI (6.1-6.4), VII (7.1-7.4), VIII (8.1, 8.2, 8.3.1 y 8.3.2), registro de versiones, Student Outcome, conclusiones en avance, bibliografía y anexos. El PDF TB1 anterior y su ZIP se conservan sin regenerar.

**Discrepancia del enunciado:** los objetivos de AV2 en p. 42 mencionan resultados, aprendizaje continuo y ejecución de experimentos, mientras que su estructura detallada en p. 43 termina en 8.3.2. La estructura de TB2 en p. 44 enumera 8.3.3-8.6. Ante la observación del profesor sobre adelantar contenido, se adopta el límite detallado de 8.3.2. Es una decisión conservadora basada en esa observación, no la afirmación de que el PDF sea inequívoco. No se elimina trabajo del repositorio ni del tablero; se excluye del documento entregable de AV2.

## Contenido excluido del documento AV2

- 8.3.3 y sus Sprint Backlogs, implementación To-Be y colaboración.
- 8.3.4 y entrevistas To-Be.
- 8.4, análisis de resultados y Question Backlog repriorizado.
- 8.5, shareback y aprendizaje continuo.
- 8.6, pre-launch, nuevo video promocional y GEES.
- Secciones adelantadas de Video App Validation y About the Team sin grabación.
- Desarrollo de planes de ejecución experimental 5-7 dentro del resumen 5.2.1.

Los criterios de calidad, historias técnicas/spikes del producto base y el To-Be Product Backlog se mantienen: no son resultados experimentales ni evidencia de ejecución. La selección de métodos, medidas y tamaño de muestra pertenece a 8.2 y sí se exige en AV2.

## Brechas de evidencia que no se cierran con esta corrección

| Requisito de AV2 | Evidencia actual | Conclusión |
|:--|:--|:--|
| 6.1 Tests | 109 casos históricos y CI; varios recorridos de sistema solo descritos | No equivale a todos los flujos E2E aceptados |
| 6.2 Análisis estático y reviews | Comandos, políticas y CI; falta revisión individual identificable para algunos cierres | Conservar alcance y fecha de cada comprobación |
| 6.3 Entrevistas de validación | Un antecedente de needfinding; sin registro de validación de uso | No contar la entrevista de 2.2 como sesión de 6.3 |
| 6.4 Auditoría realizada/recibida | Protocolo y cronograma relativo; sin grupo externo, acta y devolución verificables | No presentarla como realizada |
| 7.4 Monitoring/alerting/notifications | Diseño y umbrales objetivo | No atribuir disponibilidad, latencia o alertas operativas medidas |
| 8.1-8.2 | Preguntas, hipótesis, medidas y diseño propuestos | No afirmar reclutamiento o resultado experimental |
| 8.3.1-8.3.2 | Historias To-Be y backlog de 53 SP | Estimación, no incremento experimental implementado |
| Student Outcome | Antecedentes AV1/TB1 | No inventar testimonios o aportes AV2 individuales |
| Archivos de AV2 | Reporte corregido como borrador de alcance | Keynote, performance y exposición AV2 deben corresponder a este hito; no renombrar los de TB1 para declararlos nuevos |

Esta auditoría es un documento interno de revisión. No se incluye en el PDF académico ni se usa para afirmar entrega AV2 completa.
'''
(root/'planning/av2-scope-audit.md').write_text(audit,encoding='utf-8')
print(json.dumps({'stage':'AV2','last_experimental_heading':'8.3.2','removed_future_lines':len(excluded.splitlines()),'historical_planning_sprints':[1,2,3,4],'delivery_status':'SCOPE_CORRECTED_EVIDENCE_GAPS_OPEN'},indent=2))
