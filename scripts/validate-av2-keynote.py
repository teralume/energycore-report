"""Check the exported AV2 deck's scope and stale test claims."""
import json
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as E

root=Path(__file__).resolve().parents[1]
folder=root/'output/keynote'
file=folder/'upc-pre-202610-1asi0732-9100-teralume-keynote-av2.pptx'
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
with ZipFile(file) as archive:
    names=sorted((n for n in archive.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')),
                 key=lambda n:int(n.split('slide')[-1][:-4]))
    slides=[' '.join(x.text or '' for x in E.fromstring(archive.read(n)).findall('.//a:t',ns)) for n in names]
assert len(slides)==27
assert 'AV2' in slides[0]
assert 'Alcance de Avance 2' in slides[2]
text='\n'.join(slides)
for forbidden in ('8.3.3','8.3.4','8.4.1','8.5.1','8.6.1','17/60','43 escenarios BDD continúan omitidos'):
    assert forbidden not in text,forbidden
for required in ('8.3.2','53 STORY POINTS','Monitoreo reproducible','60/60','109','24 participantes'):
    assert required in text,required
print(json.dumps({'slides':len(slides),'scope':'AV2 through 8.3.2','stale_test_claims':0}))
