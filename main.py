import os
from src import AutoCall


if __name__ == "__main__":
    if not os.path.exists('news'):
        os.mkdir('news')
    news = AutoCall.load_all_news()
    for news in news:
        news.save()