import urllib.request
import json
import time

url = "https://dashboard.licenbase.com/modules/addons/whmcsmcp/mcp.php"
token = "wmcp_ypbKEJuEEdjkOyPZShd1RCymAvnoiHjM1DdXNXI4o_8"

order_map = [
    {"id": 48, "name": "Managed Cloud VPS 4", "order": 1},
    {"id": 49, "name": "Managed Cloud VPS 6", "order": 2},
    {"id": 50, "name": "Managed Cloud VPS 8", "order": 3},
    {"id": 51, "name": "Managed Cloud VPS 12", "order": 4},
    {"id": 52, "name": "Managed Cloud VPS 16", "order": 5},
    {"id": 53, "name": "Managed Cloud VPS 18", "order": 6}
]

def call_tool(name, args):
    payload = {
        "jsonrpc": "2.0",
        "id": int(time.time() * 1000),
        "method": "tools/call",
        "params": {
            "name": name,
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
        return json.loads(resp.read().decode())

for item in order_map:
    res = call_tool("update_product", {"id": item["id"], "order": item["order"]})
    print(f"PID {item['id']} ({item['name']}) -> order={item['order']}: {res.get('result', {}).get('structuredContent') or res}")
    time.sleep(0.3)
