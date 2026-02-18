import requests
import pandas as pd

API_KEY = "242074edd2be48b98c230d62c9de2b4d"

query = "cybersecurity OR malware OR ransomware"

url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=50&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

articles = []

for article in data["articles"]:
    articles.append({
        "title": article["title"],
        "description": article["description"],
        "content": article["content"],
        "source": article["source"]["name"],
        "published_at": article["publishedAt"],
        "url": article["url"],
        "topic": "cybersecurity"
    })

df = pd.DataFrame(articles)

df.dropna(inplace=True)
df.drop_duplicates(subset="title", inplace=True)

df.to_csv("cybersecurity_corpus.csv", index=False)
df.to_json("cybersecurity_corpus.json", orient="records", indent=4)

print("Corpus Created Successfully!")
print("Total Articles Collected:", len(df))
