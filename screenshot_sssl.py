import os
import requests

# Ensure the snapshot directory exists inside the site folder
os.makedirs("site/snapshot", exist_ok=True)

def capture():
    print("Fetching screenshot from APIFLASH…")

    TARGET_URL = "https://southshoresoccer.com/schedule"

    api_url = (
        "https://api.apiflash.com/v1/urltoimage"
        "?url=" + TARGET_URL +
        "&format=png"
        "&response_type=image"
        "&full_page=true"
        "&ttl=86400"
    )

    response = requests.get(api_url)

    print("Status:", response.status_code)

    if response.status_code != 200:
        print("ERROR: Screenshot API failed")
        return

    with open("site/snapshot/schedule.png", "wb") as f:
        f.write(response.content)

    print("Screenshot saved successfully.")

if __name__ == "__main__":
    capture()
