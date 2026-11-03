# Sprint Planning de antecedentes - AV2

Línea base de planificación: **20/10/2026**. Alcance actualizado según la rúbrica de **S12 | AV2**.

 Datos cuantitativos y criterio de capacidad

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


## Reglas de trazabilidad

Sprints 1-3: reconstrucción desde artefactos, no actas contemporáneas. Sprint 4: revisión del registro TB1. Fecha de reunión, inicio/fin, asistentes y capacidad histórica: No registrados. No se fabrican burn-down, velocidad, horas reales o porcentajes de avance. Responsable técnico histórico documentado: Jean Loa; otros apoyos se limitan a evidencia registrada. Los responsables de tareas futuras deben aceptar su asignación en Trello.

## Sprint 1: Base integrada web y API

**Naturaleza:** Reconstrucción histórica; implementación disponible, sin acta de compromiso original.

**Objetivo:** Base integrada web y API.

**Entrada:** Artefactos y commits existentes; sin planificación original verificable.

| ID | Título | SP | Responsable | Estado |
| :-- | :-- | :-- | :-- | :-- |
| US-02 | Registro e inicio de sesión | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-03 | Recuperación de contraseña | 3 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-04A | Gestión de sedes | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-04B | Gestión de habitaciones | 3 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-05 | Vinculación de dispositivos | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-06 | Control remoto | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-10A | Dashboard energético | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-10B | Histórico energético | 3 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-16A | Comparación de planes | 3 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-16B | Suscripción y pago académico | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-01 | Landing Page y CTA | 5 | Jean (implementación documentada) | Implementado; verificar alcance |

**Estimación:** 47 SP del bloque funcional/experimental.

**Trabajo integrado:** Integrar contratos IAM, espacios, dispositivos, energía y planes; conectar CTA y login; comprobar autorización y consultas con datos controlados.

**Salida/evidencia:** Backend/Angular/Landing y suites actuales. No acredita pruebas históricas de cada sprint.

**Dependencias y riesgos:** Confirmar cobertura por historia en UI; el pago sigue siendo académico.

**Capacidad:** No medida históricamente / por confirmar para compromisos futuros.

**Desglose de referencia:** paquetes propuestos, no horas ejecutadas; dos tareas por historia. El equipo debe dividir nuevamente si una tarea excede 8 h al refinar.

| Tarea | Descripción | h estimadas | Responsable | Condición de cierre |
| :-- | :-- | :-- | :-- | :-- |
| US-02-A | Revisar contrato, alcance y criterio de Registro e inicio de sesión | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-02-B | Integrar implementación y prueba de Registro e inicio de sesión | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-03-A | Revisar contrato, alcance y criterio de Recuperación de contraseña | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-03-B | Integrar implementación y prueba de Recuperación de contraseña | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-04A-A | Revisar contrato, alcance y criterio de Gestión de sedes | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-04A-B | Integrar implementación y prueba de Gestión de sedes | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-04B-A | Revisar contrato, alcance y criterio de Gestión de habitaciones | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-04B-B | Integrar implementación y prueba de Gestión de habitaciones | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-05-A | Revisar contrato, alcance y criterio de Vinculación de dispositivos | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-05-B | Integrar implementación y prueba de Vinculación de dispositivos | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-06-A | Revisar contrato, alcance y criterio de Control remoto | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-06-B | Integrar implementación y prueba de Control remoto | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-10A-A | Revisar contrato, alcance y criterio de Dashboard energético | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-10A-B | Integrar implementación y prueba de Dashboard energético | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-10B-A | Revisar contrato, alcance y criterio de Histórico energético | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-10B-B | Integrar implementación y prueba de Histórico energético | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-16A-A | Revisar contrato, alcance y criterio de Comparación de planes | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-16A-B | Integrar implementación y prueba de Comparación de planes | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-16B-A | Revisar contrato, alcance y criterio de Suscripción y pago académico | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-16B-B | Integrar implementación y prueba de Suscripción y pago académico | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-01-A | Revisar contrato, alcance y criterio de Landing Page y CTA | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-01-B | Integrar implementación y prueba de Landing Page y CTA | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |

Total de referencia: **116 h**, sin evidencia de capacidad para comprometer ese total. No implica duración del sprint ni aceptación del equipo.

## Sprint 2: Experiencia móvil y automatización conectadas

**Naturaleza:** Reconstrucción histórica; funcionalidad disponible, aceptación móvil física abierta.

**Objetivo:** Experiencia móvil y automatización conectadas.

**Entrada:** Artefactos y commits existentes; sin planificación original verificable.

| ID | Título | SP | Responsable | Estado |
| :-- | :-- | :-- | :-- | :-- |
| US-07 | Grupos de dispositivos | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-08 | Rutinas | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-11A | Reglas y alertas | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-11B | Preferencias de notificación | 3 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-12A | Metas energéticas | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-12B | Reportes por periodo | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-09 | Modos de operación | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-15 | Soporte y mantenimiento | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-13 | Perfiles y permisos | 5 | Jean (implementación documentada) | Implementado; verificar alcance |
| US-14 | Tema e idiomas | 5 | Jean (implementación documentada) | Implementado; verificar alcance |

**Estimación:** 48 SP del bloque funcional/experimental.

**Trabajo integrado:** Conectar grupos, rutinas, modos, alertas, metas y soporte con sedes/dispositivos; conservar permisos e idiomas en Flutter.

**Salida/evidencia:** Código Flutter, matriz de paridad y CI Android/iOS; no publicación en tienda.

**Dependencias y riesgos:** NF-05/NF-06 no se cierran con un build de simulador.

**Capacidad:** No medida históricamente / por confirmar para compromisos futuros.

**Desglose de referencia:** paquetes propuestos, no horas ejecutadas; dos tareas por historia. El equipo debe dividir nuevamente si una tarea excede 8 h al refinar.

| Tarea | Descripción | h estimadas | Responsable | Condición de cierre |
| :-- | :-- | :-- | :-- | :-- |
| US-07-A | Revisar contrato, alcance y criterio de Grupos de dispositivos | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-07-B | Integrar implementación y prueba de Grupos de dispositivos | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-08-A | Revisar contrato, alcance y criterio de Rutinas | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-08-B | Integrar implementación y prueba de Rutinas | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-11A-A | Revisar contrato, alcance y criterio de Reglas y alertas | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-11A-B | Integrar implementación y prueba de Reglas y alertas | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-11B-A | Revisar contrato, alcance y criterio de Preferencias de notificación | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-11B-B | Integrar implementación y prueba de Preferencias de notificación | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-12A-A | Revisar contrato, alcance y criterio de Metas energéticas | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-12A-B | Integrar implementación y prueba de Metas energéticas | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-12B-A | Revisar contrato, alcance y criterio de Reportes por periodo | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-12B-B | Integrar implementación y prueba de Reportes por periodo | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-09-A | Revisar contrato, alcance y criterio de Modos de operación | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-09-B | Integrar implementación y prueba de Modos de operación | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-15-A | Revisar contrato, alcance y criterio de Soporte y mantenimiento | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-15-B | Integrar implementación y prueba de Soporte y mantenimiento | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-13-A | Revisar contrato, alcance y criterio de Perfiles y permisos | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-13-B | Integrar implementación y prueba de Perfiles y permisos | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-14-A | Revisar contrato, alcance y criterio de Tema e idiomas | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-14-B | Integrar implementación y prueba de Tema e idiomas | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |

Total de referencia: **116 h**, sin evidencia de capacidad para comprometer ese total. No implica duración del sprint ni aceptación del equipo.

## Sprint 3: Evidencia de AV1 y trazabilidad técnica

**Naturaleza:** Reconstrucción histórica; artefactos y automatización disponibles.

**Objetivo:** Evidencia de AV1 y trazabilidad técnica.

**Entrada:** Artefactos y commits existentes; sin planificación original verificable.

**Estimación formalizada:** 17 SP de calidad/habilitadores, sin contabilizarlos como velocidad histórica.

**Trabajo integrado:** Mantener reportes, OpenAPI, capturas, fuentes y guías; mapear pruebas a reglas y endpoints; conservar autoría real.

**Salida/evidencia:** Reportes AV1, 109 tests y workflows. Las historias TECH/NF se formalizan ahora, sin atribuirles fecha retroactiva.

**Dependencias y riesgos:** TECH-01/02 y NF-01/02 verificados en su alcance; TECH-03 requiere revisión cruzada.

**Capacidad:** No medida históricamente / por confirmar para compromisos futuros.

## Sprint 4: Revisión TB1 y respuesta a observaciones

**Naturaleza:** Revisión del Sprint Planning registrado; sin inventar una nueva reunión.

**Objetivo:** Revisión TB1 y respuesta a observaciones.

**Entrada:** Artefactos y commits existentes; sin planificación original verificable.

**Estimación heredada:** 52 h / 10 tareas ET; tiempos reales no registrados.

**Trabajo integrado:** Completar criterios medibles, tipos NF/TECH/SPIKE, ERD visible y trazabilidad a evidencias y tablero.

**Salida/evidencia:** README, fuentes PlantUML, SVG, PDF y validadores.

**Dependencias y riesgos:** Revisiones individuales ET-06 a ET-10 no se consideran hechas por tener CI verde.

**Capacidad:** No medida históricamente / por confirmar para compromisos futuros.

El registro de tareas original se conserva en [fuente del Sprint 4](sprint-4-source-before-refinement.md). Su estado To do se conserva como Por verificar hasta evidencia individual; el refinamiento actual cierra el documento de ET-04, no una ceremonia histórica.

## Planificación To-Be exigida por la rúbrica AV2

La rúbrica de **S12 | AV2** incluye Product Backlog y Sprint Backlogs To-Be, además del desglose de las historias en tareas de ingeniería de 4 a 8 horas. Por ello se incorpora aquí la planificación existente de los Sprints 5-7, tomada de [Sprint Planning detallados](sprint-planning.md). Las secciones siguientes son una **propuesta por iniciar**: documentan trabajo a ejecutar, no incrementos implementados, sesiones con participantes ni resultados experimentales.

| Sprint propuesto | Historias | SP estimados | Tareas de ingeniería | Horas estimadas |
|:--|--:|--:|--:|--:|
| 5: medición reproducible | 5 | 21 | 10 | 52 |
| 6: tratamientos seguros | 4 | 16 | 8 | 40 |
| 7: preparar recuperación y análisis reproducible | 4 | 16 | 8 | 40 |
| **Total To-Be** | **13** | **53** | **26** | **132** |

Los 53 SP y las 132 h expresan estimaciones distintas; no se suman ni se convierten en velocidad. Las 12 h máximas de los tres spikes pertenecen al backlog de investigación y no están incluidas en esas 132 h. Cada historia tiene dos tareas de 4 u 8 h. Los responsables continúan **Por asignar** hasta que acepten el trabajo y confirmen disponibilidad; no hay compromiso de fechas ni capacidad acreditada.

### Prioridad, preguntas experimentales e Impact Map

La priorización parte del [Question Backlog y Experiment Cards](../README.md#814-question-backlog) y del [Impact Map existente](../assets/diagrams/impact-map.svg), cuya [fuente](../assets/diagrams/source/impact-map.puml) conecta el objetivo **ayudar a tomar decisiones energéticas informadas** con responsables del hogar, administradores de negocio y operadores autorizados. La tabla hace explícita esa trazabilidad; no modifica el mapa ni afirma que el impacto ya se haya logrado.

| Orden de preparación | Historias | Pregunta / experimento | Relación con el Impact Map y motivo |
|:--|:--|:--|:--|
| 1. Medición y consentimiento, Sprint 5 | TS-01, TS-02A, TS-02B, US-19, TS-03 | ERQ-01 a ERQ-05; EC-01 a EC-03 | Habilitan medir el objetivo del mapa con asignación estable, eventos equivalentes, datos controlados y participación informada. Son prerrequisitos de evidencia, no un beneficio de usuario demostrado. |
| 2. Comprensión y acción, Sprint 6 | US-21, US-17A, US-17B | ERQ-01 y ERQ-02, prioridad 41.7; EC-01; comparación web/Android de ERQ-03 | Hogar: **Comprende consumo y costo** mediante dashboard y lecturas. Operador: **Ejecuta tareas seguras** mediante controles según permisos. La frescura del dato precede a explicar y ejecutar una acción. |
| 3. Protección de alcance, Sprint 6 | US-18 | ERQ-04, prioridad 26.7; EC-02 | Administrador: **Controla espacios y sedes**. Operador: **Ejecuta tareas seguras**. Confirmar dispositivos afectados protege cualquier comando posterior y es condición de seguridad para probar reintentos. |
| 4. Recuperación y evidencia, Sprint 7 | US-20A, US-20B, TS-04, TS-05 | ERQ-05, prioridad 40.0; EC-03; métricas de EC-01 y EC-02 | Recuperar una tarea sin duplicar comandos sostiene los controles seguros del operador. Dashboard de resultados y exportación son habilitadores para evaluar el objetivo del mapa, no resultados ya obtenidos. |

El score del Question Backlog ordena incertidumbres, pero el Sprint Backlog respeta dependencias y guardrails. Aunque ERQ-05 tiene mayor score que ERQ-04, su prueba necesita primero una tarea instrumentada y un control seguro con alcance confirmado. La instrumentación equivalente de web y Flutter se prepara desde el Sprint 5 para medir ERQ-03 sobre los mismos datos. La selección y los valores conservan la propuesta registrada; deben ratificarse con el equipo antes de comprometer capacidad.

**Límite de AV2:** se entrega este plan y sus condiciones de cierre. La ejecución del piloto, el reclutamiento, el análisis de resultados y las decisiones de adopción no se acreditan mediante estas tablas. Tampoco se atribuyen entrevistas o una aceptación individual de las tareas.

## Sprint 5: Preparar medición reproducible

**Naturaleza:** Propuesto / Por iniciar.

**Objetivo:** Preparar medición reproducible.

**Entrada:** Ready completo y disponibilidad confirmada por el equipo; sin compromiso de fechas aún.

| ID | Título | SP | Responsable | Estado |
| :-- | :-- | :-- | :-- | :-- |
| TS-01 | Asignación y configuración de variantes | 5 | Por asignar | Por iniciar |
| TS-02A | Contrato de eventos web | 3 | Por asignar | Por iniciar |
| TS-02B | Contrato equivalente en Flutter | 5 | Por asignar | Por iniciar |
| US-19 | Aviso y control de telemetría | 5 | Por asignar | Por iniciar |
| TS-03 | Dataset semilla del experimento | 3 | Por asignar | Por iniciar |

**Estimación:** 21 SP del bloque funcional/experimental.

**Trabajo integrado:** Definir variantes y consentimiento; validar contratos de eventos web/móvil sin PII; versionar dataset reiniciable.

**Salida/evidencia:** Esquemas, tests de eventos y dataset; aún no existen resultados del piloto.

**Dependencias y riesgos:** SPIKE-02 antes de compromiso; sin horas disponibles ni equipo asignado confirmados.

**Capacidad:** No medida históricamente / por confirmar para compromisos futuros.

**Desglose de referencia:** paquetes propuestos, no horas ejecutadas; dos tareas por historia. El equipo debe dividir nuevamente si una tarea excede 8 h al refinar.

| Tarea | Descripción | h estimadas | Responsable | Condición de cierre |
| :-- | :-- | :-- | :-- | :-- |
| TS-01-A | Revisar contrato, alcance y criterio de Asignación y configuración de variantes | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-01-B | Integrar implementación y prueba de Asignación y configuración de variantes | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-02A-A | Revisar contrato, alcance y criterio de Contrato de eventos web | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-02A-B | Integrar implementación y prueba de Contrato de eventos web | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-02B-A | Revisar contrato, alcance y criterio de Contrato equivalente en Flutter | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-02B-B | Integrar implementación y prueba de Contrato equivalente en Flutter | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-19-A | Revisar contrato, alcance y criterio de Aviso y control de telemetría | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-19-B | Integrar implementación y prueba de Aviso y control de telemetría | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-03-A | Revisar contrato, alcance y criterio de Dataset semilla del experimento | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-03-B | Integrar implementación y prueba de Dataset semilla del experimento | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |

Total de referencia: **52 h**, sin evidencia de capacidad para comprometer ese total. No implica duración del sprint ni aceptación del equipo.

## Sprint 6: Implementar tratamientos seguros

**Naturaleza:** Propuesto / Por iniciar.

**Objetivo:** Implementar tratamientos seguros.

**Entrada:** Ready completo y disponibilidad confirmada por el equipo; sin compromiso de fechas aún.

| ID | Título | SP | Responsable | Estado |
| :-- | :-- | :-- | :-- | :-- |
| US-21 | Frescura y sincronización | 3 | Por asignar | Por iniciar |
| US-17A | Explicación de anomalía | 5 | Por asignar | Por iniciar |
| US-17B | Acción permitida | 3 | Por asignar | Por iniciar |
| US-18 | Vista previa de alcance | 5 | Por asignar | Por iniciar |

**Estimación:** 16 SP del bloque funcional/experimental.

**Trabajo integrado:** Integrar recomendación en Energy Monitoring; delegar acciones a Device Control; mostrar alcance y frescura.

**Salida/evidencia:** Tests de mapper/componente, feature flag y smoke web/Android por generar.

**Dependencias y riesgos:** Depende de Sprint 5 y NF-03/04; no afirmar mejora porcentual sin experimento.

**Capacidad:** No medida históricamente / por confirmar para compromisos futuros.

**Desglose de referencia:** paquetes propuestos, no horas ejecutadas; dos tareas por historia. El equipo debe dividir nuevamente si una tarea excede 8 h al refinar.

| Tarea | Descripción | h estimadas | Responsable | Condición de cierre |
| :-- | :-- | :-- | :-- | :-- |
| US-21-A | Revisar contrato, alcance y criterio de Frescura y sincronización | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-21-B | Integrar implementación y prueba de Frescura y sincronización | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-17A-A | Revisar contrato, alcance y criterio de Explicación de anomalía | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-17A-B | Integrar implementación y prueba de Explicación de anomalía | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-17B-A | Revisar contrato, alcance y criterio de Acción permitida | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-17B-B | Integrar implementación y prueba de Acción permitida | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-18-A | Revisar contrato, alcance y criterio de Vista previa de alcance | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-18-B | Integrar implementación y prueba de Vista previa de alcance | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |

Total de referencia: **40 h**, sin evidencia de capacidad para comprometer ese total. No implica duración del sprint ni aceptación del equipo.

## Sprint 7: Preparar recuperación y análisis reproducible

**Naturaleza:** Propuesto / Por iniciar.

**Objetivo:** Preparar recuperación y análisis reproducible mediante capacidades técnicas verificables.

**Entrada:** Ready completo y disponibilidad confirmada por el equipo; sin compromiso de fechas aún.

| ID | Título | SP | Responsable | Estado |
| :-- | :-- | :-- | :-- | :-- |
| US-20A | Recuperación después de desconexión | 5 | Por asignar | Por iniciar |
| US-20B | Reintento idempotente | 3 | Por asignar | Por iniciar |
| TS-04 | Dashboard de resultados | 5 | Por asignar | Por iniciar |
| TS-05 | Exportación anonimizada | 3 | Por asignar | Por iniciar |

**Estimación:** 16 SP del bloque funcional/experimental.

**Trabajo integrado:** Probar recuperación y reintentos idempotentes; preparar el dashboard y la exportación anonimizada con datos semilla. Las 40 h cubren estas capacidades técnicas, no la ejecución del piloto, el reclutamiento ni el análisis de resultados de participantes.

**Salida/evidencia prevista:** Pruebas de recuperación, dashboard reproducible y exportación verificada con datos semilla, vinculados a sus commits. No se generan aquí muestra reclutada, mediciones del piloto ni conclusiones experimentales.

**Dependencias y riesgos:** Depende de Sprints 5-6, NF-05/06, contratos de eventos y disponibilidad de un entorno móvil verificable. El reclutamiento y la ejecución experimental requieren una planificación posterior independiente.

**Capacidad:** No medida históricamente / por confirmar para compromisos futuros.

**Desglose de referencia:** paquetes propuestos, no horas ejecutadas; dos tareas por historia. El equipo debe dividir nuevamente si una tarea excede 8 h al refinar.

| Tarea | Descripción | h estimadas | Responsable | Condición de cierre |
| :-- | :-- | :-- | :-- | :-- |
| US-20A-A | Revisar contrato, alcance y criterio de Recuperación después de desconexión | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-20A-B | Integrar implementación y prueba de Recuperación después de desconexión | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-20B-A | Revisar contrato, alcance y criterio de Reintento idempotente | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| US-20B-B | Integrar implementación y prueba de Reintento idempotente | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-04-A | Revisar contrato, alcance y criterio de Dashboard de resultados | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-04-B | Integrar implementación y prueba de Dashboard de resultados | 8 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-05-A | Revisar contrato, alcance y criterio de Exportación anonimizada | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |
| TS-05-B | Integrar implementación y prueba de Exportación anonimizada | 4 | Por asignar | Contrato y test del criterio enlazados a SHA; sin atribución de ejecución retrospectiva |

Total de referencia: **40 h**, sin evidencia de capacidad para comprometer ese total. No implica duración del sprint ni aceptación del equipo.


## Tablero de seguimiento

[EnergyCore en Trello](https://trello.com/b/kFru7uh2/energycore-product-backlog-y-sprint-planning). Los planes 1-4 se conservan como antecedentes; los planes 5-7 son propuestas To-Be incorporadas para cubrir la rúbrica de AV2.

| Sprint propuesto | Tarjeta de planificación | Estado documentado |
|:--|:--|:--|
| 5 | [PLAN-05](https://trello.com/c/4giUDgtV/52-plan-05-sprint-5-preparar-medici%C3%B3n-reproducible-sprint-5) | Propuesto / Por iniciar |
| 6 | [PLAN-06](https://trello.com/c/FDYkZKQK/53-plan-06-sprint-6-implementar-tratamientos-seguros-sprint-6) | Propuesto / Por iniciar |
| 7 | [PLAN-07](https://trello.com/c/8TzKs9GB/54-plan-07-sprint-7-recuperaci%C3%B3n-y-piloto-experimental-sprint-7) | Propuesto / Por iniciar |

Los enlaces proceden del registro verificado el 20/10/2026 en [trello-sync-result.json](trello-sync-result.json); esta actualización documental no es una nueva comprobación del tablero ni atribuye asignaciones aceptadas. Las 26 tareas To-Be se desglosan en este documento y no se afirman como 26 tarjetas independientes ya creadas en Trello.
