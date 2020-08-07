from fastapi import FastAPI
import takeMenuNaWynos
import calculatePizzaSize

app = FastAPI()


@app.get("/")
async def root():
    return {"pizzapricebysurface": calculatePizzaSize.allPizzaPriceBySurface}


@app.get("/restaurant")
async def restaurant():
    return {"restaurant": takeMenuNaWynos.allRestaurantsArr}
