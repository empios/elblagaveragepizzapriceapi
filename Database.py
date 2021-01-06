from peewee import *

db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Restaurant(BaseModel):
    name = CharField()
    calculated = DecimalField()


class Menu(BaseModel):
    restaurant = ForeignKeyField(Restaurant, backref='restaurant')
    name = CharField()
    price = DecimalField()


db.connect()
db.drop_tables([Restaurant, Menu])
db.create_tables([Restaurant, Menu])
