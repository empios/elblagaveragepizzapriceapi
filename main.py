from fastapi import FastAPI
import calculatePizzaSize

app = FastAPI()


@app.get("/")
async def root():
    calculatePizzaSize.calculateSurfaceOverPrice()
    return {"pizzapricebysurface": calculatePizzaSize.allPizzaPriceBySurface}
