import requests
import bs4
import ftfy
import re
from src.base import Website, News
from markdownify import markdownify as md


class Seagate(Website):
    url = 'https://www.seagate.com/blog/'
    replacements = {
        "â": "—",  # En dash or em dash
        "â": "'",  # Possessive apostrophe
        "Â": "",     # Unnecessary character
    }

    def get_single_news(self, url: str) -> News:
        headers = {'Accept-Language': 'en'}
        response = requests.get(url, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        # get main div with the data
        main_div = soup.find('div', class_='AT-body')
        main_div = main_div.find('div', class_='body-content')
        markdown = md(str(main_div))

        for incorrect, correct in self.replacements.items():
                markdown = markdown.replace(incorrect, correct)

        pattern = r'(?<! )\[[^\]]*\]\([^\)]*\)'
        markdown = re.sub(pattern, r' \g<0>', markdown)
        
        return markdown
    
    def get_news(self) -> list[News]:
        headers = {'Accept-Language': 'en'}
        response = requests.get(self.url, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        cards = soup.find_all('li', class_='CardLayout-card')
        news = []
        for card in cards[1:4]:
            title = card.find('a', class_='card-title').text.strip()
            subtitle = card.find('p', class_='card-body').text.strip()
            image = "https://www.seagate.com" + card.find('img')['src']
            url = "https://www.seagate.com" + card.find('a', class_='card-title')['href']

            news.append(News(title=title, subtitle=subtitle, image=image, url=url, content=self.get_single_news(url), date="today"))

        return news
