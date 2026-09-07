const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const outputDir = path.resolve(__dirname, '..', 'assets', 'evidence', 'implemented');
fs.mkdirSync(outputDir, { recursive: true });

const server = http.createServer((request, response) => {
  if (request.method !== 'POST') {
    response.writeHead(405).end('POST required');
    return;
  }

  const requestedName = decodeURIComponent(new URL(request.url, 'http://127.0.0.1:4400').pathname.slice(1));
  const fileName = path.basename(requestedName);

  if (!/^[a-z0-9-]+\.png$/i.test(fileName)) {
    response.writeHead(400).end('Invalid filename');
    return;
  }

  const chunks = [];
  request.on('data', (chunk) => chunks.push(chunk));
  request.on('end', () => {
    const body = Buffer.concat(chunks);
    if (body.length < 100 || body.length > 15 * 1024 * 1024) {
      response.writeHead(400).end('Invalid image size');
      return;
    }

    fs.writeFileSync(path.join(outputDir, fileName), body);
    response.writeHead(201, { 'Content-Type': 'text/plain' }).end(`${fileName}:${body.length}`);
  });
});

server.listen(4400, '127.0.0.1', () => {
  process.stdout.write(`Capture receiver ready at http://127.0.0.1:4400\n`);
});
