import requests

def get_news():
    # Example function to fetch the latest news using a news API
    api_key = "d3d3597262024bd08f99742dc7df8af0"
  # Replace with your actual API key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        news = response.json()
        articles = news['articles']
        headlines = []
        for i ,article in enumerate(articles[:5]):
            headlines.append(f"{i +1}.{article['title']}")
        return "\n".join(headlines)
    else:
        return "Sorry, I couldn't fetch the news at the moment."