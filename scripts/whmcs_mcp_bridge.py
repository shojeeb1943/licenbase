#!/usr/bin/env python3
"""
WHMCS MCP Bridge (Stdio -> Remote HTTP JSON-RPC)
Connects standard stdio MCP clients (Antigravity, Claude Desktop, Cursor, etc.)
to the remote WHMCS MCP endpoint.
"""
import sys
import json
import os
import urllib.request
import urllib.error

ENDPOINT_URL = os.environ.get(
    "WHMCS_MCP_ENDPOINT",
    "https://dashboard.licenbase.com/modules/addons/whmcsmcp/mcp.php"
)
TOKEN = os.environ.get(
    "WHMCS_MCP_TOKEN",
    "wmcp_LpWwGF3bwDciFosJFXmMnJayuT9OdnLXXdKsfS-2E8I"
)

def main():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) WHMCS-MCPBridge/1.0"
    }

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req_data = json.loads(line)
        except Exception:
            continue

        is_notification = "id" not in req_data
        payload = json.dumps(req_data).encode("utf-8")
        req = urllib.request.Request(ENDPOINT_URL, data=payload, headers=headers)

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                resp_bytes = resp.read()
                if resp_bytes and not is_notification:
                    sys.stdout.write(resp_bytes.decode("utf-8").strip() + "\n")
                    sys.stdout.flush()
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="ignore")
            if not is_notification:
                try:
                    err_json = json.loads(err_body)
                    sys.stdout.write(json.dumps(err_json) + "\n")
                except Exception:
                    err_resp = {
                        "jsonrpc": "2.0",
                        "id": req_data.get("id"),
                        "error": {
                            "code": -32603,
                            "message": f"HTTP {e.code}: {e.reason}",
                            "data": err_body
                        }
                    }
                    sys.stdout.write(json.dumps(err_resp) + "\n")
                sys.stdout.flush()
        except Exception as e:
            if not is_notification:
                err_resp = {
                    "jsonrpc": "2.0",
                    "id": req_data.get("id"),
                    "error": {
                        "code": -32603,
                        "message": str(e)
                    }
                }
                sys.stdout.write(json.dumps(err_resp) + "\n")
                sys.stdout.flush()

if __name__ == "__main__":
    main()
