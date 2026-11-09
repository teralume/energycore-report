# Presentación de EnergyCore para AV2

La edición del 9 de noviembre de 2026 mantiene 27 diapositivas y llega hasta el Product Backlog de la sección 8.3.2. Para exponer esta edición, abre el [PowerPoint](../output/keynote/upc-pre-202610-1asi0732-9100-teralume-keynote-av2.pptx) o el [PDF exportado desde PowerPoint](../output/keynote/upc-pre-202610-1asi0732-9100-teralume-keynote-av2.pdf).

El diseño anterior conserva su enlace de Canva. La sincronización de esta revisión requiere reconectar la cuenta. [Diseño de Canva](https://www.canva.com/design/DAHYoDC_Zqc/BJZvKHIJtJGlH2Z6kJ0IjQ/edit)

## Evidencia para la exposición

| Páginas | Qué mostrar | Fuente |
| --- | --- | --- |
| 13–14 | Recorrido de la landing al login y navegación a registro y recuperación en el navegador. Las capturas corresponden al 9 de noviembre. | [ST-01](../assets/evidence/av2/public-navigation/st-01.json) |
| 18 | Resultados de backend, web, landing y Flutter. Cada registro identifica la ejecución, la fecha y el commit del componente. | [Extractos de GitHub Actions](../assets/evidence/av2-ci/execution-records-2026-11-09.json) |
| 20 | La prueba del dashboard comprueba potencia y energía con 200 lecturas preparadas. Las notas incluyen el comando Maven. | [Prueba JUnit](https://github.com/teralume/energycore-platform/blob/3f74d4780a34f96958c6fe4626400d44a9a9f918/src/test/java/com/teralume/energycore/energymonitoring/application/services/EnergyDashboardPowerTest.java) |
| 21–23 | Aceptación en septiembre, CI posterior y sondeos públicos de noviembre. El deploy condicional se omitió en el run del backend. | [Ejecución del monitor](https://github.com/teralume/energycore-report/actions/runs/42528712452) · [Lectura del 9 de noviembre](../assets/evidence/av2/public-navigation/public-probe.json) |
| 25–26 | Piloto propuesto y distribución del backlog en los sprints 5, 6 y 7. | [Capítulo VIII](../README.md) |

## Verificación de los archivos

Se revisaron las 27 páginas renderizadas y se contrastó el texto editable del PPT con la página correspondiente del PDF. Las cuatro capturas y láminas de evidencia de las páginas 13, 14, 18 y 23 se verifican contra los PNG del repositorio. El [registro de integridad](av2-keynote-export.json) conserva la procedencia y el SHA-256 de cada archivo.

Después de editar, exporta nuevamente las 27 páginas, revisa las imágenes y actualiza el registro. Ejecuta `python scripts/validate-av2-keynote.py` y `node scripts/build-av2-keynote.mjs`. La presentación utiliza DM Sans.
