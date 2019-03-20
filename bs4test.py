from bs4 import BeautifulSoup
import requests
# importing both Beautiful Soup and the Requests library

page_link = 'https://www.azlyrics.com/lyrics/edsheeran/perfect.html'
# url that to scrape from.

page_response = requests.get(page_link, timeout=5)
# fetch the content from the url, using the requests library

page_content = BeautifulSoup(page_response.content, "html.parser")
# parse the url content and store it in a variable via "html.parser" arguement

print(page_content)
# what's this?! ed sheeran lyrics?

title = page_content.title
print(title, type(title))
title = page_content.title.string
print(title, type(title))

para = page_content.text
print(para, type(para))
