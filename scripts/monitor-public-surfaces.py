"""Read-only public synthetic monitoring. No accounts, writes, secrets or body retention."""
import argparse
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API = 'https://energycore-platform-ujdgb2zcpq-ue.a.run.app'
TARGETS = [('api-health', API + '/api/v1/health', 'health'),
           ('api-contract', API + '/v3/api-docs', 'openapi'),
           ('webapp', 'https://university-energycorp.web.app', 'html')]


def validate_payload(kind, status, content_type, body):
    if status != 200:
        return False
    if kind == 'html':
        return 'text/html' in content_type and b'<html' in body.lower()
    try:
        payload = json.loads(body)
        if kind == 'health':
            return isinstance(payload, dict) and payload.get('status') == 'UP'
        return (isinstance(payload, dict) and str(payload.get('openapi', '')).startswith('3.')
                and bool(payload.get('paths')))
    except (ValueError, TypeError):
        return False


def probe(name, url, kind):
    started = time.perf_counter()
    status, ok, error = None, False, None
    try:
        with urlopen(Request(url, headers={'User-Agent': 'EnergyCore-AV2-Monitor/1.0'}), timeout=60) as response:
            status = response.status
            ok = validate_payload(kind, status, response.headers.get('Content-Type', ''), response.read(2_000_000))
            if not ok:
                error = 'unexpected_status_or_payload'
    except HTTPError as exc:
        status, error = exc.code, 'http_error'
    except (URLError, TimeoutError, OSError):
        error = 'connection_or_timeout'
    return {'name': name, 'url': url, 'http_status': status, 'passed': ok,
            'elapsed_ms': round((time.perf_counter() - started) * 1000), 'error': error}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('output/monitoring/latest.json'))
    args = parser.parse_args()
    result = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'mode': 'read_only_synthetic',
              'checks': [probe(*target) for target in TARGETS],
              'limitations': 'Point-in-time reachability and payload only; no uptime SLA, browser E2E, user validation, or physical energy measurement.'}
    result['passed'] = all(check['passed'] for check in result['checks'])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    summary = '\n'.join(['## EnergyCore public monitoring', '| Surface | HTTP | ms | Result |',
                         '|---|---:|---:|---|'] +
                        [f"| {c['name']} | {c['http_status']} | {c['elapsed_ms']} | {'PASS' if c['passed'] else 'FAIL'} |" for c in result['checks']])
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as stream:
            stream.write(summary + '\n')
    print(json.dumps(result, indent=2))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
