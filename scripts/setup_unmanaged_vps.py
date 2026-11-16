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

# Products to configure
catalog = [
    {
        "pid": 54, # already created
        "name": "Unmanaged Cloud VPS x4",
        "order": 1,
        "monthly": 5.98,
        "description": (
            "• 2 Core CPU\n"
            "• 4 GB RAM\n"
            "• 40 GB NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included"
        )
    },
    {
        "pid": None,
        "name": "Unmanaged Cloud VPS x8",
        "order": 2,
        "monthly": 11.98,
        "description": (
            "• 4 Core CPU\n"
            "• 8 GB RAM\n"
            "• 60 GB NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included"
        )
    },
    {
        "pid": None,
        "name": "Unmanaged Cloud VPS x12",
        "order": 3,
        "monthly": 17.98,
        "description": (
            "• 4 Core CPU\n"
            "• 12 GB RAM\n"
            "• 90 GB NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included"
        )
    },
    {
        "pid": None,
        "name": "Unmanaged Cloud VPS x16",
        "order": 4,
        "monthly": 21.98,
        "description": (
            "• 6 Core CPU\n"
            "• 16 GB RAM\n"
            "• 120 GB High-Speed NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included"
        )
    },
    {
        "pid": None,
        "name": "Unmanaged Cloud VPS x24",
        "order": 5,
        "monthly": 31.98,
        "description": (
            "• 6 Core CPU\n"
            "• 24 GB RAM\n"
            "• 180 GB NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included"
        )
    },
    {
        "pid": None,
        "name": "Unmanaged Cloud VPS x32",
        "order": 6,
        "monthly": 41.98,
        "description": (
            "• 6 Core CPU\n"
            "• 32 GB RAM\n"
            "• 180 GB NVMe Storage\n"
            "• 1 Gbps Port (Unlimited Bandwidth)\n"
            "• FREE Automated Backup\n"
            "• Full Root Access (Linux / Windows)\n"
            "• Dedicated IPv4 Included"
        )
    }
]

created_products = []

for item in catalog:
    pid = item["pid"]
    if pid is None:
        # Create product
        res = call_tool("create_product", {
            "gid": 10,
            "name": item["name"],
            "paytype": "recurring",
            "description": item["description"]
        })
        pid = res.get("result", {}).get("structuredContent", {}).get("response", {}).get("pid")
        print(f"Created {item['name']} -> PID: {pid}")
        time.sleep(0.3)
    else:
        print(f"Using existing PID {pid} for {item['name']}")

    # Set pricing (double of base)
    price_res = call_tool("update_product_pricing", {
        "productid": pid,
        "currency": 1,
        "monthly": item["monthly"]
    })
    print(f"  Pricing set to ${item['monthly']}/mo -> {price_res.get('result', {}).get('structuredContent', {}).get('result')}")
    time.sleep(0.3)

    # Set sort order
    order_res = call_tool("update_product", {
        "id": pid,
        "order": item["order"]
    })
    print(f"  Sort order set to {item['order']} -> {order_res.get('result', {}).get('structuredContent', {}).get('result')}")
    time.sleep(0.3)

    created_products.append({
        "pid": pid,
        "name": item["name"],
        "order": item["order"],
        "monthly": item["monthly"]
    })

print("\n--- Setup Complete ---")
print(json.dumps(created_products, indent=2))
