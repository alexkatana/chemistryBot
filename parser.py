from bs4 import BeautifulSoup
import requests

src = 'https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4'
request = requests.get(src)
soup = BeautifulSoup(request.text, 'lxml')

th_table = soup.find('tbody').find_all('th', class_='plainlist')
tr_table = soup.find('tbody').find_all('td', class_='plainlist')
tr_table.pop(0)

for i in range(len(th_table)):
    (f'{th_table[i].text}:{tr_table[i].text}')
