import peewee

from Database import db


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Restaurant(BaseModel):
    name = peewee.CharField()
    calculated = peewee.DecimalField()


class Menu(BaseModel):
    restaurant = peewee.ForeignKeyField(Restaurant, backref='restaurant')
    name = peewee.CharField()
    price = peewee.DecimalField()


def createAndDrop():
    db.drop_tables([Restaurant, Menu])
    db.create_tables([Restaurant, Menu])


def insertMenu(allRestaurantsArr, pizzaName, pizzaPrice):
    with db.atomic():
        for x in allRestaurantsArr:
            for y, z in zip(pizzaName, pizzaPrice):
                Menu.create(restaurant=x, name=y, price=z)

