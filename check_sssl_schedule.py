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

    old_hash = None
    if os.path.exists(hash_file):
        old_hash = open(hash_file).read().strip()

    with open(hash_file, "w") as f:
        f.write(new_hash)

    if old_hash and old_hash != new_hash:
        print("CHANGE DETECTED")
    else:
        print("NO CHANGE")
