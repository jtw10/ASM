import bs4 as bs
import urllib.request

scraped_data = urllib.request.urlopen('https://abcnews.go.com/International/wireStory/thousands-protest-anniversary-brazils-coup-62077492')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('div', class_='StoryBody__main--1VIBe fonts__tiemposTextRegular--1u6HI')

article_text = ""

for p in paragraphs:
    article_text += p.text

print(article_text)
