"""Verify the monitor rejects false positives without external network access."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('monitor', Path(__file__).with_name('monitor-public-surfaces.py'))
monitor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(monitor)


class PayloadTests(unittest.TestCase):
    def test_health_requires_up(self):
        self.assertTrue(monitor.validate_payload('health', 200, 'application/json', b'{"status":"UP"}'))
        self.assertFalse(monitor.validate_payload('health', 200, 'application/json', b'{"status":"DOWN"}'))

    def test_contract_rejects_spa_fallback(self):
        self.assertFalse(monitor.validate_payload('openapi', 200, 'text/html', b'<html>app</html>'))
        self.assertFalse(monitor.validate_payload('openapi', 200, 'application/json', b'{"openapi":"3.1.0","paths":{}}'))
        self.assertTrue(monitor.validate_payload('openapi', 200, 'application/json', b'{"openapi":"3.1.0","paths":{"/x":{}}}'))

    def test_html_requires_success_and_html(self):
        self.assertFalse(monitor.validate_payload('html', 503, 'text/html', b'<html>maintenance</html>'))
        self.assertFalse(monitor.validate_payload('html', 200, 'application/json', b'{}'))
        self.assertTrue(monitor.validate_payload('html', 200, 'text/html; charset=utf-8', b'<!doctype html><html></html>'))


if __name__ == '__main__':
    unittest.main()
