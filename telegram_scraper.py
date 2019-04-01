import bs4 as bs
import urllib.request

scraped_data = urllib.request.urlopen('https://www.thetelegram.com/news/welcome-to-canada-70-years-on-296385/')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('div', class_='article-content')

article_text = ""

for p in paragraphs:
    article_text += p.text

print(article_text)
