import requests

query = input("Enter the topic you want to search news for: ")

api_key = "b8eff777eccd42b79ceeb31255542334"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-05&sortBy=publishedAt&apiKey={api_key}"
print(url)

r = requests.get(url)
data = r.json()
articals = data['articles']
for articals in articals:
    print(articals["title"], articals["url"])
    print("\n*******************\n")