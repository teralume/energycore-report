# Auditoría de experiencia de usuario: EnergyCore

**Equipo evaluador:** ShiftTech Solutions  
**Producto evaluado:** EnergyCore, de Teralume  
**Fecha de revisión:** 9 de noviembre de 2026  
**Tipo de evaluación:** revisión exploratoria de experiencia de usuario y recorridos funcionales seleccionados.

## Alcance y método

Se revisó el reporte proporcionado por el equipo y se realizaron pruebas exploratorias en la landing page y las aplicaciones web y móvil, utilizando una cuenta de prueba. Se crearon una sede, una habitación y un dispositivo identificados como prueba. Los resultados reflejan los recorridos observados, no una evaluación exhaustiva ni una prueba con usuarios.

| Producto | Dirección o archivo | Estado de la revisión |
|---|---|---|
| Landing page | https://teralume.github.io/energycore-website/ | Responde con HTTP 200; se probaron el idioma, una pestaña de público, una pregunta frecuente y el acceso desde un plan. |
| Aplicación web | https://university-energycorp.web.app/iam/login | Se probó el acceso, la creación de sede, habitación y dispositivo, la vista de consumo y un formulario de rutina. |
| Aplicación móvil Android | EnergyCore-Android.apk | Se revisaron el acceso al panel, la navegación por energía, dispositivos, espacios y alertas, y la visualización de datos creados desde la web en un emulador Pixel 6. |

## Escala de prioridad

| Nivel | Interpretación |
|---|---|
| Alta | Impide una tarea esencial o expone al usuario a un problema importante. |
| Media | Dificulta una tarea o deja información relevante sin acceso claro. |
| Baja | Genera confusión limitada o reduce la claridad, pero permite continuar. |

## Observaciones de la landing page

### L-01. No se identifica un enlace al acuerdo de servicio en la navegación pública

- **Prioridad sugerida:** media.
- **Ubicación:** navegación principal y pie de página.
- **Comprobación:** consultar la página pública y revisar los destinos de sus enlaces.
- **Resultado observado:** los enlaces inspeccionados conducen a secciones de la landing, al acceso de la aplicación o a la universidad; no se identificó un enlace a términos y condiciones o al acuerdo de servicio.
- **Impacto:** una persona interesada en los planes podría no encontrar desde la landing las condiciones aplicables antes de continuar.
- **Recomendación:** publicar un enlace visible al acuerdo de servicio y comprobar que conduzca al texto correspondiente. El reporte del equipo sí describe un acuerdo académico.
- **Límite:** no se verificó si existe un enlace equivalente dentro de la aplicación autenticada.

### L-02. La selección de un plan no se distingue en el destino del enlace

- **Prioridad sugerida:** baja.
- **Ubicación:** botones de los planes Starter, Professional y Enterprise.
- **Comprobación:** revisar los destinos declarados de los tres enlaces y seleccionar «Probar Professional».
- **Resultado observado:** los tres apuntan a la misma dirección de inicio de sesión, sin identificar el plan en la URL. Al seleccionar Professional se mostró el inicio de sesión sin una indicación visible del plan elegido.
- **Impacto potencial:** después de autenticarse, el usuario podría necesitar volver a elegir el plan y perder el contexto de su selección inicial.
- **Recomendación:** comprobar el recorrido posterior al inicio de sesión y, si no conserva la elección, informar que deberá seleccionarse nuevamente o preservar la intención de forma segura.
- **Límite:** no se ha probado el comportamiento posterior al acceso; por ello el impacto es una hipótesis y no un fallo confirmado de suscripción.

## Aspectos positivos observados

- La landing explica la propuesta de valor, presenta capacidades, planes y preguntas frecuentes.
- El documento HTML declara una opción de salto al contenido principal y etiquetas para los controles de idioma y navegación.
- El acceso a la aplicación web está enlazado desde la landing.
- El selector de español de la landing actualizó el contenido visible. La pestaña «Profesionales» y la expansión de una pregunta frecuente respondieron a la interacción.
- La cuenta de prueba pudo acceder a la aplicación web. La sede, la habitación y el dispositivo de prueba se crearon y se reflejaron en el panel. El idioma de la vista de dispositivos cambió a inglés y regresó a español.
- La aplicación móvil abrió y presentó los campos de correo y contraseña, además de las opciones de recuperación de contraseña y creación de cuenta. Estas dos últimas opciones no se han probado.
- El panel móvil mostró indicadores y opciones de navegación. La sede, habitación y dispositivo creados desde la web aparecieron en la aplicación móvil con la misma cuenta; la pantalla de asignaciones mostró el dispositivo vinculado a la habitación.

## Hallazgos de la aplicación web

### W-01. La validación de sede vacía presenta un mensaje genérico

- **Prioridad sugerida:** media.
- **Ubicación:** Espacios → Sedes → Crear sede.
- **Pasos:** abrir el formulario, dejar vacío el nombre y seleccionar «Crear sede».
- **Resultado observado:** apareció «No se pudo crear la sede»; el mensaje no explicó qué campo debía corregirse. En la vista observada, la notificación quedó parcialmente cubierta por el formulario.
- **Impacto:** el usuario no recibe una orientación clara para completar la operación y puede interpretar el problema como una falla del servicio.
- **Recomendación:** indicar junto al nombre que es obligatorio, evitar enviar el formulario con datos incompletos y mostrar la notificación por encima del diálogo o dentro de él.

### W-02. El estado vacío de consumo sugiere una acción ya realizada

- **Prioridad sugerida:** baja.
- **Ubicación:** Inicio → Consumo energético → Consumo por habitación.
- **Pasos:** crear una sede, una habitación y un dispositivo asignado; mantener el dispositivo apagado y consultar consumo.
- **Resultado observado:** aunque el dispositivo figuraba asignado a la habitación, la sección mostró «Sin datos por habitación» y sugirió asignar habitaciones a los dispositivos.
- **Impacto:** el mensaje puede hacer creer que la asignación falta, cuando la ausencia observada corresponde a que aún no hay lecturas de consumo.
- **Recomendación:** distinguir entre «no hay dispositivos asignados» y «hay dispositivos asignados, pero todavía no hay lecturas».

## Hallazgos de la aplicación móvil

### M-01. La pestaña de habitaciones aparece truncada y su nombre no refleja claramente su contenido

- **Prioridad sugerida:** media.
- **Ubicación:** Más → Espacios → pestaña central.
- **Pasos:** abrir Espacios y seleccionar la pestaña central, visible como «Consumo por ha».
- **Resultado observado:** el título aparece truncado en el emulador; la pantalla presenta habitaciones y opciones para administrarlas.
- **Impacto:** el nombre visible sugiere una consulta de consumo y puede dificultar que el usuario encuentre la gestión de habitaciones.
- **Recomendación:** utilizar una etiqueta breve, por ejemplo «Habitaciones», y verificar que se muestre completa en pantallas de distintos tamaños.
- **Evidencia:** [Pantalla de habitaciones](auditoria-energycore-evidencias/movil-etiqueta-habitaciones.png).

### M-02. El botón flotante de alertas se superpone al contenido

- **Prioridad sugerida:** baja.
- **Ubicación:** Alertas → Bandeja.
- **Pasos:** abrir la bandeja con varias notificaciones y revisar las tarjetas que aparecen cerca de la parte inferior.
- **Resultado observado:** el botón «Nueva alerta» se muestra por encima de parte del texto de una tarjeta de notificación.
- **Impacto:** puede dificultar la lectura o el acceso al contenido de la tarjeta en esa posición.
- **Recomendación:** reservar espacio para el botón o ajustar su ubicación para que el contenido pueda desplazarse sin quedar cubierto.
- **Evidencia:** [Bandeja de alertas](auditoria-energycore-evidencias/movil-alertas.png).

## Alcance pendiente de comprobación

- **Landing:** navegación completa por teclado y presentación en distintos tamaños.
- **Web:** registro de cuenta, ejecución de rutinas, alertas, controles de dispositivos, reportes y demás recorridos no mencionados como probados.
- **Android:** creación y edición completas en todos los módulos, permisos, ejecución de rutinas y comportamiento en dispositivos físicos y otros tamaños de pantalla. La revisión realizada no acredita el funcionamiento completo ni la seguridad del APK.

## Evidencia técnica consultada

- Landing y ruta de acceso: respuesta HTTP 200 obtenida el 9 de noviembre de 2026.
- HTML público de la landing: enlaces de planes con destino común al inicio de sesión; controles de idioma y pestañas declarados.
- APK: identificador `com.teralume.energycore_flutter`, versión declarada `1.0.0`, versión mínima Android API 24. Los metadatos no constituyen una verificación de seguridad.
- Reporte académico facilitado por Teralume: funcionalidades previstas y descripción del acuerdo de servicio.
