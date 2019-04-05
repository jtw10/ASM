import bs4 as bs
import urllib.request

scraped_data = urllib.request.urlopen('https://www.cbc.ca/parents/learning/view/fortnite-kids-playing-is-ok-by-me')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('div', class_='view-entry')

article_text = ""

for p in paragraphs:
    article_text += p.text

print(article_text)
