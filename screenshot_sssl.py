import os
from playwright.sync_api import sync_playwright

# Ensure the snapshot directory exists inside the site folder
os.makedirs("site/snapshot", exist_ok=True)

def capture():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the SSSL schedule page
        page.goto("https://southshoresoccer.com/schedule")

        # Save screenshot into the published folder
        page.screenshot(path="site/snapshot/schedule.png")

        browser.close()

if __name__ == "__main__":
    capture()
