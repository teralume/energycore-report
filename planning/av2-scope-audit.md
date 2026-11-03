# Auditoría de alcance AV2 - actualización del 03/11/2026

Fuente normativa: `../Enunciado.pdf`, tercer hito, páginas físicas/impresas 42-43. La estructura de TB2 aparece en la página física 44 (rotulada 43/53). Inspeccionada la página 43 renderizada para confirmar el límite.

Fuente de calificación vigente: [actividad S12 AV2 y su rúbrica](https://aulavirtual.upc.edu.pe/ultra/courses/_554468_1/assessment/_74454492_1/overview?courseId=_554468_1), consultada directamente en Aula Virtual el 03/11/2026. Vence el 09/11/2026 a las 09:00 (UTC-5). La rúbrica asigna 4 puntos a verificación/validación, 4 a DevOps, 2.5 a planificación experimental, 2.5 a diseño, 2 a Product y Sprint Backlogs To-Be, 2 a mejora continua y 3 a comunicación.

## Decisión aplicada

AV2 conserva los capítulos previos corregidos y desarrolla VI (6.1-6.4), VII (7.1-7.4), VIII (8.1, 8.2, 8.3.1 y 8.3.2), registro de versiones, Student Outcome, conclusiones en avance, bibliografía y anexos. El PDF TB1 anterior y su ZIP se conservan sin regenerar.

**Corrección basada en la rúbrica viva:** AV2 sí exige To-Be Sprint Backlogs con historias descompuestas en Engineering Tasks estimadas de 4 a 8 h. Se incluyen como planificación dentro de 8.3.2 y en `planning/sprint-planning-av2.md`: 13 historias, 53 SP, 26 tareas y 132 h estimadas. Sus estados y responsables siguen por confirmar; no se declara ejecución. También se incorpora la comparación de alternativas DevOps exigida por el criterio de herramientas y pipeline, fundamentada con documentación oficial.

**Discrepancia resuelta para la planificación:** los objetivos de AV2 en p. 42 mencionan resultados y ejecución, pero el índice de p. 43 termina en 8.3.2; TB2 enumera 8.3.3-8.6. El 21/10 se había excluido también el Sprint Backlog To-Be. La rúbrica publicada permite corregir esa exclusión: se incorpora el plan y se mantiene fuera la evidencia de implementación, ejecución y resultados no realizados. No se usa el corte numérico del índice para omitir un criterio explícito de evaluación.

## Contenido excluido del documento AV2

- Implementación To-Be y colaboración de 8.3.3 presentadas como ejecución. La planificación de sus Sprint Backlogs sí se incluye por la rúbrica.
- 8.3.4 y entrevistas To-Be.
- 8.4, análisis de resultados y Question Backlog repriorizado.
- 8.5, shareback y aprendizaje continuo.
- 8.6, pre-launch, nuevo video promocional y GEES.
- Secciones adelantadas de Video App Validation y About the Team sin grabación.
- Ejecución de los sprints experimentales 5-7 presentada como realizada; su planificación se desarrolla en 8.3.2.

Los criterios de calidad, historias técnicas/spikes del producto base y el To-Be Product Backlog se mantienen: no son resultados experimentales ni evidencia de ejecución. La selección de métodos, medidas y tamaño de muestra pertenece a 8.2 y sí se exige en AV2.

## Brechas de evidencia que no se cierran con esta corrección

| Requisito de AV2 | Evidencia actual | Conclusión |
|:--|:--|:--|
| 6.1 Tests | 109 casos históricos y CI; varios recorridos de sistema solo descritos | No equivale a todos los flujos E2E aceptados |
| 6.2 Análisis estático y reviews | Inspección automática por commit y CI consultado, tres observaciones registradas | No equivale a revisión humana por pares |
| 6.3 Entrevistas de validación | Un antecedente de needfinding; sin registro de validación de uso | No contar la entrevista de 2.2 como sesión de 6.3 |
| 6.4 Auditoría realizada/recibida | Protocolo y cronograma relativo; sin grupo externo, acta y devolución verificables | No presentarla como realizada |
| 7.4 Monitoring/alerting/notifications | Activación PASS del 21/10 y monitor activo; comprobación del 03/11: web 200, API/OpenAPI 503 por facturación cerrada | Incidente abierto; no ocultar el fallo ni afirmar disponibilidad actual de la API |
| 8.1-8.2 | Preguntas, hipótesis, medidas y diseño propuestos | No afirmar reclutamiento o resultado experimental |
| 8.3.1-8.3.2 | Historias To-Be, backlog de 53 SP y 26 tareas de Sprint Backlog con 132 h estimadas | Planificación requerida por la rúbrica; no incremento experimental implementado |
| Student Outcome | Antecedentes AV1/TB1 | No inventar testimonios o aportes AV2 individuales |
| Archivos de AV2 | Reporte y presentación adaptados al alcance | Performance y exposición AV2 requieren su evidencia propia; no renombrar los de TB1 |

Esta auditoría es un documento interno de revisión. No se incluye en el PDF académico ni se usa para afirmar entrega AV2 completa.
