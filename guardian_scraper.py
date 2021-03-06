import bs4 as bs
import urllib.request
import re

url = 'https://www.theguardian.com/environment/2019/mar/29/can-the-world-quench-chinas-bottomless-thirst-for-milk'
scraped_data = ''

def guardian_scraper(url):
    scraped_data = urllib.request.urlopen(url)
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article,'lxml')

    paragraphs = parsed_article.find_all('div', class_='content__article-body from-content-api js-article__body')

    article_text = ''

    for p in paragraphs:
        article_text += p.text


    # put unwanted words to be replaced in the dictionary
    badwords = {'Facebook': '', 'Twitter': '', 'Email': '', 'LinkedIn': '', 'WhatsApp': '', 'Messenger': '', 'Pinterest': '', 'Share via': '', 'Share on': '', 'Read more': ''}

    # this section of code replaces substrings that matches the key with the keyvalue from the dictionary
    badwords = dict((re.escape(k), v) for k, v in badwords.items())
    pattern = re.compile("|".join(badwords.keys()))
    cleaned_text = pattern.sub(lambda m: badwords[re.escape(m.group(0))], article_text)

    return cleaned_text

fatty = guardian_scraper(url)
print(fatty)