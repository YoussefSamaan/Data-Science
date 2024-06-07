import requests
import datetime
import os

NEWS_API_URL = "https://newsapi.org/v2/everything"

# List of North American news sources (you can add or remove sources as needed)
NORTH_AMERICAN_SOURCES = ['cnn', 'fox-news', 'nbc-news', 'the-washington-post', 'the-new-york-times']


def fetch_latest_news(api_key, news_keywords, lookback_days=10):

    date = (datetime.date.today() - datetime.timedelta(lookback_days))

    params = {
        'apiKey': api_key,
        'q': ' '.join(news_keywords),
        'from': date,
        'language': 'en',
        'sources': ','.join(NORTH_AMERICAN_SOURCES),
        'sortBy': 'publishedAt',
    }

    response = requests.get(NEWS_API_URL, params=params)

    if response.status_code == 200:
        articles = response.json().get('articles', [])

        filtered_articles = [article for article in articles if
                             'taylor swift' in article['title'].lower()]

        return filtered_articles
    else:
        raise ValueError(f'Error response code {response.status_code}: {response.text}')


if __name__ == "__main__":
    api_key = os.environ.get('API_KEY')
    news_keywords = ['Taylor', 'Swift']
    print(' '.join(news_keywords))

    latest_news = fetch_latest_news(api_key, news_keywords, 11)

    print(len(latest_news))
