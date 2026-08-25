import os
from datetime import datetime

os.makedirs("site", exist_ok=True)

schedule_html = ""
try:
    with open("site/data/schedule.html") as f:
        schedule_html = f.read()
except:
    schedule_html = "<p>Schedule unavailable.</p>"

html = f"""
<html>
<head>
<title>SSSL Monitor</title>
<style>
body {{ font-family: Arial; padding: 20px; }}
table {{ border-collapse: collapse; width: 100%; }}
td, th {{ border: 1px solid #ccc; padding: 8px; }}
</style>
</head>
<body>
<h1>SSSL Schedule Monitor</h1>
<p>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
{schedule_html}
</body>
</html>
"""

with open("site/index.html", "w") as f:
    f.write(html)
