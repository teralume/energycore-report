const fs = require('fs');
const os = require('os');
const path = require('path');
const { pathToFileURL } = require('url');

const repoRoot = path.resolve(__dirname, '..');
const inputPath = path.join(repoRoot, 'README.md');
const outputPath = path.join(
  repoRoot,
  'output',
  'pdf',
  'upc-pre-202610-1asi0732-9100-teralume-report-av1.pdf',
);
const tempDirectory = path.join(repoRoot, 'tmp', 'pdfs');
const tempHtmlPath = path.join(tempDirectory, 'energycore-report-av1.html');

const extensionsRoot = path.join(os.homedir(), '.vscode', 'extensions');
const extensionDirectory = fs
  .readdirSync(extensionsRoot, { withFileTypes: true })
  .filter((entry) => entry.isDirectory() && entry.name.startsWith('yzane.markdown-pdf-'))
  .map((entry) => path.join(extensionsRoot, entry.name))
  .sort()
  .at(-1);

if (!extensionDirectory) {
  throw new Error('The yzane.markdown-pdf VS Code extension is not installed.');
}

const bundledModules = path.join(
  os.homedir(),
  '.cache',
  'codex-runtimes',
  'codex-primary-runtime',
  'dependencies',
  'node',
  'node_modules',
);
const { marked } = require(path.join(bundledModules, 'marked'));
const { chromium } = require(path.join(bundledModules, 'playwright'));

const browserCandidates = [
  process.env.PROGRAMFILES && path.join(process.env.PROGRAMFILES, 'Microsoft', 'Edge', 'Application', 'msedge.exe'),
  process.env['PROGRAMFILES(X86)'] && path.join(process.env['PROGRAMFILES(X86)'], 'Microsoft', 'Edge', 'Application', 'msedge.exe'),
  process.env.PROGRAMFILES && path.join(process.env.PROGRAMFILES, 'Google', 'Chrome', 'Application', 'chrome.exe'),
  process.env.LOCALAPPDATA && path.join(process.env.LOCALAPPDATA, 'Google', 'Chrome', 'Application', 'chrome.exe'),
].filter(Boolean);
const executablePath = browserCandidates.find((candidate) => fs.existsSync(candidate));

if (!executablePath) {
  throw new Error('Microsoft Edge or Google Chrome was not found.');
}

function escapeHtml(value) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}

async function main() {
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.mkdirSync(tempDirectory, { recursive: true });

  const markdown = fs.readFileSync(inputPath, 'utf8');
  const content = marked.parse(markdown, { gfm: true, breaks: false });
  const styles = ['markdown.css', 'markdown-pdf.css', 'tomorrow.css']
    .map((name) => fs.readFileSync(path.join(extensionDirectory, 'styles', name), 'utf8'))
    .join('\n');
  const baseUrl = pathToFileURL(`${repoRoot}${path.sep}`).href;
  const title = 'EnergyCore - Project Report AV1';
  const html = `<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <base href="${escapeHtml(baseUrl)}">
  <title>${escapeHtml(title)}</title>
  <style>
    ${styles}
    body { font-family: "Segoe UI", Arial, sans-serif; }
    img { max-width: 100%; height: auto; }
    table { width: 100%; font-size: 9pt; break-inside: auto; }
    tr, img, pre, blockquote { break-inside: avoid; }
    h1, h2, h3, h4 { break-after: avoid; }
    pre { white-space: pre-wrap; overflow-wrap: anywhere; }
    code { overflow-wrap: anywhere; }
    a { color: #5b21b6; text-decoration: none; }
    @page { size: A4; margin: 1.5cm 1cm 1cm; }
  </style>
</head>
<body class="markdown-body">${content}</body>
</html>`;
  fs.writeFileSync(tempHtmlPath, html, 'utf8');

  const browser = await chromium.launch({
    executablePath,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--allow-file-access-from-files'],
  });
  try {
    const page = await browser.newPage();
    await page.goto(pathToFileURL(tempHtmlPath).href, { waitUntil: 'networkidle0', timeout: 0 });
    await page.pdf({
      path: outputPath,
      format: 'A4',
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: '<div style="font-size:8px;margin-left:1cm;color:#555">EnergyCore - Project Report AV1</div>',
      footerTemplate: '<div style="font-size:8px;margin:0 auto;color:#555"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
      margin: { top: '1.5cm', right: '1cm', bottom: '1cm', left: '1cm' },
    });
  } finally {
    await browser.close();
  }

  fs.rmSync(tempDirectory, { recursive: true, force: true });
  console.log(outputPath);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
