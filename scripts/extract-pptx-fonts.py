"""Inspect reference typography, without editing the PowerPoint package."""
import json
import sys
from zipfile import ZipFile
from xml.etree import ElementTree as E

ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
with ZipFile(sys.argv[1]) as archive:
    result={}
    for name in archive.namelist():
        if name.startswith('ppt/slides/slide') and name.endswith('.xml'):
            result[name]={s.find('.//p:cNvPr',ns).get('id'):
                          [f.get('typeface') for f in s.findall('.//a:latin',ns)]
                          for s in E.fromstring(archive.read(name)).findall('.//p:sp',ns)}
print(json.dumps(result))
