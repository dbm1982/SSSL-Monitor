import requests
from bs4 import BeautifulSoup
import os

def fetch_schedule():
    url = "https://southshoresoccer.com/schedule"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")

    # Extract the schedule table (adjust selector if needed)
    table = soup.find("table")

    if not table:
        return "<p>Schedule unavailable.</p>"

    return str(table)

if __name__ == "__main__":
    os.makedirs("site/data", exist_ok=True)
    schedule_html = fetch_schedule()

    with open("site/data/schedule.html", "w") as f:
        f.write(schedule_html)
