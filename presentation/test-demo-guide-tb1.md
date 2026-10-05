# Guía de demostración de tests — EnergyCore TB1

Comprobación local: **05/10/2026**.

## Resultados comprobados

| Repositorio | Resultado | Cobertura principal |
|:--|:--|:--|
| energycore-platform | 28 JUnit + 60 escenarios BDD aprobados; 0 omitidos; 0 fallos | Dominio, aplicación, seguridad, eventos, HTTP, H2 y aceptación |
| energycore-webapp | 3 archivos, 5 tests aprobados | App, título, estadísticas y contrato HTTP de login |
| energycore-website | 5 tests aprobados | Accesibilidad, assets, URL de login y servidor HTTP |
| energycore-mobile/flutter | 11 tests aprobados | Modelos, permisos, rutinas, idiomas, widget e interfaz iOS |
| RunnerTests.swift | 1 XCTest disponible | Persistencia y borrado de sesión en iOS Keychain; requiere macOS |

## 1. Backend: mostrar un test unitario

Archivo: energycore-platform/src/test/java/com/teralume/energycore/energymonitoring/application/services/EnergyDashboardPowerTest.java.

El método repeatedSamplesAccumulateEnergyButNotCurrentPower demuestra que las muestras históricas acumulan energía, pero la potencia actual no se suma dos veces.

    Set-Location "C:\JeanLoa\Universidad\Diseño de Experimentos de Ingeniería de Software\energycore-platform"
    $env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
    .\mvnw.cmd -Dtest=EnergyDashboardPowerTest#repeatedSamplesAccumulateEnergyButNotCurrentPower test

Resultado esperado: Tests run: 1, Failures: 0, Errors: 0 y BUILD SUCCESS.

Gate completo del producto:

    Set-Location "C:\JeanLoa\Universidad\Diseño de Experimentos de Ingeniería de Software\energycore-report"
    .\scripts\run-energycore-quality-gate.ps1

Suite completa del backend:

    .\mvnw.cmd test

Clases JUnit y propósito:

- EnergyDashboardPowerTest: potencia actual, energía histórica y totales por habitación.
- RoutineSchedulePolicyServiceTest: rutinas diarias, semanales, por intervalo y de una sola ejecución.
- DevicePairingCatalogServiceTest: normalización y rechazo de códigos de emparejamiento.
- AccessProfilePolicyServiceTest: permisos de Owner y Guest.
- AccessAuthorizationServiceTest: autorización por permiso y acceso a la propia cuenta.
- PasswordHashingServiceTest: BCrypt genera un hash y valida la contraseña original.
- AuthApplicationServiceTest: recuperación, token de un solo uso y cambio de contraseña.
- BillingCommandServiceImplTest: checkout, eventos y cancelación al final del ciclo.
- MonthlyConsumptionReportSchedulerServiceTest: reporte mensual habilitado o deshabilitado.
- UserRegisteredEventHandlerTest y ReportingIntegrationEventHandlerTest: traducción de eventos entre bounded contexts.

## 2. Backend: mostrar BDD/Cucumber

    .\mvnw.cmd -Dtest=CucumberRunnerTest test

Los ocho archivos feature ejecutan los 60 escenarios Given-When-Then contra Spring Boot con H2. Cubren registro, login, JWT, planes, checkout, sedes, habitaciones, dispositivos, grupos, rutinas, modos, lecturas, dashboard, preferencias, reglas, alertas, metas, reportes, soporte y mantenimiento. El resultado esperado es 60 ejecutados, 0 omitidos, 0 fallos y 0 errores.

## 3. WebApp: estadísticas energéticas

Archivo: energycore-webapp/src/app/energy-monitoring/domain/services/energy-statistics.service.spec.ts.

Comprueba que 900 W y 100 W produzcan total 1000 W, promedio 500 W, máximo Office HVAC, una lectura alta y una normal.

    Set-Location "C:\JeanLoa\Universidad\Diseño de Experimentos de Ingeniería de Software\energycore-webapp"
    npx ng test --watch=false --include=src/app/energy-monitoring/domain/services/energy-statistics.service.spec.ts

Suite completa:

    npm run test:ci

Los otros tests comprueban que Angular cree la aplicación, establezca el título y que AuthApiService envíe un POST a /api/v1/auth/sign-in con las credenciales correctas.

## 4. Landing Page

    Set-Location "C:\JeanLoa\Universidad\Diseño de Experimentos de Ingeniería de Software\energycore-website"
    npm test

Valida estructura accesible, enlace de ingreso, conexión entre HTML/CSS/JS/assets, URL /iam/login y un servidor HTTP temporal que responde 200 para la página, estilos y script.

Solo el funcional:

    npm run test:functional

## 5. Flutter

    Set-Location "C:\JeanLoa\Universidad\Diseño de Experimentos de Ingeniería de Software\energycore-mobile\flutter"
    flutter test test\domain_models_test.dart --plain-name "goal progress is normalized between zero and one"

Ese test demuestra que el progreso de una meta queda limitado entre 0 y 1.

Suite completa:

    flutter test

También prueba estados de dispositivos, preferencias, permisos Owner/Guest, rutinas, modos, tres idiomas, el widget de marca y autenticación con apariencia iOS.

## 6. iOS nativo

RunnerTests.swift escribe una sesión sintética en Keychain, la recupera desde otra instancia, la reemplaza y confirma que logout la elimina. Solo se ejecuta en macOS con Xcode:

    cd energycore-mobile/flutter/ios
    xcodebuild test -workspace Runner.xcworkspace -scheme Runner -sdk iphonesimulator -destination 'platform=iOS Simulator,name=iPhone 16'

En Windows, ios_auth_test.dart comprueba la interfaz y el canal de almacenamiento con TargetPlatform.iOS; no sustituye el XCTest nativo.

## Respuestas breves para la exposición

**Unitario:** prueba una regla aislada, como calcular potencia o normalizar progreso.

**Integración:** prueba componentes conectados, como Angular con el contrato HTTP o Spring con H2 y repositorios.

**Funcional o aceptación:** observa el comportamiento externo, como servir la Landing por HTTP o ejecutar Given-When-Then contra la API.

**¿Cuántas pruebas pasan?** El gate ejecuta 109 pruebas automatizadas: 88 en backend —28 JUnit y 60 Cucumber—, 5 en Angular, 5 en la Landing Page y 11 en Flutter. La ejecución comprobada terminó sin fallos ni escenarios omitidos.

**¿Qué hace GitHub Actions?** En cada push o pull request instala dependencias, ejecuta pruebas, construye el producto y publica artefactos. El despliegue desde main solo ocurre si la variable de despliegue está habilitada y el job de verificación termina correctamente.
