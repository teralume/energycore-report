# Handoff: EnergyCore, evidencias y presentación Canva

2026-09-06 · Continuar en una sesión nueva sin rehacer el producto ni las capturas.

## Objetivo inmediato

Insertar las capturas reales de Swagger, aplicación web y Flutter Android en la presentación Canva existente. Revisar composición y legibilidad, mostrar las vistas previas y pedir aprobación puntual antes de guardar. Terminar solo después de confirmar que Canva guardó los cambios y verificar el resultado. No crear otra presentación.

## Permisos: bloqueo de la sesión anterior

- El usuario autorizó expresamente insertar las imágenes, pero NO quiere permisos permanentes «Always», aprobación automática global ni acceso irrestricto.
- `C:\Users\Asus\.codex\config.toml` fue comprobado con `approval_policy = "on-request"` y `sandbox_mode = "workspace-write"`.
- Aun después de que el usuario confirmó haber reiniciado Codex, la sesión anterior seguía recibiendo la política efectiva `never`. La carga devolvía exactamente: `MCP tool call requires approval, but approval policy is never`.
- No se encontró la causa del override en los archivos revisados. No afirmar que crear esta nueva sesión necesariamente lo solucionará: comprobar la política efectiva y realizar como máximo una prueba de carga si corresponde.
- No modificar configuraciones de seguridad, recomendar «Always» ni sortear la denegación mediante navegador, otro endpoint o alojamiento público temporal. Si persiste, informar el error exacto y detener las mutaciones; no repetir el mismo intento ni pedir reinicios indefinidamente.
- El permiso de Canva consultado era «Use my default», con predeterminado «Allow low-risk actions». Esto no garantizó que la operación pudiera ejecutarse.

## Ubicación y diseño exactos

Raíz: `C:\JeanLoa\Universidad\Diseño de Experimentos de Ingeniería de Software`

Usar **Universidad**, no `University`, ni LowCortisol. Los cinco repositorios son `energycore-report`, `energycore-platform`, `energycore-webapp`, `energycore-mobile` y `energycore-website`.

Canva: https://www.canva.com/design/DAHUaBAyBvU/vtK0ZX5t0G5EkHt0DUBn6w/edit

Design ID: `DAHUaBAyBvU`. Último dato conocido: 16 diapositivas; inspeccionar el estado actual antes de editar. Ninguna de las nuevas capturas locales fue insertada ni guardada en Canva. Tampoco dar por guardados borradores de rediseño anteriores cuyo commit fue rechazado.

## Diseño aprobado

EnergyCore es el producto de Teralume. Estética tecnológica/futurista, verde principal, negro/grafito y contraste fuerte, sin azul. Usar mascota/rayo e íconos significativos existentes, con capturas reales grandes. El usuario quiere diapositivas visualmente llenas, pero mantener alineación, jerarquía, márgenes y texto legible; no amontonar ni usar imágenes genéricas como evidencia. No sustituir Flutter por una web responsive.

## Archivos listos

Carpeta absoluta de imágenes:
`C:\JeanLoa\Universidad\Diseño de Experimentos de Ingeniería de Software\energycore-report\assets\evidence\implemented`

Selección principal:

- API: `swagger-live-overview.png`, `swagger-live-energy-endpoints.png`, `swagger-live-health-200.png`.
- Web: `webapp-live-login.png`, `webapp-live-home.png`, `webapp-live-energy-chart.png`, `webapp-live-energy-metrics.png`, `webapp-live-devices.png`. Respaldo: `webapp-live-energy.png`, `webapp-live-energy-full.png`.
- Android: `android-live-login-20260906-065244.png`, `android-live-home-20260906-065526.png`, `android-live-devices-20260906-065544.png`.
- Android actualizado tras corregir potencia: `android-live-energy-20260906-071106.png` (KPIs), `android-live-energy-20260906-071137.png` (habitación: **1370 W**).
- Android histórico de respaldo: `android-live-energy-20260906-065529.png`, `android-live-energy-20260906-065620.png`. No confundir estos estados anteriores con la verificación posterior al arreglo.

Las capturas son de ejecución local real: Angular/Flutter → Spring Boot → PostgreSQL aislado, con datos sintéticos de demostración. No se interceptaron respuestas HTTP para estas nuevas imágenes. No prueban sensores físicos, ahorro real ni despliegue en producción. Los kWh difieren entre tomas porque el muestreo continuaba.

Texto breve de contexto: «Ejecución local real con datos de demostración; no son mediciones físicas ni evidencia de producción».

## Fuentes de continuidad

- `energycore-report/presentation/evidence-audit-2026-09-06.md`: requisitos, capturas, limitaciones, pruebas y colocación recomendada; leer primero.
- `energycore-report/README.md`, sección 5.2.5: capturas Android ya incorporadas, incluida la corrección.
- `energycore-report/assets/evidence/implemented/openapi-live.json`: contrato real, OpenAPI 3.1.0, 100 operaciones.
- `preferences-concurrency-smoke.json` y `energy-power-smoke.json`, misma carpeta: resultados reales de regresión.

## Trabajo técnico terminado: no rehacer

- Carrera de preferencias: corregida en backend mediante bloqueo transaccional de User; regresiones concurrentes y navegación verificadas. No se afirma que los 403 de llamadas web antes del login estén corregidos.
- Potencia: backend sumaba watts de muestras sucesivas. Ahora habitación y topDevices usan potencia actual configurada de equipos ON, mientras kWh/costos permanecen acumulativos. API y Android confirmaron **120 + 350 + 900 = 1370 W**.
- Se agregaron `EnergyDashboardPowerTest` (5 pruebas) y `energycore-platform/scripts/smoke-energy-power.cjs`. Cinco pruebas ejecutadas con JUnit Platform Launcher: todas aprobadas; antes fallaban cuatro. `mvnw.cmd -o test-compile` pasó. Maven/Surefire estándar quedó bloqueado por plugin ausente y permisos de caché; no presentar la suite completa como aprobada.
- APK instalado cotejado por SHA-256 con el APK local: `96289E1CC4EDEB5CBCCFDD997CD7D2C5033B05D52F34151EA2CFF0571B0F4F53`.

## Límites y pendientes ajenos a esta edición

No hacer commits, push, deploy, compras ni cambios en Neon/Google Cloud sin nueva autorización. Preservar el árbol de trabajo sucio: contiene las correcciones y evidencias aún no publicadas. No mostrar credenciales/tokens ni publicar imágenes en servicios temporales.

Las entrevistas están excluidas por el usuario; él graba About-the-Product. No inventar integrantes, entrevistas ni resultados experimentales. Datos del reporte: Jean Franck Loa Rojas, U20241E406, séptimo ciclo, NRC 9100, profesor Alex Humberto Sánchez Ponce. No ampliar el reporte ahora.

La auditoría también señala una diferencia tecnológica pendiente de confirmar con el docente: el enunciado pide Vue/PrimeVue y ASP.NET Core/C#, pero el proyecto autorizado para reutilización usa Angular/Spring Boot. No migrar automáticamente.

Las suites históricas registraban 83 casos descubiertos, **40 ejecutados y 43 omitidos**, no 83 ejecutados. Las cinco pruebas nuevas de potencia son una ejecución separada.

Servicios de la sesión anterior: backend 8080, web 4300, PostgreSQL aislado 55432 y Pixel_7 `emulator-5554`. Su actividad puede haber cambiado tras reiniciar; verificar solo si hace falta. Las capturas ya guardadas no requieren arrancarlos.

## Próxima acción

Leer la auditoría, comprobar los permisos efectivos y usar la skill `canva-edit-design`. Si la carga funciona, inspeccionar las páginas existentes, colocar las imágenes sin tapar contenido, mostrar las miniaturas y pedir aprobación puntual para guardar. Confirmar el commit exitoso y devolver el enlace al diseño. Si el permiso vuelve a fallar, detenerse con un diagnóstico concreto, sin afirmar que se insertaron imágenes.
