# Imports:
import requests
from bs4 import BeautifulSoup

# Variables:


# Functions:
def get_url():
    try:
        get_access = requests.get(
            f'https://www.timeanddate.com/weather/?query={place}').text
