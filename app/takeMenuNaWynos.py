from urllib.request import urlopen
from bs4 import BeautifulSoup
import Models

mainMenuHTML = urlopen("https://www.portel.pl/nawynos/kuchnia/pizza")
bsMainMenu = BeautifulSoup(mainMenuHTML.read(), 'html.parser')
allRestaurantsArr = []
allRestaurantLinks = []
averageSize = [40, 32, 40, 32, 37, 34, 30, 30, 36, 42, 35, 37, 40, 41, 32, 30]
averagePrice = []
pizzaName = []
pizzaPrice = []

Models.createAndDrop()
restaurantNameHTML = bsMainMenu.find_all("h2")

for div in bsMainMenu.find_all("div", class_='rest'):
    for a in div.find_all("a", href=True):
        allRestaurantLinks.append("https://www.portel.pl" + a['href'])

for x in restaurantNameHTML:
    slicedName = x.get_text().strip()
    allRestaurantsArr.append(slicedName)
allRestaurantsArr.pop(0)


def getPizzaName(restaurantId):
    restaurantSite = urlopen(allRestaurantLinks[restaurantId])
    bsRestaurant = BeautifulSoup(restaurantSite.read(), 'html.parser')
    pizzaNameHTML = bsRestaurant.find_all("div", class_='nazwa')
    for x in pizzaNameHTML:
        slicedName = x.get_text().strip()
        pizzaName.append(slicedName)


def getPizzaPrice(restaurantId):
    tempAvgPrice = 0
    restaurantSite = urlopen(allRestaurantLinks[restaurantId])
    bsRestaurant = BeautifulSoup(restaurantSite.read(), 'html.parser')
    pizzaPriceHTML = bsRestaurant.find_all("div", attrs={'data-cena': True})
    for x in range(len(pizzaPriceHTML)):
        pizzaPrice.append(pizzaPriceHTML[x].attrs["data-cena"])

    for y in range(len(pizzaPrice)):
        tempAvgPrice += float(pizzaPrice[y])
    averagePrice.append(tempAvgPrice / len(pizzaPrice))


for x in range(len(allRestaurantsArr)):
    getPizzaPrice(x)
    getPizzaName(x)

Models.insertMenu(allRestaurantsArr, pizzaName, pizzaPrice)
