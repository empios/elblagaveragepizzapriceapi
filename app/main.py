from fastapi import *
import calculatePizzaSize
import Database
import Models

calculatePizzaSize.initFile()

app = FastAPI()

sleep_time = 150


async def reset_db_state():
    Database.db._state._state.set(Database.db_state_default.copy())
    Database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        Database.db.connect(reuse_if_open=True)
        yield
    finally:
        if not Database.db.is_closed():
            Database.db.close()


response = {'pizzapricebysurface': []}
response2 = {"restaurant": []}


@app.get("/", dependencies=[Depends(get_db)])
def root():
    restaurant = Models.Restaurant.select()
    for rest in restaurant.dicts():
        response['pizzapricebysurface'].append(rest['name'])
    return response


@app.get("/restaurant", dependencies=[Depends(get_db)])
def restaurant():
    restaurant = Models.Restaurant.select()
    for rest in restaurant.dicts():
        response2['restaurant'].append(rest['calculated'])
    return response2
