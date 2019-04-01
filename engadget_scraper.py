import bs4 as bs
import urllib.request

scraped_data = urllib.request.urlopen('https://www.engadget.com/2019/03/30/apple-chip-designer-gerard-williams/')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('div', class_='article-text c-gray-1')

article_text = ""

for p in paragraphs:
    article_text += p.text

print(article_text)
