import bs4 as bs
import urllib.request

url = 'https://abcnews.go.com/International/wireStory/thousands-protest-anniversary-brazils-coup-62077492'
scraped_data = ''

def abc_scraper(url):
    scraped_data = urllib.request.urlopen(url)
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article,'lxml')

    paragraphs = parsed_article.find_all('div', class_='StoryBody__main--1VIBe fonts__tiemposTextRegular--1u6HI')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    return article_text


fatty = abc_scraper(url)
print(fatty)
