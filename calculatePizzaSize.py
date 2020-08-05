from operator import index

import takeMenuNaWynos
import math

allPizzaSurface = []
allPizzaPriceBySurface = []


def calculateSize():
    for x in takeMenuNaWynos.averageSize:
        surface = 2 * math.pi * (x / 2)
        allPizzaSurface.append(surface)


def calculateSurfaceOverPrice():
    calculateSize()
    for x in allPizzaSurface:

        priceOverSurface = x/takeMenuNaWynos.averagePrice[allPizzaSurface.index(x)]
        allPizzaPriceBySurface.append(priceOverSurface)
