// Canva is the visual authority. Never regenerate AV2 from the older TB1 deck.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const manifest = JSON.parse(await fs.readFile(path.join(root, 'presentation/av2-keynote-export.json'), 'utf8'));
for (const file of manifest.files) {
  const bytes = await fs.readFile(path.join(root, file.path));
  const hash = createHash('sha256').update(bytes).digest('hex');
  if (hash !== file.sha256) throw new Error(`Export changed: ${file.path}. Review it and update the export record.`);
}
console.log('AV2: the reviewed PPTX and Canva PDF match the export record. No files were overwritten.');
console.log('For a new revision, follow presentation/av2-keynote-source.md.');
