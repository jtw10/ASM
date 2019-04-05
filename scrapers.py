import bs4 as bs
import urllib.request
import re


def article_scraper(url):
    scraped_data = urllib.request.urlopen(url)
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article,'lxml')

    paragraphs = news_check(url, parsed_article)

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


def news_check(url, parsed_article):
    if 'theverge' in url:
        return parsed_article.find_all('div', class_='c-entry-content')
    elif 'theguardian' in url:
        return parsed_article.find_all('div', class_='content__article-body from-content-api js-article__body')
    elif 'abcnews' in url:
        return parsed_article.find_all('div', class_='StoryBody__main--1VIBe fonts__tiemposTextRegular--1u6HI')
    elif 'ctvnews' in url:
        return parsed_article.find_all('div', class_='articleBody')
    elif 'nbcnews' in url:
        return parsed_article.find_all('div', class_='body___2BbXy publico-txt f4 f5-m lh-copy gray-100')
