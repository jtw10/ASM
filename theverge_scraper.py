import bs4 as bs
import urllib.request

scraped_data = urllib.request.urlopen('https://www.theverge.com/2019/3/31/18289518/google-maps-app-snakes-game-april-fools-day')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('div', class_='c-entry-content')

article_text = ""

for p in paragraphs:
    article_text += p.text

print(article_text)
