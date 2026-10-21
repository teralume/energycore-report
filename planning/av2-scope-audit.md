# Auditoría de alcance AV2 - 21/10/2026

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
| 6.2 Análisis estático y reviews | Inspección automática por commit y CI consultado, tres observaciones registradas | No equivale a revisión humana por pares |
| 6.3 Entrevistas de validación | Un antecedente de needfinding; sin registro de validación de uso | No contar la entrevista de 2.2 como sesión de 6.3 |
| 6.4 Auditoría realizada/recibida | Protocolo y cronograma relativo; sin grupo externo, acta y devolución verificables | No presentarla como realizada |
| 7.4 Monitoring/alerting/notifications | Comprobación pública PASS, tres pruebas del monitor y workflow preparado | Falta activar el workflow remoto y observar historial; sin SLA ni percentiles medidos |
| 8.1-8.2 | Preguntas, hipótesis, medidas y diseño propuestos | No afirmar reclutamiento o resultado experimental |
| 8.3.1-8.3.2 | Historias To-Be y backlog de 53 SP | Estimación, no incremento experimental implementado |
| Student Outcome | Antecedentes AV1/TB1 | No inventar testimonios o aportes AV2 individuales |
| Archivos de AV2 | Reporte y presentación adaptados al alcance | Performance y exposición AV2 requieren su evidencia propia; no renombrar los de TB1 |

Esta auditoría es un documento interno de revisión. No se incluye en el PDF académico ni se usa para afirmar entrega AV2 completa.
