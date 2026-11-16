import urllib.request
import json
import time

url = "https://dashboard.licenbase.com/modules/addons/whmcsmcp/mcp.php"
token = "wmcp_ypbKEJuEEdjkOyPZShd1RCymAvnoiHjM1DdXNXI4o_8"

with open("c:/dev/Licenbase.com/scripts/pricing_approvals.json") as f:
    approval_map = json.load(f)

for pid, data in approval_map.items():
    args = dict(data["args"])
    args["_approvalId"] = data["approval_id"]
    payload = {
        "jsonrpc": "2.0",
        "id": int(time.time() * 1000),
        "method": "tools/call",
        "params": {
            "name": "update_product_pricing",
            "arguments": args
        }
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode())
        print(f"PID {pid} ({data['name']}) -> {res.get('result', {}).get('structuredContent') or res}")
    time.sleep(0.5)
