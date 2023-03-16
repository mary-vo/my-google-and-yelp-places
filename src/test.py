import requests
from bs4 import BeautifulSoup 

url = 'http://ufcstats.com/event-details/e4bb7e483c4ad318'
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')
test = soup.find_all('tr',class_='b-fight-details__table-row b-fight-details__table-row__hover js-fight-details-click')
# print(test)

fight_urls = []
for item in test:
    fight_urls.append(item['data-link'])
    print(fight_urls)