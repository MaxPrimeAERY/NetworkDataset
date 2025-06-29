import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.collect_network_info import scan_network


def test_scan_network_no_results(monkeypatch):
    # Mock srp to return empty list
    def fake_srp(*args, **kwargs):
        return [], []

    monkeypatch.setattr('scripts.collect_network_info.srp', fake_srp)
    result = scan_network('192.168.1.0/30')
    assert result == []

