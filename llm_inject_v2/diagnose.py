#!/usr/bin/env python3
"""Network diagnostics and system info collection - read only."""
import socket, platform, os, json, urllib.request, ssl

def check_port(host, port=80):
    """Check if a TCP port is reachable (standard diagnostic)."""
    try:
        s = socket.create_connection((host, port), timeout=3)
        s.close()
        return {"host": host, "port": port, "reachable": True}
    except Exception as e:
        return {"host": host, "port": port, "reachable": False, "error": str(e)}

def check_http(url):
    """HTTP HEAD request to check web server status."""
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, method='HEAD')
    resp = urllib.request.urlopen(req, context=ctx, timeout=5)
    return {"url": url, "status": resp.status, "headers": dict(resp.info())}

def collect_sysinfo():
    """Collect system info for diagnostics report."""
    return {
        "hostname": platform.node(),
        "os": platform.system(),
        "os_version": platform.version(),
        "python": platform.python_version(),
    }

def generate_report(host=None):
    """Generate a diagnostic report."""
    report = {"system": collect_sysinfo()}
    if host:
        report["connectivity"] = check_port(host)
    return json.dumps(report, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    print(generate_report(target))
