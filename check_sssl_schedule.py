import requests
import hashlib
import os

URL = "https://textise.net/showtext.aspx?strURL=https://southshoresoccer.com/schedule"

def fetch_hash():
    text = requests.get(URL).text
    return hashlib.sha256(text.encode()).hexdigest()

if __name__ == "__main__":
    os.makedirs("site/data", exist_ok=True)

    new_hash = fetch_hash()
    hash_file = "site/data/hash.txt"
    status_file = "site/data/status.txt"

    old_hash = None
    if os.path.exists(hash_file):
        old_hash = open(hash_file).read().strip()

    # Write the new hash
    with open(hash_file, "w") as f:
        f.write(new_hash)

    # Determine status
    if old_hash and old_hash != new_hash:
        status = "CHANGE DETECTED"
    else:
        status = "NO CHANGE"

    # Write status file
    with open(status_file, "w") as f:
        f.write(status)

    print(status)
