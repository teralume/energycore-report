# Presentación AV2: fuente visual y archivos

El diseño vigente está en [Canva](https://www.canva.com/design/DAHYoDC_Zqc/BJZvKHIJtJGlH2Z6kJ0IjQ/edit). Conserva 27 diapositivas y el alcance de AV2 hasta 8.3.2. El enlace conserva los permisos del propietario.

Archivos publicados:

- [PowerPoint editable](../output/keynote/upc-pre-202610-1asi0732-9100-teralume-keynote-av2.pptx): archivo editable validado que se importó para aplicar el diseño en Canva.
- [PDF](../output/keynote/upc-pre-202610-1asi0732-9100-teralume-keynote-av2.pdf): exportación del diseño final desde Canva, revisada página por página.
- [Registro de integridad](av2-keynote-export.json): hashes SHA-256 y procedencia de ambos archivos.

El diseño usa fondo marfil, verde oscuro, acentos lima y tipografía DM Sans. Se revisaron las 27 páginas y se comprobó que el texto del PowerPoint esté presente en la página correspondiente del PDF. El PDF fija la apariencia para exponer; PowerPoint requiere DM Sans para conservar la misma tipografía al editar.

## Actualizaciones posteriores

1. Editar el diseño vigente y mantener el límite de AV2. Las hipótesis, el piloto y el backlog propuestos no representan resultados ejecutados.
2. Exportar todas las páginas a PDF y PowerPoint; revisar visualmente las 27 páginas antes de reemplazar los archivos publicados.
3. Actualizar el registro de integridad con los hashes de los archivos revisados y su procedencia real.
4. Ejecutar `python scripts/validate-av2-keynote.py` y los controles del repositorio antes de publicar.

`node scripts/build-av2-keynote.mjs` verifica los archivos publicados. Ya no reconstruye AV2 a partir del PPT de TB1: esa generación antigua sobrescribía el diseño aprobado. Los entregables de AV1 y TB1 mantienen sus propios archivos.
