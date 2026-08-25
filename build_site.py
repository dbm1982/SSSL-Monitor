import os
from datetime import datetime

os.makedirs("site", exist_ok=True)

# Read hash
hash_file = "site/data/hash.txt"
hash_value = ""
if os.path.exists(hash_file):
    with open(hash_file) as f:
        hash_value = f.read().strip()

# Read status
status_file = "site/data/status.txt"
status_value = "UNKNOWN"
if os.path.exists(status_file):
    with open(status_file) as f:
        status_value = f.read().strip()

html = f"""
<html>
<head>
<title>SSSL Monitor</title>
<style>
body {{ font-family: Arial; padding: 20px; }}
.status {{
    font-size: 2rem;
    font-weight: bold;
    color: {'green' if status_value == 'NO CHANGE' else 'red'};
}}
</style>
</head>
<body>
<h1>SSSL Schedule Monitor</h1>
<p>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
<p>Current hash: {hash_value}</p>
<p class="status">{status_value}</p>
</body>
</html>
"""

with open("site/index.html", "w") as f:
    f.write(html)
