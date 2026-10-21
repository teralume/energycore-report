# Sprint Planning detallados - EnergyCore

Actualizado: **20/10/2026**.

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

Sprints 1-3: reconstrucción desde artefactos, no actas contemporáneas. Sprint 4: revisión del registro TB1. Sprints 5-7: propuesta futura. Fecha de reunión, inicio/fin, asistentes y capacidad histórica: No registrados. No se fabrican burn-down, velocidad, horas reales o porcentajes de avance. Responsable técnico histórico documentado: Jean Loa; otros apoyos se limitan a evidencia registrada. Los responsables de tareas futuras deben aceptar su asignación en Trello.

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

## Sprint 7: Recuperación y piloto experimental

**Naturaleza:** Propuesto / Por iniciar.

**Objetivo:** Recuperación y piloto experimental.

**Entrada:** Ready completo y disponibilidad confirmada por el equipo; sin compromiso de fechas aún.

| ID | Título | SP | Responsable | Estado |
| :-- | :-- | :-- | :-- | :-- |
| US-20A | Recuperación después de desconexión | 5 | Por asignar | Por iniciar |
| US-20B | Reintento idempotente | 3 | Por asignar | Por iniciar |
| TS-04 | Dashboard de resultados | 5 | Por asignar | Por iniciar |
| TS-05 | Exportación anonimizada | 3 | Por asignar | Por iniciar |

**Estimación:** 16 SP del bloque funcional/experimental.

**Trabajo integrado:** Probar reintentos idempotentes; ejecutar protocolo consentido; anonimizar resultados, analizar y registrar decisiones.

**Salida/evidencia:** Dataset y análisis por generar; no hay muestra reclutada o resultados medidos.

**Dependencias y riesgos:** Depende de Sprints 5-6, NF-05/06, distribución móvil y disponibilidad de participantes.

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


## Tablero Trello verificado

[EnergyCore - Product Backlog y Sprint Planning](https://trello.com/b/kFru7uh2/energycore-product-backlog-y-sprint-planning)

Verificación: 20/10/2026. 64 tarjetas con descripción, estado y enlace propio; 0 duplicados o discrepancias. El tablero es privado. No se enviaron invitaciones ni se atribuyeron responsables o actividad histórica sin confirmación.

| Sprint | Tarjeta de planificación | Naturaleza |
|:--|:--|:--|
| 1 | [PLAN-01](https://trello.com/c/Y1aCkOEg/48-plan-01-sprint-1-base-integrada-web-y-api-sprint-1) | Reconstrucción histórica |
| 2 | [PLAN-02](https://trello.com/c/jwuMwbiK/49-plan-02-sprint-2-experiencia-m%C3%B3vil-y-automatizaci%C3%B3n-conectadas-sprint-2) | Reconstrucción histórica |
| 3 | [PLAN-03](https://trello.com/c/u2SEoccW/50-plan-03-sprint-3-evidencia-de-av1-y-trazabilidad-t%C3%A9cnica-sprint-3) | Reconstrucción histórica |
| 4 | [PLAN-04](https://trello.com/c/We6pgTe3/51-plan-04-sprint-4-revisi%C3%B3n-tb1-y-respuesta-a-observaciones-sprint-4) | Revisión TB1 |
| 5 | [PLAN-05](https://trello.com/c/4giUDgtV/52-plan-05-sprint-5-preparar-medici%C3%B3n-reproducible-sprint-5) | Propuesto / Por iniciar |
| 6 | [PLAN-06](https://trello.com/c/FDYkZKQK/53-plan-06-sprint-6-implementar-tratamientos-seguros-sprint-6) | Propuesto / Por iniciar |
| 7 | [PLAN-07](https://trello.com/c/8TzKs9GB/54-plan-07-sprint-7-recuperaci%C3%B3n-y-piloto-experimental-sprint-7) | Propuesto / Por iniciar |

Distribución verificada: Backlog 13; Por iniciar 14; En curso 0; Implementado - por verificar 33; Verificado - pruebas y CI 4. El acta `trello-sync-result.json` contiene los 64 enlaces y la confirmación de lectura posterior.
