import bs4 as bs
import urllib.request

# THIS ONE IS NOT PERFECT, THEY HAVE OTHER THINGS INSIDE THE DIV TAG WE ARE PULLING P TAGS FROM

scraped_data = urllib.request.urlopen('https://www.nbcnews.com/tech/internet/facial-recognition-s-dirty-little-secret-millions-online-photos-scraped-n981921')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('div', class_='body___2BbXy publico-txt f4 f5-m lh-copy gray-100')

article_text = ""

for p in paragraphs:
    article_text += p.text

print(article_text)
