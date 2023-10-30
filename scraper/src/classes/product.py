import json
from classes.app import App
from enums.config import Config
from enums.currency import Currency
from utils.functions import get_currency_conversion, limit_float
from .store import Store

class Product:
    id: str
    currency: str
    name: str
    packaging: str
    price: float
    size: float
    size_format: str
    store: Store

    def __init__(self, id, name, store, price, currency, size, size_format, packaging):
        self.id = id
        self.name = name
        self.store = store
        self.price = limit_float(price, 2)
        self.currency = currency.value
        self.size = limit_float(size, 2)
        self.size_format = size_format
        self.packaging = packaging
                
    def __json__(self):
        return json.dumps(self, default=lambda x: x.__dict__)

    def __str__(self):
        string = "> Product:\n\n"
        string += "\t\t* ID: " + self.id + "\n"
        string += "\t\t* Name: " + self.name + "\n"
        string += "\t\t* Store: " + self.store.name.value + "\n"
        string += "\t\t* Price: " + str(self.price  * get_currency_conversion(self.currency, App.get(Config.CURRENCY).name)) + App.get(Config.CURRENCY).value + "\n"
        string += "\t\t* Size: " + str(self.size) + self.size_format + "\n"
        string += "\t\t* Packaging: " + self.packaging
        return string