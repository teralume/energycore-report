# GitHub Actions: evidencia y explicación para AV2

Revisión del 03/11/2026. Esta guía distingue los workflows implementados, los resultados de sus ejecuciones y el estado de producción. No permite deducir qué observación concreta hizo el docente durante una exposición anterior.

## Qué mostrar durante la exposición

1. Abrir [Platform CI and delivery](https://github.com/teralume/energycore-platform/actions/workflows/ci-cd.yml) y seleccionar una ejecución del commit que se está explicando.
2. Abrir **CI - Tests and container build**. Mostrar el comando Maven `verify`, los resultados JUnit/Cucumber, la construcción Docker y el artefacto JAR.
3. Abrir el artefacto **energycore-platform-test-reports-SHA**. Surefire conserva los resultados incluso si una prueba falla; una carpeta o nombre de test por sí solo no prueba que el caso haya aprobado.
4. Explicar **CD - Cloud Run when enabled**: depende de CI, de un push a main y de `GCP_DEPLOY_ENABLED=true`. La variable no está definida en la revisión actual, por lo que el job se omite. El YAML preparado no demuestra un despliegue ejecutado.
5. Abrir el [monitoreo público](https://github.com/teralume/energycore-report/actions/workflows/monitoring.yml). Su fallo actual registra la indisponibilidad del backend por facturación cerrada; la web está accesible. El monitor conserva JSON y no crea cuentas ni modifica datos.

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

## Corrección concreta del backend

El smoke de deploy consultaba `/actuator/health`, una ruta no expuesta de forma anónima por la configuración de seguridad actual. Se cambió a `/api/v1/health` y se exige un objeto JSON con `status=UP`; HTTP 200 por sí solo no es suficiente. No se abrió Actuator ni se ampliaron permisos de autenticación.

El verificador se comprobó con cinco entradas: acepta `UP`; rechaza `DOWN`, JSON inválido, estado ausente y un array. La condición CD, el comando Maven, los triggers y los permisos permanecen iguales. Las evidencias de pruebas se conservan con `if: always()`; el JAR y Docker siguen sujetos al éxito de las pruebas.

La [ejecución del 03/11 que detectó el fallo](https://github.com/teralume/energycore-platform/actions/runs/41643972372) también reveló una dependencia de calendario en `Deleting a stored report`: solicitaba octubre de 2026 mientras la API registraba una lectura de noviembre. El HTTP 400 era correcto para ese período vacío. La prueba se corrigió en [abd1964](https://github.com/teralume/energycore-platform/commit/abd196438d3d1bd8f7de951aab31fae4aa0e0753) para tomar el día de `recordedAt` devuelto por la API, comprobar el período del reporte creado y confirmar que desaparece después del DELETE. No se modificó la regla de negocio ni se omitió el escenario. Maven `verify` local aprobó **28 pruebas JUnit y 60 escenarios Cucumber: 88 en total, sin fallos ni omisiones**. La verificación local utilizó JBR 21 con compilación `release 17`; Actions conserva su runner Java 17 y debe aprobar por separado para el commit integrado.

La revisión no elimina el incidente cloud: requiere que el titular restablezca la facturación antes de comprobar otra vez health, OpenAPI y flujos autenticados.
