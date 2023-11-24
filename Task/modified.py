import requests
from bs4 import BeautifulSoup


def check_year(url1, url2):
    page1 = requests.get(url1)
    soup1 = BeautifulSoup(page1.content, 'html.parser')

    page2 = requests.get(url2)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    # print(soup)
    mydivs1 = soup1.find("h2", string="Breed specifics")
    mydivs2 = soup2.find("h2", string="Breed Specifics")
    print(mydivs1, "|||||", mydivs2)

    if "years" in mydivs1.parent.prettify() and "years" in mydivs2.parent.prettify():
        result = "no difference"
    else:
        result = "year in both links is not present"
    return result


try:
    print(check_year("https://www.royalcanin.com/us/cats/breeds/breed-library/asian",
          "https://rh-sc-rlt-weu-01.rlt.royalcanin.com/us/cats/breeds/Abyssinian"))


except AttributeError:
    print("Year is missing")


def check_icon(url1, url2):
    page1 = requests.get(url1)
    soup1 = BeautifulSoup(page1.content, 'html.parser')

    page2 = requests.get(url2)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    # print(soup)
    mydivs1 = soup1.find("h2", string="Key facts")
    mydivs2 = soup2.find("h2", string="Key facts")
    print(mydivs1, "|||||", mydivs2)

    if "rc-icon" in mydivs1.parent.prettify() and "rc-icon" in mydivs2.parent.prettify():
        result = "no difference"
    else:
        result = "icon in both links is not present"
    return result


try:
    print(check_icon("https://www.royalcanin.com/us/cats/breeds/breed-library/asian",
          "https://rh-sc-rlt-weu-01.rlt.royalcanin.com/us/cats/breeds/Abyssinian"))


except AttributeError:
    print("Iconis missing")