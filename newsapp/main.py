import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
if not api_key:
    raise ValueError("API_KEY not found. Check your .env file.")

query = input("Enter the topic you want to search news for: ")

url = f"https://newsapi.org/v2/everythingTATA?q={query}&from=2025-12-05&sortBy=publishedAt&apiKey={api_key}"
print(url)
r = requests.get(url)
data = r.json()

articles = data['articles']
for article in articles:
    print(article["title"], article["url"], sep="\n")
    print("\n" + "*" * 30 + "\n")
