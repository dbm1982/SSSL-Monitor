import os
from datetime import datetime

# Ensure site/snapshot exists
os.makedirs("site/snapshot", exist_ok=True)

html = f"""
<html>
<head>
<title>SSSL Monitor</title>
<style>
body {{ font-family: Arial; padding: 20px; }}
img {{ max-width: 100%; border: 1px solid #ccc; margin-top: 20px; }}
</style>
</head>
<body>
<h1>SSSL Schedule Monitor</h1>
<p>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
<p>Latest screenshot:</p>
<img src="snapshot/schedule.png" alt="Schedule Screenshot">
</body>
</html>
"""

with open("site/index.html", "w") as f:
    f.write(html)
