from src import AutoCall

if __name__ == "__main__":
    news = AutoCall.load_all_news()
    exit()
    for news in news:
        print(news)