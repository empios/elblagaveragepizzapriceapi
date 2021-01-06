from fastapi import FastAPI
import calculatePizzaSize
import Database

app = FastAPI()

response = {'pizzapricebysurface': []}
response2 = {"restaurant": []}
restaurant = Database.Restaurant.select()
for rest in restaurant.dicts():
    response['pizzapricebysurface'].append(rest['name'])
    response2['restaurant'].append(rest['calculated'])




@app.get("/")
async def root():
    return response


@app.get("/restaurant")
async def restaurant():
    return response2
