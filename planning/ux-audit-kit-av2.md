# Kit de intercambio de auditorías UX — AV2

Este kit prepara una auditoría externa. No acredita que otro equipo haya evaluado EnergyCore ni que Teralume haya auditado otro producto. La autoevaluación de 6.3.3 conserva su origen interno.

## Alcance y ficha de sesión

El grupo participante debe registrar startup, producto, NRC, nombres de auditores, fecha real, URL de su informe, versión evaluada (SHA/tag), navegador, plataforma y entorno. Intercambiar esos datos antes de iniciar. No usar cuentas personales ni credenciales productivas compartidas.

## Tareas y criterios de observación

| ID | Tarea | Precondición | Éxito observable | Seguridad |
|:--|:--|:--|:--|:--|
| UX-01 | Localizar el consumo de un periodo y reconocer su unidad. | Entorno de prueba con lecturas semilla y usuario autorizado. | La persona encuentra el periodo, la unidad y el valor; registrar pasos, tiempo y errores. | Solo lectura; no atribuir lecturas semilla a sensores físicos. |
| UX-02 | Encontrar una sede, su habitación y un dispositivo asociado. | Jerarquía semilla documentada por el grupo auditado. | La persona identifica correctamente la relación y el estado visible. | No eliminar ni modificar dispositivos reales. |
| UX-03 | Crear una rutina de demostración y revisar su alcance antes de confirmar. | Cuenta de prueba y dispositivos simulados, sin actuadores reales. | La interfaz permite revisar alcance, cancelar y reconocer el resultado. | Si no existe entorno aislado, inspeccionar el formulario y cancelar; no contar ejecución remota como probada. |

## Procedimiento reproducible

1. Congelar la versión y completar ficha, accesos y datos semilla.
2. Inspeccionar cada tarea en 390, 768 y 1440 px; comprobar foco, teclado, nombres de controles, mensajes y recuperación.
3. Aplicar las diez heurísticas de Nielsen; severidad 0–4. Registrar solo lo observado, con captura y pasos.
4. Consolidar duplicados y devolver el informe al otro grupo, conservando sus respuestas originales.
5. Repetir los pasos de los hallazgos corregidos en la nueva versión y registrar evidencia de cierre.

El criterio de accesibilidad documentado no equivale a certificar conformidad WCAG completa.

## Registro de hallazgos

| ID | Ruta y versión | Pasos | Esperado | Observado | Heurística / criterio | Severidad | Evidencia | Recomendación |
|:--|:--|:--|:--|:--|:--|:--:|:--|:--|

Una tabla sin observaciones representa un instrumento sin ejecutar, no cero defectos.

## Respuesta y acta

Por cada hallazgo recibido: indicar aceptado, mitigado, rechazado con sustento o incorporado al backlog; enlazar tarjeta, commit y nueva comprobación cuando existan. El acta identifica fecha, participantes, informe original, acuerdos y confirmación de recepción. Sin esos datos no se cierra la auditoría realizada/recibida de 6.4.
