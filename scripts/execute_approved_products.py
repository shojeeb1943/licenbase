import urllib.request
import json
import time

url = "https://dashboard.licenbase.com/modules/addons/whmcsmcp/mcp.php"
token = "wmcp_ypbKEJuEEdjkOyPZShd1RCymAvnoiHjM1DdXNXI4o_8"

pending = [
    {
        "name": "Managed Cloud VPS 6",
        "gid": 9,
        "paytype": "recurring",
        "description": (
            "• 6 vCPU Cores\n"
            "• 12 GB Guaranteed RAM\n"
            "• 200 GB SSD / 100 GB NVMe Storage\n"
            "• 2 Automated Snapshots\n"
            "• 300 Mbit/s Port (Unlimited Traffic)\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        ),
        "_approvalId": "a0a75b3c30a44b00526d21bcda3d159f"
    },
    {
        "name": "Managed Cloud VPS 8",
        "gid": 9,
        "paytype": "recurring",
        "description": (
            "• 8 vCPU Cores\n"
            "• 24 GB Guaranteed RAM\n"
            "• 300 GB SSD / 150 GB NVMe Storage\n"
            "• 3 Automated Snapshots\n"
            "• 600 Mbit/s Port (Unlimited Traffic)\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        ),
        "_approvalId": "9592eb851e5a5b3dbdd717d3a4dca383"
    },
    {
        "name": "Managed Cloud VPS 12",
        "gid": 9,
        "paytype": "recurring",
        "description": (
            "• 12 vCPU Cores\n"
            "• 48 GB Guaranteed RAM\n"
            "• 400 GB SSD / 200 GB NVMe Storage\n"
            "• 3 Automated Snapshots\n"
            "• 800 Mbit/s Port (Unlimited Traffic)\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        ),
        "_approvalId": "2d4c7913cda6ef141276a76184cd4c04"
    },
    {
        "name": "Managed Cloud VPS 16",
        "gid": 9,
        "paytype": "recurring",
        "description": (
            "• 16 vCPU Cores\n"
            "• 64 GB Guaranteed RAM\n"
            "• 500 GB SSD / 250 GB NVMe Storage\n"
            "• 3 Automated Snapshots\n"
            "• 1 Gbit/s Port (Unlimited Traffic)\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        ),
        "_approvalId": "21761007961081034d490b763718e2f1"
    },
    {
        "name": "Managed Cloud VPS 18",
        "gid": 9,
        "paytype": "recurring",
        "description": (
            "• 18 vCPU Cores\n"
            "• 96 GB Guaranteed RAM\n"
            "• 600 GB SSD / 300 GB NVMe Storage\n"
            "• 3 Automated Snapshots\n"
            "• 1 Gbit/s Port (Unlimited Traffic)\n"
            "• Fully Managed Support: OS updates, security hardening, firewall setup & 24/7 monitoring\n"
            "• Free Full Migration Assistance"
        ),
        "_approvalId": "2ecb8f2a4a5907552792a1fdd4e79241"
    }
]

for p in pending:
    payload = {
        "jsonrpc": "2.0",
        "id": int(time.time() * 1000),
        "method": "tools/call",
        "params": {
            "name": "create_product",
            "arguments": p
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
        print(f"{p['name']} -> {res}")
    time.sleep(0.5)
