import os
from playwright.sync_api import sync_playwright

os.makedirs("site/snapshot", exist_ok=True)

def capture():
    print("Starting Playwright…")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            print("Loading schedule page…")
            response = page.goto("https://southshoresoccer.com/schedule", timeout=30000)

            if not response:
                print("ERROR: No response from server.")
            else:
                print("Status:", response.status)
                if not response.ok:
                    print("ERROR: Page failed to load.")

            print("Taking screenshot…")
            page.screenshot(path="site/snapshot/schedule.png")
            print("Screenshot saved.")

            browser.close()
    except Exception as e:
        print("Playwright ERROR:", e)

if __name__ == "__main__":
    capture()
