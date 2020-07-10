# Imports

import requests
from bs4 import BeautifulSoup

# Variables

userCountry = ''
userCountry = userCountry.lower()
userCity = ''
userCity = userCity.lower()
numDays = 0
a = 1
b = 0
c = 1
d = 0
e = 0


# Functions

def defVar():
    global userCity
    global userCountry
    global numDays
    try:
        userCountry = str(input('Enter your preferred country: '))
        userCountry = userCountry.lower()
        userCity = str(input('Enter your preferred city: '))
        userCity = userCity.lower()
        numDays = int(
            input('How many days of forecast are you interested in?\nEnter an input between 1 & 14: '))
    except ValueError:
        print('Please Try Again With An Appropriate Value.')
        defVar()
    except AttributeError:
        print('An Error Occurred!\nPlease Try Again With An Appropriate Location.')
        defVar()


def checkNumDays():
    global numDays
    try:
        while numDays > 14 or numDays <= 0:
            numDays = int(
                input('\nYou have exceeded our data limit!\nPlease enter a valid input: '))
    except ValueError:
        print('Please Try Again With An Appropriate Value.')
        defVar()
        checkNumDays()


def weatherData():
    global numDays
    global a
    global b
    global c
    global d
    global e
    try:
        src = requests.get(
            f'https://www.timeanddate.com/weather/{userCountry}/{userCity}/ext').text
        content = BeautifulSoup(src, 'html.parser')
        table = content.find('table', id='wt-ext')
        twoWeeks = table.find('tbody')
        perDay = twoWeeks.find_all('tr')
        # Impdata Includes: DailyHigh, DailyLow, WindSpeed, Humidity
        impData = twoWeeks.find_all('td')
        # Secondarydata Includes: FeelsLike & PrecipitationChance
        secondaryData = twoWeeks.find_all('td', class_='sep')
        desc = twoWeeks.find_all('td', class_='small')
        for day in perDay[0:numDays]:
            dailyDate = day.th.text
            dailyDay = day.th.span.text
            date = dailyDate.replace(dailyDay, '')
            print(f'{dailyDay}: {date}')
            print(impData[a].text)
            print(impData[a + 3].text)
            print(impData[a + 5].text)
            print(desc[b].text)
            print(secondaryData[b].text)
            print(secondaryData[c].text)
            a += 12
            b += 1
            c += 2
            print()
    except AttributeError:
        print('An Error Occurred!\nPlease Try Again With An Appropriate Location.')
        defVar()
        weatherData()
