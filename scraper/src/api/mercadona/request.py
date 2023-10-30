import json
import requests
from .parser import parser
from classes.category import Category
from classes.store import Store as Store
from enums.category import Category as Categories
from enums.store import Store as Stores
from utils.functions import get_index_from_enum

# Initialize store

name = Stores.MERCADONA
index = get_index_from_enum(Stores, Stores.MERCADONA)
store = Store(index, name)

# Endpoints

endpoints = [("https://tienda.mercadona.es/api/categories/112", Categories.OIL_AND_VINEGAR),
             ("https://tienda.mercadona.es/api/categories/116", Categories.SAUCES),
             ("https://tienda.mercadona.es/api/categories/117", Categories.SAUCES),
             ("https://tienda.mercadona.es/api/categories/115", Categories.SPICES)
            ]

# Functions

def get_category(endpoint: (), categories: []):
    try:
            request = requests.get(endpoint[0])
            products = parser(json.loads(request.text), store)
            category = next((_category for _category in categories if _category.id == get_index_from_enum(Categories, endpoint[1])), None)
            if type(category) is Category and len(products) > 0:
                category.products.extend(products)
    except:
        print("[error][mecadona.py][get_category] Error when loading request: " + endpoint)

def get_mercadona(categories: []):
    for endpoint in endpoints:
        get_category(endpoint, categories)