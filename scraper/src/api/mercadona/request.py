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

endpoints = [("https://tienda.mercadona.es/api/categories/216", Categories.BABY),
             ("https://tienda.mercadona.es/api/categories/59", Categories.BAKERY),
             ("https://tienda.mercadona.es/api/categories/60", Categories.BAKERY),
             ("https://tienda.mercadona.es/api/categories/62", Categories.BAKERY),
             ("https://tienda.mercadona.es/api/categories/64", Categories.BAKERY),
             ("https://tienda.mercadona.es/api/categories/164", Categories.BEER),
             ("https://tienda.mercadona.es/api/categories/166", Categories.BEER),
             ("https://tienda.mercadona.es/api/categories/75", Categories.BUTTER_AND_MARGARINE),
             ("https://tienda.mercadona.es/api/categories/86", Categories.CACAO_AND_SOLUBLES),
             ("https://tienda.mercadona.es/api/categories/78", Categories.CEREALS),
             ("https://tienda.mercadona.es/api/categories/48", Categories.CHARCUTERIE),
             ("https://tienda.mercadona.es/api/categories/49", Categories.CHARCUTERIE),
             ("https://tienda.mercadona.es/api/categories/50", Categories.CHARCUTERIE),
             ("https://tienda.mercadona.es/api/categories/51", Categories.CHARCUTERIE),
             ("https://tienda.mercadona.es/api/categories/52", Categories.CHARCUTERIE),
             ("https://tienda.mercadona.es/api/categories/58", Categories.CHARCUTERIE),
             ("https://tienda.mercadona.es/api/categories/53", Categories.CHEESE),
             ("https://tienda.mercadona.es/api/categories/54", Categories.CHEESE),
             ("https://tienda.mercadona.es/api/categories/56", Categories.CHEESE),
             ("https://tienda.mercadona.es/api/categories/92", Categories.CHOCOLATE),
             ("https://tienda.mercadona.es/api/categories/81", Categories.COFFEE),
             ("https://tienda.mercadona.es/api/categories/83", Categories.COFFEE),
             ("https://tienda.mercadona.es/api/categories/84", Categories.COFFEE),
             ("https://tienda.mercadona.es/api/categories/79", Categories.COOKIES),
             ("https://tienda.mercadona.es/api/categories/80", Categories.COOKIES),
             ("https://tienda.mercadona.es/api/categories/126", Categories.CREAMS),
             ("https://tienda.mercadona.es/api/categories/130", Categories.CREAMS),
             ("https://tienda.mercadona.es/api/categories/106", Categories.DESSERT),
             ("https://tienda.mercadona.es/api/categories/110", Categories.DESSERT),
             ("https://tienda.mercadona.es/api/categories/111", Categories.DESSERT),
             ("https://tienda.mercadona.es/api/categories/77", Categories.EGGS),
             ("https://tienda.mercadona.es/api/categories/163", Categories.ENERGETIC_ISOTONIC_DRINKS),
             ("https://tienda.mercadona.es/api/categories/31", Categories.FISH),
             ("https://tienda.mercadona.es/api/categories/34", Categories.FISH), # Frozen
             ("https://tienda.mercadona.es/api/categories/36", Categories.FISH),
             ("https://tienda.mercadona.es/api/categories/789", Categories.FISH),
             ("https://tienda.mercadona.es/api/categories/145", Categories.FROZEN),
             ("https://tienda.mercadona.es/api/categories/147", Categories.FROZEN),
             ("https://tienda.mercadona.es/api/categories/148", Categories.FROZEN),
             ("https://tienda.mercadona.es/api/categories/149", Categories.FROZEN),
             ("https://tienda.mercadona.es/api/categories/150", Categories.FROZEN),
             ("https://tienda.mercadona.es/api/categories/151", Categories.FROZEN),
             ("https://tienda.mercadona.es/api/categories/152", Categories.FROZEN),
             ("https://tienda.mercadona.es/api/categories/154", Categories.FROZEN),
             ("https://tienda.mercadona.es/api/categories/155", Categories.FROZEN),
             ("https://tienda.mercadona.es/api/categories/884", Categories.FROZEN),
             ("https://tienda.mercadona.es/api/categories/27", Categories.FRUITS),
             ("https://tienda.mercadona.es/api/categories/99", Categories.JUICE),
             ("https://tienda.mercadona.es/api/categories/100", Categories.JUICE),
             ("https://tienda.mercadona.es/api/categories/143", Categories.JUICE),
             ("https://tienda.mercadona.es/api/categories/98", Categories.JUICE),
             ("https://tienda.mercadona.es/api/categories/181", Categories.LIQUEURS),
             ("https://tienda.mercadona.es/api/categories/37", Categories.MEAT),
             ("https://tienda.mercadona.es/api/categories/38", Categories.MEAT),
             ("https://tienda.mercadona.es/api/categories/40", Categories.MEAT),
             ("https://tienda.mercadona.es/api/categories/42", Categories.MEAT),
             ("https://tienda.mercadona.es/api/categories/43", Categories.MEAT),
             ("https://tienda.mercadona.es/api/categories/44", Categories.MEAT),
             ("https://tienda.mercadona.es/api/categories/45", Categories.MEAT),
             ("https://tienda.mercadona.es/api/categories/46", Categories.MEAT),
             ("https://tienda.mercadona.es/api/categories/47", Categories.MEAT), # Frozen
             ("https://tienda.mercadona.es/api/categories/72", Categories.MILK),
             ("https://tienda.mercadona.es/api/categories/112", Categories.OIL_AND_VINEGAR),
             ("https://tienda.mercadona.es/api/categories/65", Categories.PATISSERIE),
             ("https://tienda.mercadona.es/api/categories/66", Categories.PATISSERIE),
             ("https://tienda.mercadona.es/api/categories/68", Categories.PATISSERIE),
             ("https://tienda.mercadona.es/api/categories/69", Categories.PATISSERIE),
             ("https://tienda.mercadona.es/api/categories/138", Categories.PIZZA),
             ("https://tienda.mercadona.es/api/categories/122", Categories.PRESERVES),
             ("https://tienda.mercadona.es/api/categories/123", Categories.PRESERVES),
             ("https://tienda.mercadona.es/api/categories/127", Categories.PRESERVES),
             ("https://tienda.mercadona.es/api/categories/140", Categories.READY_MEALS),
             ("https://tienda.mercadona.es/api/categories/142", Categories.READY_MEALS),
             ("https://tienda.mercadona.es/api/categories/897", Categories.READY_MEALS),
             ("https://tienda.mercadona.es/api/categories/118", Categories.RICE_PASTA_AND_LEGUMES),
             ("https://tienda.mercadona.es/api/categories/120", Categories.RICE_PASTA_AND_LEGUMES),
             ("https://tienda.mercadona.es/api/categories/121", Categories.RICE_PASTA_AND_LEGUMES),
             ("https://tienda.mercadona.es/api/categories/116", Categories.SAUCES),
             ("https://tienda.mercadona.es/api/categories/117", Categories.SAUCES),
             ("https://tienda.mercadona.es/api/categories/32", Categories.SEAFOOD),
             ("https://tienda.mercadona.es/api/categories/132", Categories.SNACKS),
             ("https://tienda.mercadona.es/api/categories/133", Categories.SNACKS),
             ("https://tienda.mercadona.es/api/categories/135", Categories.SNACKS),
             ("https://tienda.mercadona.es/api/categories/158", Categories.SODA),
             ("https://tienda.mercadona.es/api/categories/159", Categories.SODA),
             ("https://tienda.mercadona.es/api/categories/162", Categories.SODA),
             ("https://tienda.mercadona.es/api/categories/129", Categories.SOUPS),
             ("https://tienda.mercadona.es/api/categories/115", Categories.SPICES),
             ("https://tienda.mercadona.es/api/categories/89", Categories.SUGAR),
             ("https://tienda.mercadona.es/api/categories/90", Categories.SWEETS),
             ("https://tienda.mercadona.es/api/categories/95", Categories.SWEETS),
             ("https://tienda.mercadona.es/api/categories/97", Categories.SWEETS),
             ("https://tienda.mercadona.es/api/categories/833", Categories.SWEETS),
             ("https://tienda.mercadona.es/api/categories/168", Categories.SUMMER_WINE),
             ("https://tienda.mercadona.es/api/categories/161", Categories.TONIC),
             ("https://tienda.mercadona.es/api/categories/28", Categories.VEGETABLES),
             ("https://tienda.mercadona.es/api/categories/29", Categories.VEGETABLES),
             ("https://tienda.mercadona.es/api/categories/156", Categories.WATER),
             ("https://tienda.mercadona.es/api/categories/169", Categories.WINE),
             ("https://tienda.mercadona.es/api/categories/170", Categories.WINE),
             ("https://tienda.mercadona.es/api/categories/171", Categories.WINE),
             ("https://tienda.mercadona.es/api/categories/173", Categories.WINE),
             ("https://tienda.mercadona.es/api/categories/174", Categories.WINE),
             ("https://tienda.mercadona.es/api/categories/103", Categories.YOGHOURTS),
             ("https://tienda.mercadona.es/api/categories/104", Categories.YOGHOURTS),
             ("https://tienda.mercadona.es/api/categories/105", Categories.YOGHOURTS),
             ("https://tienda.mercadona.es/api/categories/107", Categories.YOGHOURTS),
             ("https://tienda.mercadona.es/api/categories/108", Categories.YOGHOURTS),
             ("https://tienda.mercadona.es/api/categories/109", Categories.YOGHOURTS),
            ]

# Functions

def get_category(endpoint: (), categories: []):
    try:
            request = requests.get(endpoint[0])
            products = parser(json.loads(request.text), store)
            category = next((_category for _category in categories if _category.id == get_index_from_enum(Categories, endpoint[1])), None)
            if type(category) is Category and len(products) > 0:
                category.products.extend(products)
    except Exception as error:
        print("[error][mecadona.py][get_category]", error, "->", endpoint[0])

def get_mercadona(categories: []):
    for endpoint in endpoints:
        get_category(endpoint, categories)