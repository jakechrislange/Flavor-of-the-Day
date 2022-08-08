#Flavor of the Day
from bs4 import BeautifulSoup
import requests
import webbrowser

koppsURL = requests.get('https://www.kopps.com/flavor-preview')
soupKopps = BeautifulSoup(koppsURL.content, 'lxml')
koppsFOD1 = soupKopps.find_all("span", class_ = "ribbon flavor-of-day")[0].text.lower()
koppsFOD2 = soupKopps.find_all("span", class_ = "ribbon flavor-of-day")[1].text.lower()

oscarsURL = requests.get('http://www.oscarscustard.com/')
soupOscars = BeautifulSoup(oscarsURL.content, 'lxml')
oscarsFOD = soupOscars.find('h5').text
oscarsFOD = oscarsFOD[oscarsFOD.index(":") +2:len(oscarsFOD)].lower();

name = input("What is your name?")
print("Hello " + name+ ", welcome to my flavor of the day finder!")

restaurantChoice = input("Would you like to see the flavor of the day for Oscar's or Kopp's (O/K)?")

if (restaurantChoice == "O"):
    print("At Oscars in Waukesha, the flavor of the day is " + oscarsFOD + "!")
    seeWeb = input("Would you like to go to Oscars's web page? (Yes/No)")
    if (seeWeb == "Yes"):
        url = 'http://www.oscarscustard.com/'
        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)
    else:
        print("Thanks for visiting, goodbye!")
elif (restaurantChoice == "K"):
    print("At Kopps in Brookfield, the flavor of the day is " + koppsFOD1 + " and " + koppsFOD2 + "!")
    seeWeb = input("Would you like to go to Kopp's web page? (Yes/No)")
    if (seeWeb == "Yes"):
        url = 'https://www.kopps.com/flavor-preview'
        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)
    else:
        print("Thanks for visiting, goodbye!")
else:
    print("Invalid Choice, I'll route you to google!")
    url = 'https://google.com'
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)

#end of program