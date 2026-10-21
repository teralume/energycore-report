"""Capture traceable repository and CI evidence without changing product repositories."""
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT.parent
repos = ['energycore-platform', 'energycore-webapp', 'energycore-mobile', 'energycore-website', 'energycore-report']
records = []
for name in repos:
    repo = COURSE / name
    sha = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    ci = json.loads(subprocess.check_output(['gh', 'run', 'list', '--repo', 'teralume/' + name, '--limit', '1',
                    '--json', 'databaseId,conclusion,headSha,createdAt,url'], text=True))
    records.append({'repository': name, 'local_head': sha, 'latest_remote_run': ci,
                    'local_equals_ci_revision': bool(ci and ci[0]['headSha'] == sha)})

platform = COURSE / 'energycore-platform'
prod = (platform / 'src/main/resources/application-prod.properties').read_text(encoding='utf-8')
health = (platform / 'src/main/java/com/teralume/energycore/shared/interfaces/rest/controllers/HealthController.java').read_text(encoding='utf-8')
findings = [
    {'id': 'REV-01', 'status': 'OPEN', 'severity': 'medium', 'source': 'energycore-platform/src/main/resources/application-prod.properties',
     'observation': 'Production schema uses ddl-auto=update; no versioned migration acceptance is established.',
     'confirmed': 'spring.jpa.hibernate.ddl-auto=update' in prod, 'action': 'Introduce and verify versioned migrations before a production schema change.'},
    {'id': 'REV-02', 'status': 'VERIFIED', 'severity': 'informational', 'source': 'energycore-platform/.../HealthController.java',
     'observation': 'Public health routes are /health and /api/v1/health. The new monitor targets /api/v1/health.',
     'confirmed': '"/api/v1/health"' in health, 'action': 'Keep the monitor contract aligned with the public controller.'},
    {'id': 'REV-03', 'status': 'OPEN', 'severity': 'medium', 'source': 'energycore-platform/src/main/resources/application-prod.properties',
     'observation': 'Default production CORS list includes localhost:4200.', 'confirmed': 'http://localhost:4200' in prod,
     'action': 'Configure an environment-specific production allowlist and verify actual preflight before removing development defaults.'},
]
result = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'review_type': 'automated_source_inspection',
          'repositories': records, 'findings': findings,
          'limitations': 'Not a human peer approval, external UX audit, penetration test, or rerun of the historical product test suites.'}
target = ROOT / 'assets/evidence/implemented/av2-review-2026-10-21.json'
target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
