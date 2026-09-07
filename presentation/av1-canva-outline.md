# EnergyCore — presentación AV1

Formato: presentación académica 16:9, 16 diapositivas. Identidad Teralume/EnergyCore: negro verdoso, grafito y esmeralda (`#22C55E`, `#15803D`, `#080D09`, `#121A14`, `#F3F6F2`), acento ámbar puntual (`#F59E0B`), sin azul. Tipografía geométrica, alto contraste, iconografía de energía y retícula tecnológica. Usar poco texto, diagramas claros y áreas preparadas para colocar las capturas reales del repositorio.

## 1. Portada

**EnergyCore** — Inteligencia energética para cada espacio. Teralume. Curso Diseño de Experimentos de Ingeniería de Software, NRC 9100, docente Alex Humberto Sánchez Ponce, AV1. Jean Franck Loa Rojas — U20241E406.

## 2. Problema y oportunidad

La energía se consume sin una vista unificada de dispositivos, espacios, horarios y costos. Usuarios domésticos, pequeños negocios y responsables operativos necesitan detectar consumo, actuar y automatizar desde un solo sistema.

## 3. Segmentos y necesidades

Tres columnas: hogares inteligentes, pequeños negocios y operadores de espacios. Necesidades compartidas: visibilidad, control, alertas, metas y decisiones comprensibles.

## 4. Propuesta de valor

EnergyCore conecta consumo en vivo, dispositivos, sedes, habitaciones, rutinas, alertas, metas y reportes. Mensaje central: “See the energy. Shape what happens next.”

## 5. Supuestos y enfoque experimental

Mapa hipótesis → señal → experimento → decisión. Declarar que las entrevistas y resultados empíricos siguen pendientes; no fabricar métricas ni testimonios. Mostrar los eventos instrumentables para el piloto.

## 6. Experiencia completa

Flujo visual: Landing Page → login/registro/recuperación → dashboard → selección de sede → consumo energético → control/automatización → alerta/reporte. Incluir recuperación por pérdida de conexión con acción Reintentar.

## 7. Sistema de diseño

Paleta esmeralda/grafito, tema claro-oscuro según sistema, Space Grotesk/Manrope, Lucide Angular en web y Material Icons en Flutter. Accesibilidad: foco visible, contraste, movimiento reducido y responsive 390/768/1024/1440.

## 8. Landing Page

Mostrar hero 3D, mascota EnergyCore, brillo y microanimaciones, capacidades, audiencias, planes Starter/Professional/Enterprise y CTA “Probar EnergyCore” dirigido al login. Reservar un marco grande para la captura real.

## 9. Autenticación web

Login, registro y recuperación en español/inglés/portugués. Destacar el retorno explícito al login y la navegación por teclado. Reservar dos marcos para capturas reales.

## 10. Centro operativo y energía

Dashboard con guía de instalación, sede activa, KPIs, consumo en vivo, potencia, costos estimados, ranking por dispositivo y consumo por habitación. Aclarar que la captura funcional local usa datos de demostración controlada; Neon será la persistencia productiva.

## 11. Aplicación Flutter Android

Paridad funcional con Angular: IAM, energía, dispositivos, grupos, rutinas, modos, espacios, alertas, metas, reportes, soporte, planes y cuenta. Tema de sistema, ES/EN/PT, sesión cifrada y estado sin conexión con Reintentar.

## 12. Arquitectura DDD

Diagrama Landing/Angular/Flutter → REST API Spring Boot → PostgreSQL Neon. Bounded contexts: IAM, Billing, Workplace, Device Control, Energy Monitoring, Notifications, Reporting y Service Management. Capas Domain, Application, Infrastructure e Interfaces/Presentation.

## 13. API y Swagger

100 operaciones declaradas en controladores Spring MVC. Swagger UI en `/swagger-ui.html` y OpenAPI JSON en `/v3/api-docs`. JWT, BCrypt, Resources, assemblers y command/query services. La evidencia de ejecución pública se agrega después del despliegue.

## 14. Calidad y verificación

Backend: 83 pruebas descubiertas, 0 fallos, 43 escenarios Cucumber omitidos por el runner temporal. Angular: build productivo exitoso en la línea base, TypeScript actual sin errores y advertencias de presupuesto; el último rebuild quedó bloqueado por `spawn EPERM` del host. Flutter: `dart analyze` sin incidencias y `flutter test` aprobado en terminal normal.

## 15. GitFlow y entrega

Cinco repositorios públicos en `github.com/teralume`: report, platform, webapp, mobile y website. Flujo `feature/*` → `develop` → `release/av1` → `main`, Conventional Commits y merges `--no-ff`. `main` espera la verificación pública de Cloud Run, Neon y Firebase.

## 16. Cierre y siguientes pasos

Estado: experiencia y evidencia AV1 preparadas; publicación de ramas completada. Próximos pasos: ejecutar Cloud Run con Neon, publicar ambos sitios Firebase, capturar Android/Swagger, completar entrevistas reales, aprobar `release/av1` y grabar About-the-Product. Cierre: “Medir. Entender. Actuar.”
