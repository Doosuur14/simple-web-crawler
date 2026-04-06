import requests
import os
import time

# create pages folder if it doesn't exist
os.makedirs("pages", exist_ok=True)

with open("urls.txt", "r") as f:
    urls = f.read().splitlines()

index = open("index.txt", "w", encoding="utf-8")

# ✅ ADD HEADERS (THIS FIXES YOUR ERROR)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
}

for i, url in enumerate(urls, start=1):
    try:
        print(f"Downloading {url}")

        # ✅ use headers here
        response = requests.get(url, headers=headers)

        filename = f"pages/page{i}.html"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        index.write(f"{i} {url}\n")

        # ✅ BE POLITE (avoid getting blocked)
        time.sleep(1)

    except Exception as e:
        print("Error:", url, e)

index.close()

print("Finished crawling.")