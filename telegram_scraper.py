import bs4 as bs
import urllib.request
import re

url = 'https://www.thetelegram.com/news/local/2019-snow-crab-catch-limits-announced-297823/' # sample url

def telegram_scraper(url):
    scraped_data = urllib.request.urlopen(url)
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article,'lxml')

    paragraphs = parsed_article.find_all('div', class_='article-content')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    # put unwanted words to be replaced in the dictionary
    badwords = {'Facebook': '', 'Twitter': '', 'Email': '', 'LinkedIn': '', 'WhatsApp': '', 'Messenger': '', 'Pinterest': '', 'Share via': '', 'Share on': '', 'Read more': ''}

    # this section of code replaces substrings that matches the key with the keyvalue from the dictionary
    badwords = dict((re.escape(k), v) for k, v in badwords.items())
    pattern = re.compile("|".join(badwords.keys()))
    cleaned_text = pattern.sub(lambda m: badwords[re.escape(m.group(0))], article_text)

    return article_text
