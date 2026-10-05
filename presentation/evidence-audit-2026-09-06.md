# Auditoría de evidencias AV1 - 6 de septiembre de 2026

## Requisito comprobado

El Enunciado.pdf, páginas físicas 37-39, exige el producto completo en web y móvil, prototipos y las secciones Implemented Landing Page Evidence, Implemented Frontend-Web Application Evidence, Implemented Native-Mobile Application Evidence, Implemented RESTful API and/or Serverless Backend Evidence, RESTful API documentation y Team Collaboration Insights. Las páginas 3-4 exigen además presentación PPTX/PDF y videos. Las capturas complementan la ejecución y la exposición; no sustituyen un producto completo ni el despliegue.

## Capturas obtenidas en esta revisión

Carpeta: `assets/evidence/implemented/`, relativa a la raíz del reporte.

| Evidencia | Archivo | Resultado |
|:--|:--|:--|
| Swagger y nombre de API | `swagger-live-overview.png` | UI oficial cargada desde Spring Boot local |
| Endpoints de energía | `swagger-live-energy-endpoints.png` | Cinco operaciones de Energy Monitoring visibles |
| Ejecución desde Swagger | `swagger-live-health-200.png` | GET /api/v1/health ejecutado con Try it out; HTTP 200 y status UP |
| Contrato OpenAPI | `openapi-live.json` | Descargado de /v3/api-docs, HTTP 200, OpenAPI 3.1.0, 100 operaciones |
| Login web | `webapp-live-login.png` | Formulario real sin credenciales visibles |
| Centro operativo | `webapp-live-home.png` | Cuenta de demostración autenticada y sede obtenida de la API |
| Consumo web | `webapp-live-energy.png` y `webapp-live-energy-full.png` | Página real con muestreo y datos persistidos |
| Gráfico y KPIs | `webapp-live-energy-chart.png`, `webapp-live-energy-metrics.png` | Recortes de componentes reales para mantener legibilidad en diapositivas |
| Dispositivos | `webapp-live-devices.png` | Tres equipos de demostración asignados a una sede y una habitación |
| Login Android | `android-live-login-20260906-065244.png` | Formulario Flutter real en español, sin credenciales visibles |
| Inicio Android | `android-live-home-20260906-065526.png` | 1370 W, 1.10 kWh, una sede y una habitación tras cargar la API |
| Consumo Android | `android-live-energy-20260906-065529.png` | KPIs de la cuenta local: 1.10 kWh, S/ 0.82 y 3/3 dispositivos |
| Tendencia Android | `android-live-energy-20260906-065620.png` | Gráfico de la aplicación real; datos sintéticos de demostración |
| Dispositivos Android | `android-live-devices-20260906-065544.png` | Los mismos equipos y habitación de demostración que en web |
| Consumo Android actualizado | `android-live-energy-20260906-071106.png` | KPIs tras recargar la aplicación contra el backend corregido |
| Potencia por habitación corregida | `android-live-energy-20260906-071137.png` | Laboratorio de software muestra 1370 W; imagen revisada visualmente |

No se interceptaron ni fabricaron respuestas HTTP en estas nuevas capturas. El script anterior `capture-hito1.cjs` sí utiliza respuestas simuladas; sus imágenes se conservan como evidencia de interfaz, no de persistencia real.

## Entorno y trazabilidad

- Backend: Spring Boot 4.0.6, `http://127.0.0.1:8080`, commit `69934f66a7ea15083f708205e4553c09b97dfbb3`.
- Base de datos: PostgreSQL 18.4 local y aislado, puerto 55432, base `energycore_evidence`. No se conectó a Neon ni se desplegó en la nube.
- Se comprobaron directamente en PostgreSQL 1 usuario, 3 dispositivos y 45 lecturas al realizar el recuento. El muestreo continuó mientras la vista de energía estuvo abierta.
- Web: build Angular existente, servido en `http://127.0.0.1:4300`; solo se configura la URL de API al servir JavaScript. Todas las llamadas /api/v1 se reenvían al backend real de 8080.
- Checkout web: commit `372d156edd5b5d76d6445a836601421319d49fe4`. Bundle `main-USX6GGWQ.js`, modificado el 05/09/2026 23:21:55, SHA-256 `A10BA1374573CBA694BCF7125CDB34899FB90125150F2778C412951D22176E26`. El rebuild en esta sesión fue bloqueado por `spawn EPERM`; no se atribuye un build nuevo al commit.
- Cuenta de prueba: EnergyCore Demo, dominio reservado `.test`. Dispositivos, potencia y transacciones de plan son fixtures de demostración local; no representan sensores físicos, ahorro comprobado ni cobros reales. El adaptador de pagos operó sin credenciales Stripe, en modo demo.
- Estas capturas prueban inicio de sesión, lectura de datos y recorrido de las pantallas mostradas. No equivalen a una prueba completa de todos los módulos.

Texto sugerido debajo de las imágenes: **Ejecución local real de Angular + Spring Boot + PostgreSQL. Datos de demostración; no son mediciones físicas ni evidencia de producción.**

## Pendientes y bloqueos comprobados

1. **Android - capturas completadas:** el usuario abrió Pixel_7 y ADB confirmó `emulator-5554` conectado. Se capturaron login, inicio, consumo, tendencia y dispositivos directamente con `adb shell screencap`, a 1080 × 2400 px. Las imágenes fueron inspeccionadas visualmente. Se comprobó el paquete en primer plano y la correspondencia del APK instalado; no son capturas de una web responsive. La discrepancia de potencia por habitación fue corregida y recapturada a las 07:11 America/Lima; se conserva el historial y se detalla la verificación abajo.
2. **Canva:** la carga directa de la captura local fue rechazada con `MCP tool call requires approval, but approval policy is never`. Ninguna captura nueva fue insertada ni guardada en el diseño. No se publicó contenido en servicios temporales para evitar ese permiso.
3. **Preferencias - 500 corregido:** se reprodujo una carrera al inicializar preferencias: cuatro de 24 GET simultáneos devolvieron 500 por violación de unicidad de `user_id`. Se implementó bloqueo transaccional de la fila padre User, compartido por GET de inicialización y PUT, sin cambiar el esquema ni el contrato REST. La regresión posterior aprobó 24 GET concurrentes y 24 GET/PUT concurrentes, con una fila por usuario, conservación de actualizaciones parciales, persistencia ES/EN/PT y aislamiento de cuentas. El recorrido de navegador login → inicio → PT → ES produjo siete respuestas 200 de preferencias, sin 500. Los 403 observados anteriormente sin autenticar son un asunto distinto: la web envía preferencias antes de tener sesión; no se modificó el frontend en esta corrección.
4. **Tecnologías:** la página 35 especifica Vue/PrimeVue y ASP.NET Core/C#. El producto reutilizado usa Angular/Spring Boot. La autorización de reutilización consta como decisión del equipo; falta confirmar explícitamente si también cubre esta diferencia tecnológica.
5. **Otros entregables:** siguen por completar la evidencia de despliegue público, las entrevistas reales (excluidas por el usuario), los enlaces de videos y la exportación final de la presentación en PPTX/PDF. No se verificaron como terminados en esta revisión.

Corrección de calidad para la presentación: los reportes históricos indican **83 casos descubiertos, 40 ejecutados y 43 omitidos**, no 83 pruebas ejecutadas. Esto se obtiene de 23 JUnit + 17 escenarios Cucumber ejecutados. No se volvieron a ejecutar las suites en esta sesión.

## Evidencia de la corrección de preferencias

- Resultado real: [`preferences-concurrency-smoke.json`](../assets/evidence/implemented/preferences-concurrency-smoke.json), ejecutado el 06/09/2026 a las 11:37:23 UTC.
- Código: `energycore-platform/scripts/smoke-ui-preferences.cjs --isolated-local-demo`. Requiere la base local aislada y crea cuentas de prueba `.test`; no apunta a servicios desplegados.
- `mvnw.cmd -o test-compile` concluyó con BUILD SUCCESS: 592 fuentes principales y 16 fuentes de pruebas compiladas. Compilar pruebas no significa ejecutar JUnit/Cucumber.
- Consulta directa de PostgreSQL para `GROUP BY user_id HAVING count(*) > 1`: cero filas.
- La corrección está en el árbol de trabajo local del backend, sobre `69934f66a7ea15083f708205e4553c09b97dfbb3`; todavía no se creó commit ni se publicó.

## Evidencia de la corrección de potencia

- Causa reproducida: el backend sumaba `EnergyReading.watts` a lo largo del día, tanto en `rooms` como en `topDevices`. La cifra por habitación inicialmente observada fue 265780 W y alcanzó 312360 W en la comprobación previa, aunque los tres dispositivos ON sumaban 1370 W.
- Cambio acotado en `EnergyMonitoringApplicationService`: `watts` representa la potencia configurada actual de los dispositivos ON. Equipos OFF, en mantenimiento o retirados no aportan potencia actual; sus lecturas conservan kWh/costos históricos. Se incluyen habitaciones activas aunque aún no tengan una muestra del día, y se conserva `Sin ambiente` para equipos sin ubicación. No cambian nombres de campos ni rutas REST; se documenta la semántica corregida en los recursos.
- `EnergyDashboardPowerTest`: cinco pruebas descubiertas y ejecutadas; antes de la corrección fallaban cuatro, después aprobaron cinco, sin omisiones. Cubren repetición de muestras, estados inactivos, ausencia de lecturas, ubicaciones vacías/desconocidas y cuenta vacía.
- `mvnw.cmd -o test-compile`: BUILD SUCCESS, 592 fuentes principales y 17 fuentes de pruebas. La ejecución normal mediante Surefire quedó bloqueada porque falta el plugin 3.5.5 en caché y Windows negó escritura en `.m2`. Las cinco pruebas sí se ejecutaron mediante el JUnit Platform Launcher disponible, sobre las clases compiladas. No se afirma que la suite completa haya pasado.
- Regresión real: [`energy-power-smoke.json`](../assets/evidence/implemented/energy-power-smoke.json), dos respuestas de la API local verificadas a las 12:09:54 UTC. Potencia global y por habitación: 1370 W; dispositivos: 120, 350 y 900 W. Script reproducible: `energycore-platform/scripts/smoke-energy-power.cjs --isolated-local-demo`.
- Confirmación visual: se reinició únicamente EnergyCore en el emulador, sin borrar sus datos, y se comprobó **1370 W** en Consumo por habitación. Captura `android-live-energy-20260906-071137.png`, SHA-256 `5AD2D3A3B3ACC1E125C56A356762E3AB2645A56FC9088CCB37260ECC046B0113`. Los kWh de demostración siguen aumentando normalmente entre capturas; no se fabricaron ni retocaron valores.
- Cambios locales sin commit, push ni despliegue. No se modificó la aplicación web ni el APK. Canva continúa bloqueado por el permiso de carga; ninguna de estas imágenes nuevas se ha insertado en el diseño.

Repetir la prueba por la vía estándar en PowerShell normal (inicia una nueva ejecución de pruebas, no un segundo servidor):

```powershell
Set-Location 'C:\JeanLoa\Universidad\Diseño de Experimentos de Ingeniería de Software\energycore-platform'
$env:JAVA_HOME = 'C:\Program Files\Android\Android Studio\jbr'
.\mvnw.cmd '-Dtest=EnergyDashboardPowerTest' test
```

## Colocación recomendada en la presentación existente

| Sección | Imagen y composición |
|:--|:--|
| Landing | Mantener la captura real `landing-desktop.png`, no una foto genérica |
| Autenticación web | `webapp-live-login.png`, completa y sin cortar el formulario |
| Dashboard | `webapp-live-energy-chart.png` arriba y `webapp-live-energy-metrics.png` debajo; también conservar la vista completa como respaldo |
| API / Swagger | `swagger-live-overview.png` grande y detalle `swagger-live-energy-endpoints.png`; `swagger-live-health-200.png` como evidencia de ejecución |
| Aplicación móvil | Usar `android-live-login-20260906-065244.png`, `android-live-home-20260906-065526.png` y `android-live-energy-20260906-065529.png` en tres marcos verticales; dispositivos y tendencia como respaldo. Archivos listos, inserción en Canva aún bloqueada |
| GitHub | Capturas existentes de ramas y Contributors, sin confundir el ícono de Git con evidencia de GitHub |

## Capturar Android cuando esté abierto

La aplicación debe estar visible en la pantalla que se quiere documentar. El script comprueba el dispositivo y el paquete en primer plano, y guarda una imagen con fecha y hora sin sobrescribir capturas anteriores.

```powershell
Set-Location 'C:\JeanLoa\Universidad\Diseño de Experimentos de Ingeniería de Software\energycore-report'
.\scripts\capture-android-evidence.ps1 -Screen login
# Navegar en EnergyCore a inicio, energía o dispositivos y repetir con:
# -Screen home / -Screen energy / -Screen devices
```

APK local: `energycore-mobile/flutter/build/app/outputs/flutter-apk/app-debug.apk`, 04/09/2026 08:05:40; SHA-256 `96289E1CC4EDEB5CBCCFDD997CD7D2C5033B05D52F34151EA2CFF0571B0F4F53`. El 06/09/2026 se extrajo el `base.apk` del paquete instalado `com.teralume.energycore_flutter` y su SHA-256 coincidió exactamente. Checkout móvil `0f545f0e5ff8dcbbbce645ad0ac325af27de6971`; no se generó un APK nuevo en esta sesión. El dispositivo reportó Android 17 y SDK 37. Las capturas se registraron entre 06:52 y 06:56 America/Lima; el reloj del emulador mostraba 11:52–11:56. El login está en tema claro; después de autenticar se cargó el tema oscuro de las preferencias de la cuenta. El endpoint de desarrollo del cliente es `http://10.0.2.2:8080/api/v1`.
