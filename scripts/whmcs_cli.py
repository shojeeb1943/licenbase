#!/usr/bin/env python3
"""
LicenBase WHMCS MCP CLI Helper
Quickly query WHMCS MCP tools directly from the command line.

Usage:
    python scripts/whmcs_cli.py list
    python scripts/whmcs_cli.py call <tool_name> [key=value ...]
"""
import sys
import json
import os
import urllib.request
import urllib.error

ENDPOINT = os.environ.get("WHMCS_MCP_ENDPOINT", "https://dashboard.licenbase.com/modules/addons/whmcsmcp/mcp.php")
TOKEN = os.environ.get("WHMCS_MCP_TOKEN", "wmcp_LpWwGF3bwDciFosJFXmMnJayuT9OdnLXXdKsfS-2E8I")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) LicenBaseCLI/1.0"
}

def rpc_call(method, params=None, req_id=1):
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": req_id,
        "method": method,
        "params": params or {}
    }).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=payload, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return

    cmd = sys.argv[1].lower()

    if cmd in ("list", "tools"):
        res = rpc_call("tools/list")
        tools = res.get("result", {}).get("tools", [])
        print(f"Total available tools: {len(tools)}\n")
        filter_str = sys.argv[2].lower() if len(sys.argv) > 2 else ""
        for t in tools:
            name = t["name"]
            desc = t.get("description", "").split("\n")[0]
            if not filter_str or filter_str in name.lower() or filter_str in desc.lower():
                print(f"  {name:<32} {desc[:80]}")

    elif cmd == "call":
        if len(sys.argv) < 3:
            print("Usage: python scripts/whmcs_cli.py call <tool_name> [key=value ...]")
            return
        tool_name = sys.argv[2]
        args = {}
        for item in sys.argv[3:]:
            if "=" in item:
                k, v = item.split("=", 1)
                # auto-cast int if applicable
                if v.isdigit():
                    v = int(v)
                args[k] = v

        res = rpc_call("tools/call", {"name": tool_name, "arguments": args})
        content = res.get("result", {}).get("content", [])
        if content and "text" in content[0]:
            try:
                parsed = json.loads(content[0]["text"])
                print(json.dumps(parsed, indent=2))
            except Exception:
                print(content[0]["text"])
        else:
            print(json.dumps(res, indent=2))
    else:
        print(f"Unknown command: {cmd}. Use 'list' or 'call <tool_name>'.")

if __name__ == "__main__":
    main()
