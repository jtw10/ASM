import bs4 as bs
import urllib.request

url = 'https://abcnews.go.com/Politics/lori-lightfoot-makes-history-chicagos-african-american-female/story?id=62127007&cid=clicksource_4380645_null_headlines_hed'
scraped_data = ''

def abc_scraper(url):
    scraped_data = urllib.request.urlopen(url)
    scraped_data = urllib.request.urlopen('https://abcnews.go.com/International/wireStory/thousands-protest-anniversary-brazils-coup-62077492')
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article,'lxml')

    paragraphs = parsed_article.find_all('div', class_='StoryBody__main--1VIBe fonts__tiemposTextRegular--1u6HI')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    return article_text


fatty = abc_scraper(url)
print(fatty)
