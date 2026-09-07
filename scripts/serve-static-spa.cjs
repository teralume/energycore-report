const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(process.argv[2] || '.');
const port = Number(process.argv[3] || 4200);
const host = '127.0.0.1';
const mimeTypes = {
  '.css': 'text/css; charset=utf-8',
  '.html': 'text/html; charset=utf-8',
  '.ico': 'image/x-icon',
  '.jpeg': 'image/jpeg',
  '.jpg': 'image/jpeg',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml; charset=utf-8',
  '.webp': 'image/webp',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
};

function sendFile(response, filePath) {
  const stream = fs.createReadStream(filePath);
  response.writeHead(200, {
    'Cache-Control': 'no-store',
    'Content-Type': mimeTypes[path.extname(filePath).toLowerCase()] || 'application/octet-stream',
  });
  stream.pipe(response);
  stream.on('error', () => response.destroy());
}

const server = http.createServer((request, response) => {
  const pathname = decodeURIComponent(new URL(request.url, `http://${host}:${port}`).pathname);

  if (pathname.startsWith('/api/v1/')) {
    const proxyRequest = http.request({
      hostname: '127.0.0.1',
      port: 4500,
      path: request.url,
      method: request.method,
      headers: request.headers,
    }, (proxyResponse) => {
      response.writeHead(proxyResponse.statusCode || 502, proxyResponse.headers);
      proxyResponse.pipe(response);
    });
    proxyRequest.on('error', () => response.writeHead(502).end('Evidence API unavailable'));
    request.pipe(proxyRequest);
    return;
  }

  const requested = path.resolve(root, `.${pathname}`);
  const insideRoot = requested === root || requested.startsWith(`${root}${path.sep}`);

  if (!insideRoot) {
    response.writeHead(403).end('Forbidden');
    return;
  }

  let candidate = requested;
  if (fs.existsSync(candidate) && fs.statSync(candidate).isDirectory()) {
    candidate = path.join(candidate, 'index.html');
  }

  if (fs.existsSync(candidate) && fs.statSync(candidate).isFile()) {
    sendFile(response, candidate);
    return;
  }

  const fallback = path.join(root, 'index.html');
  if (fs.existsSync(fallback)) {
    sendFile(response, fallback);
    return;
  }

  response.writeHead(404).end('Not found');
});

server.listen(port, host, () => {
  process.stdout.write(`SPA server ready at http://${host}:${port}\n`);
});
