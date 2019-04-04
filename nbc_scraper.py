import bs4 as bs
import urllib.request
import re

# THIS ONE IS NOT PERFECT, THEY HAVE OTHER THINGS INSIDE THE DIV TAG WE ARE PULLING P TAGS FROM

# url = 'https://www.nbcnews.com/tech/internet/facial-recognition-s-dirty-little-secret-millions-online-photos-scraped-n981921' # sample url

def nbc_scraper(url):
    scraped_data = urllib.request.urlopen(url)
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article,'lxml')

    paragraphs = parsed_article.find_all('div', class_='body___2BbXy publico-txt f4 f5-m lh-copy gray-100')

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



dick = nbc_scraper(url)
print(dick)