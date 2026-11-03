# GitHub Actions: evidencia y explicación para AV2

Revisión del 03/11/2026. Esta guía distingue los workflows implementados, los resultados de sus ejecuciones y el estado de producción. No permite deducir qué observación concreta hizo el docente durante una exposición anterior.

## Qué mostrar durante la exposición

1. Abrir [Platform CI and delivery](https://github.com/teralume/energycore-platform/actions/workflows/ci-cd.yml) y seleccionar una ejecución del commit que se está explicando.
2. Abrir **CI - Tests and container build**. Mostrar el comando Maven `verify`, los resultados JUnit/Cucumber, la construcción Docker y el artefacto JAR.
3. Abrir el artefacto **energycore-platform-test-reports-SHA**. Surefire conserva los resultados incluso si una prueba falla; una carpeta o nombre de test por sí solo no prueba que el caso haya aprobado.
4. Explicar **CD - Cloud Run when enabled**: depende de CI, de un push a main y de `GCP_DEPLOY_ENABLED=true`. En la [ejecución de main `3f74d478`](https://github.com/teralume/energycore-platform/actions/runs/41646065500), CI terminó en `success` y CD en `skipped`. El YAML preparado no demuestra un despliegue ejecutado.
5. Abrir el [monitoreo de recuperación](https://github.com/teralume/energycore-report/actions/runs/41651099079), ejecutado sobre `main` en `e1e26416`: las tres superficies aprobaron el 03/11/2026 a las 14:10:53 UTC (09:10:53 de Lima), después de la reactivación de facturación comunicada en la sesión. Conservar también el incidente de las 13:08:52 UTC (08:08:52 de Lima), cuando API y OpenAPI devolvieron 503. El monitor conserva JSON y no crea cuentas ni modifica datos; el PASS puntual no prueba disponibilidad continua.

Un job puede contener varios pasos de pruebas y compilación. Esa organización es válida. Los nombres ahora distinguen CI de CD; no se añadieron jobs vacíos para cambiar el dibujo del pipeline.

## Cómo interpretar los resultados

| Señal | Significado verificable |
|:--|:--|
| CI success | Los pasos de esa ejecución y commit aprobaron. No acredita disponibilidad actual de la API. |
| Deploy skipped | No se cumplió alguna condición de ejecución. No es un despliegue aprobado. |
| Monitor failure | Alguna superficie pública falló o devolvió contenido inválido. Debe conservarse y analizarse. |
| Artefacto publicado | Archivo producido o validado por el workflow. No equivale a publicar en Cloud Run, Firebase o una tienda. |
| Runner.app | Build para simulador iOS. No acredita ejecución en iPhone ni distribución TestFlight. |

## Estado inspeccionado

Los cinco repositorios tienen CI. Backend, Web Application y Landing configuran un deploy condicionado, pero `GCP_DEPLOY_ENABLED` y `FIREBASE_DEPLOY_ENABLED` no están definidas en los repositorios correspondientes. Las ramas se inspeccionaron sin protección; aprobar CI no bloquea por sí solo un push directo. La revisión humana tampoco se genera automáticamente.

La Landing además conserva GitHub Pages en modo legacy desde `main:/`; esa publicación es independiente del job `verify`. Vincularla a un workflow con dependencia explícita de pruebas sería una mejora posterior. No se modificó Pages ni se habilitó el despliegue productivo en esta revisión.

## Matriz de capacidades y evidencia del pipeline

La matriz relaciona capacidades con implementación y resultados observados. No convierte un número de filas en un porcentaje de implementación: la rúbrica pide al menos 50 %, pero no define aquí un denominador ponderado. Corresponde sustentar el alcance con estos controles y sus límites, sin declarar un porcentaje no medido.

| Capacidad | Evidencia concreta | Estado y límite |
|:--|:--|:--|
| Integración por cambio | Los cinco workflows de CI declaran `push`, `pull_request` y ejecución manual; el run backend `41646065500` se activó por push a `main`. | Implementado. No equivale a protección de ramas ni aprobación humana. |
| Pruebas backend | Job `125951592147`, Maven `verify`: 28 JUnit + 60 Cucumber, 88 ejecutadas, 0 fallos, errores u omisiones. | PASS para `3f74d478`; la integración usa la configuración de test, no demuestra todos los recorridos de producción. |
| Compilación y contenedor | En el mismo job aprobaron Maven y `Build container from verified source`. | Build verificado. La imagen construida no se presenta como promovida a Cloud Run. |
| Artefactos de entrega | Reportes Surefire `13235147141` y paquete backend `13234109978`, asociados al SHA y con digest de GitHub. | Publicados. El workflow conserva los reportes con `if: always()` y publica el paquete después de las pruebas. |
| Staging y aprobación de entorno | No aparecen jobs de staging ni una aprobación protegida en el workflow inspeccionado. | No implementados como etapas verificadas. |
| Despliegue productivo | Job dependiente de `verify`, condicionado a `main`, `push` y variable de habilitación; OIDC declarado. | CD `skipped` en el run observado. No se cuenta como despliegue exitoso ni como promoción del mismo binario. |
| Smoke posterior al despliegue | El YAML consulta `/api/v1/health` y valida un objeto JSON con `status=UP`. | Implementado en código; no ejecutado por ese job de CD omitido. |
| Operación y detección | `monitoring.yml` prueba sus reglas, consulta health/OpenAPI/web y conserva JSON 30 días; run `41651099079` y artefacto `13237586113`. | PASS puntual tras un fallo real conservado. No mide p95, SLA ni estado autenticado del usuario. |
| Avisos operativos | Un fallo deja código de salida no cero y job rojo visible en Actions. | Evidencia de detección y diagnóstico. La entrega de correo depende de suscripciones; no se verificó recepción ni hay integración de guardia acreditada. |

El [registro saneado de CI y recuperación](../assets/evidence/implemented/av2-recovery-2026-11-03.json) conserva SHA, jobs, artefactos, tiempos y resultados. Los benchmarks y los workflows del resto de componentes se relacionan en [la comparación DevOps](devops-benchmark-av2.md). La ejecución aprobada de tests no sustituye entrevistas, auditoría externa o revisión por pares.

## Corrección concreta del backend

El smoke de deploy consultaba `/actuator/health`, una ruta no expuesta de forma anónima por la configuración de seguridad actual. Se cambió a `/api/v1/health` y se exige un objeto JSON con `status=UP`; HTTP 200 por sí solo no es suficiente. No se abrió Actuator ni se ampliaron permisos de autenticación.

El verificador se comprobó con cinco entradas: acepta `UP`; rechaza `DOWN`, JSON inválido, estado ausente y un array. La condición CD, el comando Maven, los triggers y los permisos permanecen iguales. Las evidencias de pruebas se conservan con `if: always()`; el JAR y Docker siguen sujetos al éxito de las pruebas.

La [ejecución del 03/11 que detectó el fallo](https://github.com/teralume/energycore-platform/actions/runs/41643972372) también reveló una dependencia de calendario en `Deleting a stored report`: solicitaba octubre de 2026 mientras la API registraba una lectura de noviembre. El HTTP 400 era correcto para ese período vacío. La prueba se corrigió en [abd1964](https://github.com/teralume/energycore-platform/commit/abd196438d3d1bd8f7de951aab31fae4aa0e0753) para tomar el día de `recordedAt` devuelto por la API, comprobar el período del reporte creado y confirmar que desaparece después del DELETE. No se modificó la regla de negocio ni se omitió el escenario. Maven `verify` local aprobó **28 pruebas JUnit y 60 escenarios Cucumber: 88 en total, sin fallos ni omisiones**. La verificación local utilizó JBR 21 con compilación `release 17`; Actions conserva su runner Java 17 y debe aprobar por separado para el commit integrado.

La integración quedó comprobada en [main `3f74d478`](https://github.com/teralume/energycore-platform/actions/runs/41646065500) con Java 17: **28 pruebas JUnit y 60 escenarios Cucumber, 88 en total, sin fallos, errores ni omisiones**, más construcción de contenedor y publicación de artefactos. Se conserva el fallo anterior como antecedente de la corrección; no se renombra como una ejecución aprobada.

## Incidente y recuperación observada

El [registro de las 13:08:52 UTC](../assets/evidence/implemented/av2-monitoring-2026-11-03.json) acredita API/OpenAPI 503 y web 200; la inspección del proveedor atribuyó el rechazo a facturación deshabilitada en ese momento. Después de la reactivación comunicada en la sesión, el [monitor de las 14:10:53 UTC](https://github.com/teralume/energycore-report/actions/runs/41651099079) obtuvo health 200 (`status=UP`), OpenAPI válido 200 y HTML web 200. No se afirma que la facturación siga cerrada ni se elimina el incidente histórico. Estas observaciones no determinan por sí solas el inicio o la duración exacta de la caída, y no acreditan login ni tareas del usuario.

## Inspección técnica complementaria

La lectura del código en `3f74d478` confirma `ddl-auto=update` y un valor predeterminado de CORS que incluye `localhost:4200`; son observaciones para revisar migraciones y la configuración efectiva, no vulnerabilidades explotadas demostradas. También se detectó una cifra documental desactualizada: 6.1.1 decía 23 pruebas JUnit y omitía los cinco casos de `EnergyDashboardPowerTest`. El registro de CI respalda su corrección a 28. Esta inspección asistida por IA no acredita aprobación humana de un Pull Request.
