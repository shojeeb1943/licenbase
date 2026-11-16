import urllib.request
import json
import time

url = "https://dashboard.licenbase.com/modules/addons/whmcsmcp/mcp.php"
token = "wmcp_ypbKEJuEEdjkOyPZShd1RCymAvnoiHjM1DdXNXI4o_8"

products = [
    {
        "id": 48,
        "name": "Managed Cloud VPS 4",
        "description": (
            "• 4 vCPU Cores\n"
            "• 8 GB Guaranteed RAM\n"
            "• 100 GB High-Speed SSD Storage\n"
            "• 1 Automated Snapshot\n"
            "• 200 Mbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel & Necessary Licenses Included\n"
            "• Softaculous 1-Click Script Installer & SitePad Website Builder Included\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        )
    },
    {
        "id": 49,
        "name": "Managed Cloud VPS 6",
        "description": (
            "• 6 vCPU Cores\n"
            "• 12 GB Guaranteed RAM\n"
            "• 200 GB SSD / 100 GB NVMe Storage\n"
            "• 2 Automated Snapshots\n"
            "• 300 Mbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel & Necessary Licenses Included\n"
            "• Softaculous 1-Click Script Installer & SitePad Website Builder Included\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        )
    },
    {
        "id": 50,
        "name": "Managed Cloud VPS 8",
        "description": (
            "• 8 vCPU Cores\n"
            "• 24 GB Guaranteed RAM\n"
            "• 300 GB SSD / 150 GB NVMe Storage\n"
            "• 3 Automated Snapshots\n"
            "• 600 Mbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel & Necessary Licenses Included\n"
            "• Softaculous 1-Click Script Installer & SitePad Website Builder Included\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        )
    },
    {
        "id": 51,
        "name": "Managed Cloud VPS 12",
        "description": (
            "• 12 vCPU Cores\n"
            "• 48 GB Guaranteed RAM\n"
            "• 400 GB SSD / 200 GB NVMe Storage\n"
            "• 3 Automated Snapshots\n"
            "• 800 Mbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel & Necessary Licenses Included\n"
            "• Softaculous 1-Click Script Installer & SitePad Website Builder Included\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        )
    },
    {
        "id": 52,
        "name": "Managed Cloud VPS 16",
        "description": (
            "• 16 vCPU Cores\n"
            "• 64 GB Guaranteed RAM\n"
            "• 500 GB SSD / 250 GB NVMe Storage\n"
            "• 3 Automated Snapshots\n"
            "• 1 Gbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel & Necessary Licenses Included\n"
            "• Softaculous 1-Click Script Installer & SitePad Website Builder Included\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        )
    },
    {
        "id": 53,
        "name": "Managed Cloud VPS 18",
        "description": (
            "• 18 vCPU Cores\n"
            "• 96 GB Guaranteed RAM\n"
            "• 600 GB SSD / 300 GB NVMe Storage\n"
            "• 3 Automated Snapshots\n"
            "• 1 Gbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel & Necessary Licenses Included\n"
            "• Softaculous 1-Click Script Installer & SitePad Website Builder Included\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        )
    }
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

# Check if update_product is registered
tools_payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
req = urllib.request.Request(url, data=json.dumps(tools_payload).encode("utf-8"), headers={
    "Authorization": f"Bearer {token}", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0"
})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    tools = [t["name"] for t in data["result"]["tools"]]

if "update_product" not in tools:
    print("Tool 'update_product' is not yet present on remote server.")
    print("Please upload whmcs/modules/addons/whmcsmcp/lib/Tools/ToolCatalog.php to your server first.")
else:
    print("Tool 'update_product' found! Submitting description updates...")
    for p in products:
        res = call_tool("update_product", {"id": p["id"], "description": p["description"]})
        print(f"PID {p['id']}: {res}")
