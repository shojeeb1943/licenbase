import urllib.request
import json
import time

url = "https://dashboard.licenbase.com/modules/addons/whmcsmcp/mcp.php"
token = "wmcp_ypbKEJuEEdjkOyPZShd1RCymAvnoiHjM1DdXNXI4o_8"

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

# 1. Managed VPS (Group 9)
managed_products = [
    {
        "id": 48,
        "name": "Managed Cloud VPS 4",
        "description": (
            "• 4 vCPU Cores\n"
            "• 8 GB Guaranteed RAM\n"
            "• 100 GB High-Speed SSD Storage\n"
            "• 200 Mbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel and necessary license included Softaculous.\n"
            "• SitePad Website Builder\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance\n"
            "• 1-2 Hours Activation Time"
        )
    },
    {
        "id": 49,
        "name": "Managed Cloud VPS 6",
        "description": (
            "• 6 vCPU Cores\n"
            "• 12 GB Guaranteed RAM\n"
            "• 200 GB SSD / 100 GB NVMe Storage\n"
            "• 300 Mbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel and necessary license included Softaculous.\n"
            "• SitePad Website Builder\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance\n"
            "• 1-2 Hours Activation Time"
        )
    },
    {
        "id": 50,
        "name": "Managed Cloud VPS 8",
        "description": (
            "• 8 vCPU Cores\n"
            "• 24 GB Guaranteed RAM\n"
            "• 300 GB SSD / 150 GB NVMe Storage\n"
            "• 600 Mbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel and necessary license included Softaculous.\n"
            "• SitePad Website Builder\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance\n"
            "• 1-2 Hours Activation Time"
        )
    },
    {
        "id": 51,
        "name": "Managed Cloud VPS 12",
        "description": (
            "• 12 vCPU Cores\n"
            "• 48 GB Guaranteed RAM\n"
            "• 400 GB SSD / 200 GB NVMe Storage\n"
            "• 800 Mbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel and necessary license included Softaculous.\n"
            "• SitePad Website Builder\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance\n"
            "• 1-2 Hours Activation Time"
        )
    },
    {
        "id": 52,
        "name": "Managed Cloud VPS 16",
        "description": (
            "• 16 vCPU Cores\n"
            "• 64 GB Guaranteed RAM\n"
            "• 500 GB SSD / 250 GB NVMe Storage\n"
            "• 1 Gbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel and necessary license included Softaculous.\n"
            "• SitePad Website Builder\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance\n"
            "• 1-2 Hours Activation Time"
        )
    },
    {
        "id": 53,
        "name": "Managed Cloud VPS 18",
        "description": (
            "• 18 vCPU Cores\n"
            "• 96 GB Guaranteed RAM\n"
            "• 600 GB SSD / 300 GB NVMe Storage\n"
            "• 1 Gbit/s Port (Unlimited Traffic)\n"
            "• WHM/cPanel Control Panel and necessary license included Softaculous.\n"
            "• SitePad Website Builder\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance\n"
            "• 1-2 Hours Activation Time"
        )
    }
]

# 2. Unmanaged VPS (Group 10)
unmanaged_products = [
    {
        "id": 54,
        "name": "Unmanaged Cloud VPS x4",
        "description": (
            "• 2 Core CPU\n"
            "• 4 GB RAM\n"
            "• 40 GB NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included\n"
            "• 1-2 Hours Activation Time"
        )
    },
    {
        "id": 55,
        "name": "Unmanaged Cloud VPS x8",
        "description": (
            "• 4 Core CPU\n"
            "• 8 GB RAM\n"
            "• 60 GB NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included\n"
            "• 1-2 Hours Activation Time"
        )
    },
    {
        "id": 56,
        "name": "Unmanaged Cloud VPS x12",
        "description": (
            "• 4 Core CPU\n"
            "• 12 GB RAM\n"
            "• 90 GB NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included\n"
            "• 1-2 Hours Activation Time"
        )
    },
    {
        "id": 57,
        "name": "Unmanaged Cloud VPS x16",
        "description": (
            "• 6 Core CPU\n"
            "• 16 GB RAM\n"
            "• 120 GB High-Speed NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included\n"
            "• 1-2 Hours Activation Time"
        )
    },
    {
        "id": 58,
        "name": "Unmanaged Cloud VPS x24",
        "description": (
            "• 6 Core CPU\n"
            "• 24 GB RAM\n"
            "• 180 GB NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included\n"
            "• 1-2 Hours Activation Time"
        )
    },
    {
        "id": 59,
        "name": "Unmanaged Cloud VPS x32",
        "description": (
            "• 6 Core CPU\n"
            "• 32 GB RAM\n"
            "• 180 GB NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included\n"
            "• 1-2 Hours Activation Time"
        )
    }
]

print("Updating Managed VPS products...")
for p in managed_products:
    res = call_tool("update_product", {"id": p["id"], "description": p["description"]})
    print(f"PID {p['id']} ({p['name']}) -> {res.get('result', {}).get('structuredContent', {}).get('result')}")
    time.sleep(0.2)

print("\nUpdating Unmanaged VPS products...")
for p in unmanaged_products:
    res = call_tool("update_product", {"id": p["id"], "description": p["description"]})
    print(f"PID {p['id']} ({p['name']}) -> {res.get('result', {}).get('structuredContent', {}).get('result')}")
    time.sleep(0.2)

print("\nAll 12 VPS products updated with '1-2 Hours Activation Time'!")
