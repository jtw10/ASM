import bs4 as bs
import urllib.request

scraped_data = urllib.request.urlopen('https://www.ctvnews.ca/politics/you-might-get-a-text-from-andrew-scheer-telling-you-to-fill-your-gas-tank-1.4355710')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('div', class_='articleBody')

article_text = ""

for p in paragraphs:
    article_text += p.text

print(article_text)
