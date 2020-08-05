from fastapi import FastAPI
import calculatePizzaSize

app = FastAPI()


@app.get("/")
async def root():
    return {"pizzapricebysurface": calculatePizzaSize.allPizzaPriceBySurface}
