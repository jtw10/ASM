import urllib3
from bs4 import BeautifulSoup


urllib3.disable_warnings()
http = urllib3.PoolManager()
response = http.request('GET', 'https://www.cbc.ca/news/business/parents-wireless-charges-phone-1.5077272')


soup = BeautifulSoup(response.data, "html.parser")  # Note the use of the .data property


table = soup.findAll('div', attrs={"class":"story"})
for x in table:
    print(x.find('p').text)
