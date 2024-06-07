from google_news import fetch_google_news
from news_api import fetch_latest_news
import os
import json
from email.utils import parsedate_to_datetime

# Set to store unique URLs
unique_urls = set()


def transform_gnews(data):

    transformed = []
    for item in data:
        if item['url'] not in unique_urls:
            unique_urls.add(item['url'])
            transformed.append({
                'source': item['publisher'],
                'title': item['title'],
                'description': item['description'],
                'url': item['url'],
                'publishedAt': parsedate_to_datetime(item['published date']).strftime('%Y-%m-%dT%H:%M:%SZ'),
                'API': 'GNews'
            })
    return transformed


def transform_newsapi(data):

    transformed = []
    for item in data:
        if item['url'] not in unique_urls:
            unique_urls.add(item['url'])
            transformed.append({
                'source': {
                    'href': item['url'],  # Assuming URL as href for consistency with GNews format
                    'title': item['source']['name']
                },
                'title': item['title'],
                'description': item['description'],
                'url': item['url'],
                'publishedAt': item['publishedAt'],
                'API': 'NewsAPI'
            })
    return transformed


if __name__ == '__main__':
    dates = {
        5: [(2023, 5, 1), (2023, 5, 31)],
        6: [(2023, 6, 1), (2023, 6, 30)],
        7: [(2023, 7, 1), (2023, 7, 31)],
        8: [(2023, 8, 1), (2023, 8, 31)],
        9: [(2023, 9, 1), (2023, 9, 30)],
        10: [(2023, 10, 1), (2023, 10, 31)],
        11: [(2023, 11, 1), None]
    }

    news_keywords = ['Taylor', 'Swift']

    api_key = os.environ.get('API_KEY')

    gnews_data = fetch_google_news(' '.join(news_keywords), dates)

    newsapi_data = fetch_latest_news(api_key, news_keywords, 30)

    unified_data = transform_gnews(gnews_data) + transform_newsapi(newsapi_data)

    with open('data/unified_swift_data.json', 'w') as file:
        json.dump(unified_data, file, indent=4)
