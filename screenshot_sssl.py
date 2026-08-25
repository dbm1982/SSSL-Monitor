import os
import requests

# Ensure the snapshot directory exists inside the site folder
os.makedirs("site/snapshot", exist_ok=True)

def capture():
    print("Fetching screenshot from ScreenshotMachine…")

    API_KEY = "YOUR_KEY"  # free key from screenshotmachine.com
    TARGET_URL = "https://southshoresoccer.com/schedule"

    api_url = (
        f"https://api.screenshotmachine.com"
        f"?key={API_KEY}"
        f"&url={TARGET_URL}"
        f"&dimension=1024xfull"
        f"&format=png"
    )

    response = requests.get(api_url)

    if response.status_code != 200:
        print("ERROR: Screenshot API failed:", response.status_code)
        return

    with open("site/snapshot/schedule.png", "wb") as f:
        f.write(response.content)

    print("Screenshot saved successfully.")

if __name__ == "__main__":
    capture()
