# Imports

import requests
from bs4 import BeautifulSoup

# Variables

userCountry = None
userCity = None
numDays = 0
dailyDay = None
date = None
impData = None
desc = None
secondaryData = None
dailyHigh = None
dailyLow = None
url_prefix = ""
a = 1
b = 0
d = 0
e = 0


# Functions


def defVar():
    global userCity
    global userCountry
    global numDays
    try:
        userCountry = str(input("Enter your preferred country: "))
        userCountry = userCountry.lower()
        userCity = str(input("Enter your preferred city: "))
        userCity = userCity.lower()
        numDays = int(
            input(
                "How many days of forecast are you interested in?\nEnter an input between 1 & 14: "
            )
        )
    except ValueError:
        print("Please Try Again With An Appropriate Value.")
        defVar()
    except AttributeError:
        print("An Error Occurred!\nPlease Try Again With An Appropriate Location.")
        defVar()


def checkNumDays():
    global numDays
    try:
        while numDays > 14 or numDays <= 0:
            numDays = int(
                input(
                    "\nYou have exceeded our data limit!\nPlease enter a valid input: "
                )
            )
    except ValueError:
        print("Please Try Again With An Appropriate Value.")
        defVar()
        checkNumDays()


def weatherData():
    global numDays
    global a
    global b
    global d
    global e
    global dailyDay
    global date
    global impData
    global desc
    global secondaryData
    global dailyHigh
    global dailyLow
    if userCountry == None and userCity == None:
        src = requests.get(f"https://www.timeanddate.com{url_prefix}/ext").text
    elif userCity != None and userCountry != None:
        src = requests.get(
            f"https://www.timeanddate.com/weather/{userCountry}/{userCity}/ext"
        ).text
    content = BeautifulSoup(src, "html.parser")
    table = content.find("table", id="wt-ext")
    twoWeeks = table.find("tbody")
    perDay = twoWeeks.find_all("tr")
    # Impdata Includes: DailyHigh, DailyLow, WindSpeed, Humidity
    impData = twoWeeks.find_all("td")
    # Secondarydata Includes: FeelsLike & PrecipitationChance
    secondaryData = twoWeeks.find_all("td", class_="sep")
    desc = twoWeeks.find_all("td", class_="small")
    for day in perDay:
        dailyDate = day.th.text
        dailyDay = day.th.span.text
        date = dailyDate.replace(dailyDay, "")
        dailyHigh = ((impData[a].text).split("/")[0] + "°C").replace(" ", "")
        dailyLow = (((impData[a].text).split("/")[1]).replace("\xa0", "")).strip()
        # if dailyDay == "Sun":
        #     dailyDay = "Sunday"
        # elif dailyDay == "Mon":
        #     dailyDay = "Monday"
        # elif dailyDay == "Tue":
        #     dailyDay = "Tuesday"
        # elif dailyDay == "Wed":
        #     dailyDay = "Wednesday"
        # elif dailyDay == "Thu":
        #     dailyDay = "Thursday"
        # elif dailyDay == "Fri":
        #     dailyDay = "Friday"
        # elif dailyDay == "Sat":
        #     dailyDay = "Saturday"
        print(f"{dailyDay}: {date}")
        print(dailyHigh)
        print(dailyLow)
        print(impData[a + 3].text)
        print(impData[a + 5].text)
        print(desc[d].text)
        print(secondaryData[b].text)
        print(secondaryData[b + 1].text)
        appendFile()
        a += 12
        b += 3
        d += 1
        print()


def appendFile():
    with open("tempData.txt", "a") as openedFile:
        openedFile.write(f"{dailyDay}: {date}\n")
        openedFile.write(dailyHigh + "\n")
        openedFile.write(dailyLow + "\n")
        openedFile.write(impData[a + 3].text + "\n")
        openedFile.write(impData[a + 5].text + "\n")
        openedFile.write(desc[d].text + "\n")
        openedFile.write(secondaryData[b].text + "\n")
        openedFile.write(secondaryData[b + 1].text + "\n\n")


if __name__ == "__main__":
    defVar()
    weatherData()
