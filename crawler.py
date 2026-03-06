import requests
import os

# create pages folder if it doesn't exist
os.makedirs("pages", exist_ok=True)

with open("urls.txt", "r") as f:
    urls = f.read().splitlines()

index = open("index.txt", "w", encoding="utf-8")

for i, url in enumerate(urls, start=1):
    try:
        print(f"Downloading {url}")

        response = requests.get(url)

        filename = f"pages/page{i}.html"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        index.write(f"{i} {url}\n")

    except Exception as e:
        print("Error:", url)

index.close()

print("Finished crawling.")