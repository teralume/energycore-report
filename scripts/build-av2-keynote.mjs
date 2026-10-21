import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
const workspaceDir=process.cwd();
const deps=path.join(process.env.USERPROFILE,'.cache/codex-runtimes/codex-primary-runtime/dependencies');
process.env.RUNTIME_NODE_MODULES=path.join(deps,'node/node_modules');
process.env.RUNTIME_NODE=path.join(deps,'node/bin/node.exe');
const {PresentationFile,FileBlob}=await import(pathToFileURL(path.join(deps,'node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs')));
const skill=path.join(process.env.USERPROFILE,'.codex/plugins/cache/openai-primary-runtime/presentations/26.1020.11348/skills/presentations');
const input=path.resolve('output/keynote/upc-pre-202610-1asi0732-9100-teralume-keynote-tb1.pptx');
const p=await PresentationFile.importPptx(await FileBlob.load(input));
// The import materializes theme defaults on empty runs. Use the source body font
// as their fallback, preserving explicit fonts on the imported visible runs.
const sourceFonts=JSON.parse(execFileSync(path.join(deps,'python/python.exe'),['scripts/extract-pptx-fonts.py',input],{encoding:'utf8'}));
for(const [index,slide] of p.slides.items.entries()) for(const shape of slide.shapes.items) {
 const family=(sourceFonts[`ppt/slides/slide${index+1}.xml`]?.[shape.id]??[]).find(f=>['DM Sans','DM Sans Bold','Georgia Pro Light'].includes(f))??'DM Sans';
 shape.text.style={typeface:family};
}
// Keep the three imported decorative panels inside the canvas for a valid package.
for(const n of [3,5,12]){const s=p.slides.items[n-1].shapes.items.find(s=>s.id==='3');const f=s.position;s.position={...f,top:Math.max(0,f.top),height:Math.min(f.height,1080-Math.max(0,f.top)),width:Math.min(f.width,1920-f.left),rotation:0};}
// Remove broken decorative icon frames already present in the source export.
for(const [n,ids] of [[1,['5']],[7,['2','3','4','5']],[8,['2']],[18,['2','3','4','5']],[19,['2','3']]])
 for(const id of ids){const s=p.slides.items[n-1].shapes.items.find(x=>x.id===id);s.fill='none';s.line={fill:'none',width:0};}
for(const s of p.slides.items[15].shapes.items) if(!s.text.toString()&&s.position.width<300){s.fill='none';s.line={fill:'none',width:0};}
const replace=(n,old,value)=>{const shapes=p.slides.items[n-1].shapes.items; const s=shapes.find(s=>s.text?.toString()===old)??shapes.find(s=>s.text?.toString().includes(old)); if(!s) throw new Error(`Missing text ${n}: ${old}`); s.text.replace(old,value);};
replace(1,'Equipo Teralume · NRC 9100 · TB1','Equipo Teralume · NRC 9100 · AV2');
replace(2,'TRABAJO PARCIAL · PRESENTACIÓN DEL STARTUP','AVANCE 2 · EQUIPO TERALUME');
replace(7,'Alcance acumulativo del TB1','Producto base para AV2');
replace(9,'REQUIREMENTS SPECIFICATION · TB1','REQUISITOS · LÍNEA BASE ACUMULATIVA');
replace(17,'23','28');
replace(17,'17/60','60/60');
replace(17,'escenarios BDD ejecutados','escenarios BDD aprobados');
replace(17,'0','109');
replace(17,'fallos reportados en la última ejecución registrada','pruebas de producto aprobadas');
replace(17,'43 escenarios BDD continúan omitidos y se muestran como deuda verificable; no se contabilizan como aprobados.','Línea base del 05/10/2026: 88 backend + 5 web + 5 landing + 11 Flutter. CI consultado el 21/10/2026.');
replace(19,'83 casos descubiertos: 40 ejecutados y 43 omitidos.','88 pruebas backend aprobadas: 28 JUnit y 60 escenarios Cucumber.');
replace(19,'Las 5 pruebas nuevas de potencia aprobaron en una ejecución separada.','CI del mismo commit consultado el 21/10/2026; no se presenta como una nueva ejecución local.');
const note='Fuente: README.md, capítulos VI–VIII; Enunciado.pdf, tercer hito, pp. 42–43. Registro técnico: assets/evidence/implemented/av2-review-2026-10-21.json. Los resultados históricos conservan su fecha; no se atribuye una nueva ejecución completa.';
p.slides.items[16].speakerNotes.text=note;
p.slides.items[18].speakerNotes.text=note;
// Flat text slides retain the existing purple canvas and reference typography.
function textbox(slide,text,x,y,w,h,size,font='DM Sans',color='#FFFFFF'){
 const s=slide.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 s.text=text; s.text.style={typeface:font,fontSize:size,color}; return s;
}
function add(title,rows,source){
 const s=p.slides.add(); s.background.fill='#34354F';
 textbox(s,title,100,75,1690,130,76,'Georgia Pro Light');
 rows.forEach((row,i)=>{textbox(s,row[0],105,245+i*205,1610,55,34,'DM Sans Bold','#99D7B7');textbox(s,row[1],105,305+i*205,1610,115,35);});
 s.speakerNotes.text=source+'\nAlcance AV2: el contenido experimental termina en 8.3.2. No se muestran resultados de experimentos ni validaciones no realizadas.';
 return s;
}
add('Alcance de Avance 2',[
 ['VERIFICACIÓN Y DEVOPS','Pruebas, revisión estática, auditorías UX y monitoreo; la evidencia técnica conserva su procedencia.'],
 ['PLANIFICACIÓN EXPERIMENTAL','Preguntas, hipótesis, diseño de medición y backlog To-Be hasta 8.3.2.'],
 ['LÍMITE DE ESTA PRESENTACIÓN','No incluye ejecución To-Be, análisis de resultados, shareback ni pre-launch de TB2.']
], 'Enunciado.pdf, pp. 42–44. La estructura detallada de AV2 termina en 8.3.2; se aplica ese límite ante la discrepancia con los objetivos generales.');
add('Revisión técnica trazable',[
 ['CI Y REVISIONES','Últimas ejecuciones consultadas: cinco repositorios con resultado success. Los cuatro repositorios del producto coinciden con su commit local.'],
 ['HALLAZGOS CONCRETOS','Producción conserva ddl-auto=update y un origen localhost en el CORS predeterminado. Son observaciones abiertas, no correcciones desplegadas.'],
 ['ALCANCE DE LA REVISIÓN','Inspección automática del código. La aprobación humana por pares y la auditoría de otro grupo no se sustituyen con esta revisión.']
], 'assets/evidence/implemented/av2-review-2026-10-21.json; README.md, 6.2 y 6.4.');
add('Monitoreo reproducible',[
 ['COMPROBACIÓN PÚBLICA DEL 21/10/2026','API health: 200 · OpenAPI: 200 · Web Application: 200. Solo solicitudes de lectura, sin cuentas ni datos personales.'],
 ['DETECCIÓN Y EVIDENCIA','El monitor valida status UP, contrato OpenAPI y HTML; termina con fallo ante una respuesta incorrecta y guarda JSON.'],
 ['AUTOMATIZACIÓN PREPARADA','Workflow manual y programado cada 6 horas. Su activación remota requiere publicar el cambio; no se afirma un SLA medido.']
], 'assets/evidence/implemented/av2-monitoring-2026-10-21.json; scripts/monitor-public-surfaces.py; .github/workflows/monitoring.yml.');
add('Pregunta e hipótesis experimental',[
 ['PREGUNTA','¿Una recomendación con causa y acción ayuda a identificar un consumo anómalo y decidir qué hacer?'],
 ['COMPARACIÓN PROPUESTA','Control: dashboard actual. Tratamiento: recomendación accionable con explicación, impacto y confirmación segura.'],
 ['HIPÓTESIS POR CONTRASTAR','El tratamiento reduce el tiempo de la tarea sin aumentar errores. No se afirma ahorro energético ni una mejora ya demostrada.']
], 'README.md, 8.1 y 8.2. Las hipótesis y la comparación son propuestas, no resultados.');
add('Diseño y medición propuestos',[
 ['VARIABLES','Tiempo de tarea, éxito y errores. Registrar variante, plataforma, segmento y experiencia previa sin identificar a la persona.'],
 ['PILOTO PROPUESTO','24 participantes para depurar tareas y estimar parámetros. La muestra confirmatoria depende de variabilidad y efecto mínimo.'],
 ['CONTROL Y ÉTICA','Mismas tareas y datos semilla; asignación consistente; consentimiento, minimización de datos y detención ante riesgo.']
], 'README.md, 8.2. No se afirma reclutamiento, ejecución del piloto o resultado estadístico.');
add('To-Be Product Backlog',[
 ['13 HISTORIAS · 53 STORY POINTS','Historias de explicación, acción segura, alcance, recuperación, idempotencia y frescura; tareas técnicas de asignación y eventos.'],
 ['CRITERIOS DE ACEPTACIÓN','Cada historia conserva su resultado verificable. Ninguna supera 5 SP; las estimaciones no equivalen a implementación terminada.'],
 ['PLANIFICACIÓN Y TRAZABILIDAD','Trello: energycore-product-backlog-y-sprint-planning. Reporte: 8.3.1 User Stories y 8.3.2 Product Backlog.']
], 'README.md, 8.3.1 y 8.3.2; https://trello.com/b/kFru7uh2/energycore-product-backlog-y-sprint-planning');
// Keep the original contact slide last.
p.slides.items.find(s=>s.shapes.items.some(x=>x.text?.toString()==='Contacto')).moveTo(p.slides.items.length-1);
p.slides.items.find(s=>s.shapes.items.some(x=>x.text?.toString()==='Alcance de Avance 2')).moveTo(2);
await fs.mkdir('tmp/av2-deck',{recursive:true});
await fs.mkdir('output/keynote',{recursive:true});
await fs.mkdir('tmp/av2-validated',{recursive:true});
const candidatePath=path.resolve('tmp/av2-deck/candidate.pptx');
await (await PresentationFile.exportPptx(p)).save(candidatePath);
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')));
const finalPath=path.resolve(`tmp/av2-validated/validated-${Date.now()}.pptx`);
const result=await finalizePresentation({workspaceDir,candidatePath,finalPath,
 pythonExecutable:path.join(deps,'python/python.exe'),
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','18288000,10287000'],
 fontPolicy:{basis:'reference',families:['DM Sans','DM Sans Bold','Georgia Pro Light'],referencePath:input,referenceSha256:crypto.createHash('sha256').update(await fs.readFile(input)).digest('hex')},
 explicitTotalSlideCount:27,verifyArtifactToolImport:true,
 receiptPath:path.resolve(`tmp/av2-deck/validation-${Date.now()}.json`)});
console.log(JSON.stringify(result));
await fs.copyFile(finalPath,path.resolve('output/keynote/upc-pre-202610-1asi0732-9100-teralume-keynote-av2.pptx'));
