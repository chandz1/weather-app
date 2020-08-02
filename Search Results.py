# Imports:
import requests
from bs4 import BeautifulSoup

# Variables:
place = 'hyderabad'

# Functions:


def get_url():
    get_access = requests.get(
        f'https://www.timeanddate.com/weather/?query={place}').text
    src = BeautifulSoup(get_access, 'html.parser')
    table_data = src.find(
        'table', attrs={'class': 'zebra fw tb-theme'})
    all_places = table_data.find_all('tr')
    del all_places[0]
    for i in all_places:
        names = i.find('td')
        print(names.text)


get_url()
