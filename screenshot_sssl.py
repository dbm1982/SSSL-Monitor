from playwright.sync_api import sync_playwright
import os

URL = "https://www.southshoresoccer.com/Schedules"

os.makedirs("snapshot", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(URL)
    page.screenshot(path="snapshot/schedule.png", full_page=True)
    browser.close()
