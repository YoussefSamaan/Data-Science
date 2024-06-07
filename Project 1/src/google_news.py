from gnews import GNews


def fetch_google_news(keywords, daterange):

    ts_articles = []

    for x in daterange:
        google_news = GNews(language='en', country='US', start_date=daterange[x][0], end_date=daterange[x][1])
        json_resp = google_news.get_news(keywords)

        filtered_articles = [article for article in json_resp if
                             'taylor swift' in article['title'].lower()]

        ts_articles.extend(filtered_articles)

    return ts_articles


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
    keyword = 'Taylor Swift'

    news = fetch_google_news(keyword, dates)

    print(news)

    print(len(news))
