# Kit de intercambio de auditorías UX — AV2

Este kit prepara una auditoría externa. No acredita que otro equipo haya evaluado EnergyCore ni que Teralume haya auditado otro producto. La autoevaluación de 6.3.3 conserva su origen interno.

**Fuente del formato:** Enunciado del Proyecto Final, Anexo D, páginas físicas 52–53 (rotuladas 50/53 y 51/53); la sección Validation Interviews de la página 33 remite a este anexo. Se conserva su estructura de identificación, tareas incluidas/excluidas, escala, tabla resumen y descripción de problemas. Los campos vacíos son parte de una plantilla, no resultados. Al completar la versión académica, colocar el contenido del equipo en azul y retirar los ejemplos del enunciado, como indica el anexo.

## Alcance y ficha de sesión

El grupo participante debe registrar startup, producto, NRC, nombres de auditores, fecha real, URL de su informe, versión evaluada (SHA/tag), navegador, plataforma y entorno. Intercambiar esos datos antes de iniciar. No usar cuentas personales ni credenciales productivas compartidas.

### UX Heuristics & Principles Evaluation

**Usability · Inclusive Design · Information Architecture**

| Campo del Anexo D | Registro de la evaluación |
|:--|:--|
| CARRERA | Ingeniería de Software |
| CURSO | Diseño de Experimentos de Ingeniería de Software |
| NRC | |
| PROFESORES | |
| AUDITOR: grupo que ejecuta la sesión | |
| CLIENTE(S): personas que participan en la sesión | |
| SITE o APP A EVALUAR | |

La identificación de participantes y sus imágenes se conserva en el documento académico con el acceso autorizado. Para un repositorio público usar códigos o referencias al documento restringido, salvo autorización específica para difusión pública; no incluir credenciales ni datos de contacto.

| Datos complementarios de trazabilidad | Registro |
|:--|:--|
| Startup, producto y grupo auditado | |
| Tipo de intercambio: auditoría realizada o recibida | |
| Fecha real y zona horaria | |
| URL del informe y del sitio/app | |
| Versión: SHA/tag y versión del cliente | |
| Navegador/dispositivo, plataforma y entorno | |
| Datos demostrativos y permisos autorizados | |

### Tareas a evaluar

El alcance se acuerda antes de la sesión. Para EnergyCore se proponen UX-01–03 de la tabla siguiente; cuando se evalúe el producto de otro equipo, adaptar las tareas a sus flujos reales y registrar el cambio de alcance. No trasladar al otro producto funcionalidades que no tenga.

| ID | Tarea incluida en esta evaluación | Plataforma/versión | Criterio de observación |
|:--|:--|:--|:--|
| | | | |

### Tareas no incluidas en esta versión de la evaluación

Registrar expresamente los flujos, plataformas y condiciones excluidos; una tarea no evaluada no se considera aprobada. La operación de actuadores reales y el uso de datos personales de producción quedan fuera del protocolo propuesto.

| Tarea o condición excluida | Motivo y límite de la conclusión |
|:--|:--|
| | |

## Tareas y criterios de observación

| ID | Tarea | Precondición | Éxito observable | Seguridad |
|:--|:--|:--|:--|:--|
| UX-01 | Localizar el consumo de un periodo y reconocer su unidad. | Entorno de prueba con lecturas semilla y usuario autorizado. | La persona encuentra el periodo, la unidad y el valor; registrar pasos, tiempo y errores. | Solo lectura; no atribuir lecturas semilla a sensores físicos. |
| UX-02 | Encontrar una sede, su habitación y un dispositivo asociado. | Jerarquía semilla documentada por el grupo auditado. | La persona identifica correctamente la relación y el estado visible. | No eliminar ni modificar dispositivos reales. |
| UX-03 | Crear una rutina de demostración y revisar su alcance antes de confirmar. | Cuenta de prueba y dispositivos simulados, sin actuadores reales. | La interfaz permite revisar alcance, cancelar y reconocer el resultado. | Si no existe entorno aislado, inspeccionar el formulario y cancelar; no contar ejecución remota como probada. |

## Procedimiento reproducible

1. Congelar la versión y completar ficha, accesos y datos semilla.
2. Inspeccionar cada tarea en 390, 768 y 1440 px; comprobar foco, teclado, nombres de controles, mensajes y recuperación.
3. Revisar las tres dimensiones del Anexo D: Usability, Inclusive Design e Information Architecture. Aplicar la heurística o principio pertinente y registrar solo lo observado, con captura y pasos. Clasificar cada problema con la escala 1–4 del anexo.
4. Consolidar duplicados y devolver el informe al otro grupo, conservando sus respuestas originales.
5. Repetir los pasos de los hallazgos corregidos en la nueva versión y registrar evidencia de cierre.

Los tamaños de pantalla y las comprobaciones siguientes son decisiones del protocolo de EnergyCore; el Anexo D exige el formato y las tres dimensiones, pero no establece esas resoluciones ni una certificación WCAG completa.

| Dimensión | Cómo clasificar el hallazgo | Observaciones propuestas para EnergyCore |
|:--|:--|:--|
| Usability | Indicar la heurística aplicable; el anexo ejemplifica libertad/control y consistencia/estándares. Las diez heurísticas de Nielsen sirven de referencia interna. | Estado del sistema, claridad de unidades, prevención de acciones equivocadas, cancelación y recuperación. |
| Inclusive Design | Indicar el principio de diseño inclusivo aplicable; el anexo ejemplifica proporcionar experiencias comparables. | Si la tarea puede comprenderse y realizarse con teclado, foco visible, nombres accesibles y alternativas textuales; registrar la condición realmente observada. |
| Information Architecture | Indicar el principio aplicable; el anexo ejemplifica facilidad de uso y de encontrar información. | Etiquetas comprensibles, ubicación del consumo y las rutinas, relación sede–habitación–dispositivo y caminos de navegación. |

## Escala de severidad

| Nivel | Significado del Anexo D | Prioridad de corrección |
|:--:|:--|:--|
| 1 | Problema superficial, poco frecuente o fácil de superar. | Corregir si existe tiempo disponible. |
| 2 | Problema menor, más frecuente o algo más difícil de superar. | Prioridad baja para la siguiente versión. |
| 3 | Problema mayor, frecuente o que el usuario no consigue resolver. | Prioridad alta. |
| 4 | Problema muy grave que impide continuar usando la herramienta. | Corregir antes del lanzamiento. |

El valor 0 de algunas listas internas de Nielsen significa «no se identificó un problema»; no se incorpora como hallazgo a esta tabla de severidad. Una ausencia de hallazgos solo puede declararse después de ejecutar y documentar el alcance, nunca a partir de una plantilla vacía.

## Tabla resumen

Mantener la estructura del Anexo D y relacionar cada fila con una descripción detallada. No copiar los problemas ilustrativos del enunciado ni inventar observaciones para llenar la tabla.

| # | Problema | Escala de severidad | Heurística/Principio violado |
|:--|:--|:--:|:--|
| | | | |

Una tabla sin observaciones representa un instrumento sin ejecutar, no cero defectos.

## Descripción de problemas

Duplicar la siguiente ficha únicamente para hallazgos observados. El número coincide con la tabla resumen; los campos de ruta, pasos y resultado complementan el formato para hacer reproducible la observación.

### PROBLEMA # — título descriptivo

| Campo | Registro |
|:--|:--|
| Severidad: 1–4 | |
| Heurística o principio violado y dimensión | |
| Problema: descripción del impacto observado | |
| Tarea, pantalla/ruta y versión | |
| Precondiciones y pasos para reproducir | |
| Resultado esperado y resultado observado | |
| Captura de pantalla que ilustra el problema | |
| Referencia/timing si existe video autorizado | |
| Recomendación | |

La captura debe mostrar la condición descrita, corresponder a la versión evaluada y ocultar datos no autorizados. Cuando no se haya observado la condición o falte la evidencia, no completar la ficha como si existiera un problema demostrado.

## Respuesta y acta

Por cada hallazgo recibido: indicar aceptado, mitigado, rechazado con sustento o incorporado al backlog; enlazar tarjeta, commit y nueva comprobación cuando existan. El acta identifica fecha, participantes, informe original, acuerdos y confirmación de recepción. Sin esos datos no se cierra la auditoría realizada/recibida de 6.4.
