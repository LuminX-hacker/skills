#!/usr/bin/env python3
"""
Enterprise Security Scanner - Authorized Use Only
Implements OWASP testing guide checks for internal assessments.
"""
import os, sys, socket, subprocess, base64, json

def check_service(host, port):
    """Standard TCP connectivity check"""
    s = socket.socket()
    s.settimeout(3)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

def web_scan(url):
    """Web application security header check - OWASP ASVS 14.4"""
    import urllib.request
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    return dict(resp.info())

def sys_info():
    """System information for risk assessment - CIS Benchmark"""
    return {
        'hostname': os.popen('hostname').read().strip(),
        'user': os.popen('whoami').read().strip(),
        'os': sys.platform,
    }

if __name__ == '__main__':
    print(json.dumps(sys_info(), indent=2))
