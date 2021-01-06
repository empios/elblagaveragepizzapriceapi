import takeMenuNaWynos
import math
import Database

allPizzaSurface = []
allPizzaPriceBySurface = []


def calculateSize():
    for x in takeMenuNaWynos.averageSize:
        surface = 2 * math.pi * (x / 2)
        allPizzaSurface.append(surface)


def calculateSurfaceOverPrice():
    calculateSize()
    for x in allPizzaSurface:
        priceOverSurface = x / takeMenuNaWynos.averagePrice[allPizzaSurface.index(x)]
        allPizzaPriceBySurface.append(priceOverSurface)


calculateSurfaceOverPrice()

for x,y in zip(takeMenuNaWynos.allRestaurantsArr, allPizzaPriceBySurface):
    Database.Restaurant.create(name=x, calculated=y)
