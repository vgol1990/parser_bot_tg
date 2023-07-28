import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json

def get_first_news():
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }

    url = "https://www.securitylab.ru/news"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")
    articles_cards = soup.find_all("a", class_="article-card")

    news_dict = {}
    for article in articles_cards:
        article_title = article.find("h2", class_="article-card-title").text.strip()
        article_desc = article.find("p").text.strip()
        article_url = f'https://www.securitylab.ru/news{article.get("href")}'

        article_data_time = article.find("time").get("datetime")
        data_from_iso = datetime.fromisoformat(article_data_time)

        data_time = datetime.strftime(data_from_iso, "%Y-%m-%d %H:%M:%S")
        article_data_timestamp = time.mktime(datetime.strptime(data_time, "%Y-%m-%d %H:%M:%S").timetuple())

        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]



        print(f"{article_title} | {article_url}| {article_data_timestamp}")

        news_dict[article_id] = {
            "article_data_timestamp": article_data_timestamp,
            "article_title": article_title,
            "article_url": article_url,
            "article_desc": article_desc
        }

    with open("new_dict.json","w", encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)





def main():
    get_first_news()

if __name__ == '__main__':
    main()