import bs4 as bs
import urllib.request

scraped_data = urllib.request.urlopen('https://www.cbc.ca/radio/thecurrent/sea-urchins-are-devouring-haida-gwaii-s-kelp-forest-so-ecologists-are-smashing-them-1.5068006')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('div', class_='story')

article_text = ""

for p in paragraphs:
    article_text += p.text

print(article_text)
