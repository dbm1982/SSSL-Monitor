import os
import requests

os.makedirs("site/snapshot", exist_ok=True)

def capture():
    print("Fetching screenshot from Microlink…")

    TARGET_URL = "https://southshoresoccer.com/schedule"

    api_url = (
        "https://api.microlink.io"
        "?url=" + TARGET_URL +
        "&screenshot=true"
        "&meta=false"
        "&embed=screenshot.url"
        "&waitUntil=networkidle2"
    )

    # First request: get JSON containing screenshot URL
    meta = requests.get(api_url).json()

    if "data" not in meta or "screenshot" not in meta["data"]:
        print("ERROR: Microlink did not return screenshot metadata.")
        print(meta)
        return

    screenshot_url = meta["data"]["screenshot"]["url"]

    # Second request: download the actual PNG
    img = requests.get(screenshot_url)

    if img.status_code != 200:
        print("ERROR: Failed to download screenshot PNG:", img.status_code)
        return

    with open("site/snapshot/schedule.png", "wb") as f:
        f.write(img.content)

    print("Screenshot saved successfully.")

if __name__ == "__main__":
    capture()
