import takeMenuNaWynos
import math
import Models

allPizzaSurface = []
allPizzaPriceBySurface = []
allRestaurantsArr = takeMenuNaWynos.allRestaurantsArr

def initFile():
    print("I am working")

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
Models.insertRes(allRestaurantsArr, allPizzaPriceBySurface)



