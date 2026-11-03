# Guion y registro de validación de EnergyCore — AV2

Instrumento preparado el 03/11/2026. No contiene entrevistas ejecutadas. Se aplica al producto actual; el ensayo A/B del capítulo VIII tiene otro protocolo y otra muestra.

## Reclutamiento y preparación

Convocar entre tres y cinco adultos por segmento: responsables de hogares urbanos y responsables de pequeños negocios. La primera ronda prevista contiene tres de cada segmento. Registrar su relación con la administración de equipos/gastos y su experiencia previa con aplicaciones de consumo. Excluir integrantes del equipo de desarrollo de esta muestra de usuarios.

Antes de cada sesión comprobar las superficies públicas, la cuenta de prueba autorizada, los datos demostrativos y el cliente disponible. Anotar commit, navegador, sistema y versión. No crear cuentas ni compartir contraseñas en este documento. La rutina se prueba con datos aislados y sin equipos físicos; si no existe ese entorno, limitar la tarea a inspección y cancelación y declararlo en el resultado.

Cobertura propuesta: H01/H02 en Android y H03 en web; N01/N02 en web y N03 en Android. Cada persona evalúa Landing Page y VAL-01–03. Así se reservan tres sesiones por cliente y tres por segmento. Una plataforma sin acceso se registra como no evaluada y se reprograma; no se sustituye silenciosamente toda la cobertura móvil por web. No es una muestra para estimar diferencias estadísticas entre plataformas.

## Consentimiento y apertura

Texto para explicar antes de grabar: «Queremos observar cómo se entiende EnergyCore; estamos evaluando el producto. Puedes no responder o detener la sesión. Usaremos las observaciones para mejorar la aplicación y el informe del curso. La grabación, si la autorizas, se mostrará por Microsoft Stream con acceso académico. Confirma por separado si autorizas participar, grabar y publicar tu imagen y voz».

Registrar la respuesta y el alcance de cada autorización. No interpretar la presencia ante cámara como permiso de publicación. Registrar nombre, edad y distrito solicitados por el Enunciado únicamente con autorización; los datos de contacto para coordinar se mantienen fuera del repositorio. El acceso del docente al video se verifica antes de incluir el enlace en el informe. Si se retira el permiso, registrar la solicitud y suspender la difusión del material correspondiente.

Separar **difusión académica restringida** de **difusión pública en GitHub**. Usar códigos en el repositorio. Mantener nombres, edad, distrito y capturas identificables en un anexo académico con acceso restringido, salvo autorización expresa para publicación pública. El consentimiento para Stream académico no se extiende por defecto al README público.

## Sesión de 26 a 29 minutos

1. Contexto y consentimiento, 4 min. «¿Qué equipos y gastos eléctricos administras? ¿Cómo sabes hoy qué está consumiendo más?»
2. Landing Page, 3 min. «¿Para qué crees que sirve? ¿Qué esperarías poder hacer?» Pedir el texto o elemento en que basa su respuesta.
3. Tareas VAL-01–03, 12–15 min. Presentarlas de una en una, sin enseñar la ruta. Pedir que piense en voz alta. Dar ayuda solo cuando la solicite o se bloquee, anotando exactamente qué se indicó.
4. Comprensión y confianza, 4 min. «¿Qué información usarías para decidir? ¿Qué confirmarías antes de cambiar una rutina? ¿Qué dato no confiarías todavía?»
5. Cierre, 3 min. «¿Qué cambiarías primero? ¿En qué situación no usarías la aplicación?» Confirmar el uso autorizado de la grabación.

| ID | Consigna | Evidencia de comprensión |
|:--|:--|:--|
| VAL-01 | Encuentra el consumo del periodo mostrado y explícalo. | Periodo, cantidad y unidad; distinción entre energía, potencia y costo; percepción de la frescura del dato. |
| VAL-02 | Localiza el equipo de demostración y explica dónde está y su estado. | Relación sede–habitación–dispositivo; interpretación del estado; acción esperada si no se actualiza. |
| VAL-03 | Prepara una rutina para salir de casa/cerrar el negocio; revisa el alcance y detente antes de ejecutarla. | Equipos afectados, horario, consecuencias y cancelación. Guardar/ejecutar solo en entorno aislado previamente verificado. |

Tras cada tarea: facilidad de 1 (muy difícil) a 7 (muy fácil), seguida de «¿Qué parte te hizo dudar?». No inducir la respuesta «fácil» ni prometer ahorro económico. No pedir consumo, recibos ni credenciales personales.

## Ficha de sesión que debe completarse con hechos

| Campo | Qué registrar |
|:--|:--|
| Participante | Código H/N, segmento y datos autorizados exigidos por el Enunciado. Los cupos H01–H03/N01–N03 no son participantes reclutados. |
| Moderación | Nombre del entrevistador y del observador, si existe. |
| Fecha y entorno | Fecha/hora con zona, URL, cliente, versión/SHA, navegador o dispositivo, estado de red. |
| Datos de prueba | Nombres de sede, habitación, dispositivo y periodo disponibles; confirmar que son demostrativos. |
| Consentimiento | Participación, grabación, publicación, medio donde consta y restricciones. |
| Audiovisual | Captura autorizada, URL institucional, timing de inicio/fin en el video consolidado y duración real. |
| Incidencias | Caída del servicio, problema de cuenta, interrupción o limitación de plataforma. |

El Anexo C del Enunciado contempla 3–5 minutos editados por entrevista en un MP4 consolidado. Conservar por separado duración completa, extracto y correspondencia de timings. Identificar segmento, participante autorizado y fecha; comprobar el acceso privado en Stream. La edición puede quitar silencios y preparación, pero debe conservar errores, dudas y respuestas contrarias a la expectativa del equipo.

## Registro por tarea

Para cada tarea conservar: código, instante de inicio/fin, resultado, pasos relevantes, ayuda, error o retroceso, valoración 1–7, cita breve con timing y observación del moderador. Resultados posibles: éxito sin ayuda; éxito con ayuda; no completada; no evaluable por entorno. No transformar una tarea no evaluable en fracaso del participante. No excluir un fallo del producto para mejorar la tasa de éxito.

La tarea termina cuando se cumple el criterio, la persona abandona o el moderador la detiene por seguridad. Si alcanza cinco minutos sin completarse, ofrecer continuar con la siguiente; anotar tiempo y motivo. Este límite organiza una entrevista cualitativa y no sustituye el límite predeclarado del experimento.

## Síntesis y trazabilidad

Agrupar por segmento y tarea; reportar conteos con denominador, no porcentajes de población. Separar observación, declaración y propuesta de cambio. Un comentario no prueba una mejora. Para cada hallazgo incluir código, heurística, impacto, repetición, captura/timing y criterio de aceptación de la corrección. Conservar contradicciones entre participantes y verificar los cambios con una sesión posterior identificada.

Una sesión se incorpora al informe cuando existen registro, consentimiento aplicable, evidencia audiovisual accesible, resumen por tarea y vínculo a los hallazgos. La cantidad de páginas de este instrumento no acredita ejecución.
