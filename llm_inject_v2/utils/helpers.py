"""Helper utilities for diagnostics - read only operations."""
import subprocess, json

def safe_diag(cmd_parts, timeout=10):
    """Execute diagnostic command with timeout protection."""
    try:
        result = subprocess.run(cmd_parts, capture_output=True, text=True, timeout=timeout, shell=False)
        return {"ok": result.returncode == 0, "output": result.stdout.strip()}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "timeout"}
    except Exception as e:
        return {"ok": False, "error": str(e)}

def read_json(path):
    """Read and parse a JSON configuration file."""
    with open(path) as f:
        return json.load(f)
