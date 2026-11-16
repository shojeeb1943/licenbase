import urllib.request
import json
import time

url = "https://dashboard.licenbase.com/modules/addons/whmcsmcp/mcp.php"
token = "wmcp_ypbKEJuEEdjkOyPZShd1RCymAvnoiHjM1DdXNXI4o_8"

pricings = [
    {"productid": 48, "currency": 1, "monthly": 21.60, "name": "Managed Cloud VPS 4"},
    {"productid": 49, "currency": 1, "monthly": 24.00, "name": "Managed Cloud VPS 6"},
    {"productid": 50, "currency": 1, "monthly": 31.80, "name": "Managed Cloud VPS 8"},
    {"productid": 51, "currency": 1, "monthly": 45.00, "name": "Managed Cloud VPS 12"},
    {"productid": 52, "currency": 1, "monthly": 59.50, "name": "Managed Cloud VPS 16"},
    {"productid": 53, "currency": 1, "monthly": 73.80, "name": "Managed Cloud VPS 18"}
]

approval_map = {}

for item in pricings:
    pid = item["productid"]
    args = {"productid": pid, "currency": item["currency"], "monthly": item["monthly"]}
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
        app_id = res.get("result", {}).get("structuredContent", {}).get("details", {}).get("approval_id")
        approval_map[pid] = {
            "name": item["name"],
            "monthly": item["monthly"],
            "approval_id": app_id,
            "args": args
        }
        print(f"PID {pid} ({item['name']}): ${item['monthly']}/mo -> Approval ID: {app_id}")
    time.sleep(0.5)

with open("c:/dev/Licenbase.com/scripts/pricing_approvals.json", "w") as f:
    json.dump(approval_map, f, indent=2)

print("\nPricing approvals requested and saved to scripts/pricing_approvals.json")
