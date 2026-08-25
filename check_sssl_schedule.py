import requests
from bs4 import BeautifulSoup
import os
import sys
import json

URL = "https://www.southshoresoccer.com/Schedules"
STATE_FILE = "state/schedule_status.json"

def load_state():
    if not os.path.exists(STATE_FILE):
        return {"has_schedule": False}
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    os.makedirs("state", exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def schedules_available():
    r = requests.get(URL, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")
    contests = soup.select(".contest")
    return len(contests) > 0

if __name__ == "__main__":
    previous = load_state()
    current = schedules_available()

    if current and not previous["has_schedule"]:
        print("Schedules detected.")
        save_state({"has_schedule": True})
        sys.exit(1)
    else:
        print("No schedules yet.")
        save_state({"has_schedule": current})
        sys.exit(0)
