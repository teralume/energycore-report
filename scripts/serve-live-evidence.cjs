// Serves the existing Angular build against the REAL local Spring API.
// Only the API base URL is configured at response time; no API response is mocked.
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '../../energycore-webapp/dist/energycore-webapp/browser');
const types = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.webp': 'image/webp', '.woff2': 'font/woff2', '.ico': 'image/x-icon' };
http.createServer((req, res) => {
  const pathname = new URL(req.url, 'http://127.0.0.1:4300').pathname;
  if (pathname.startsWith('/api/v1/')) {
    const upstream = http.request({hostname: '127.0.0.1', port: 8080, path: req.url, method: req.method, headers: req.headers}, response => {
      res.writeHead(response.statusCode, response.headers);
      response.pipe(res);
    });
    upstream.on('error', () => res.writeHead(502).end('Real backend unavailable'));
    req.pipe(upstream);
    return;
  }
  let file = path.resolve(root, '.' + decodeURIComponent(pathname));
  if (file !== root && !file.startsWith(root + path.sep)) return res.writeHead(403).end();
  if (!fs.existsSync(file) || !fs.statSync(file).isFile()) file = path.join(root, 'index.html');
  const ext = path.extname(file);
  let content = fs.readFileSync(file);
  if (ext === '.js') content = Buffer.from(content.toString().replaceAll('https://energycore-platform-vfvqevfzvq-ue.a.run.app/api/v1', 'http://127.0.0.1:4300/api/v1').replaceAll('__ENERGYCORE_API_BASE_URL__', 'http://127.0.0.1:4300/api/v1'));
  res.writeHead(200, {'Content-Type': types[ext] || 'application/octet-stream', 'Cache-Control': 'no-store'});
  res.end(content);
}).listen(4300, '127.0.0.1', () => console.log('Angular evidence: http://127.0.0.1:4300; real API: http://127.0.0.1:8080'));
