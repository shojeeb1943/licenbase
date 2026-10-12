from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 630})
    content = """<!DOCTYPE html><html><body style="font-family: 'Inter', 'Nirmala UI', sans-serif; background: #0f172a; color: white;">
    <h1>cPanel লাইসেন্সের দাম কত?</h1>
    <p>VPS সার্ভারের জন্য সাশ্রয়ী লাইসেন্স গাইড</p>
    </body></html>"""
    page.set_content(content)
    page.screenshot(path="scratch/test_bengali.png")
    browser.close()
print("Screenshot created successfully")
