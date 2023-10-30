from classes.product import Product
from classes.store import Store
from enums.currency import Currency

def parser(data, store: Store):
    products = []
    sub_categories = data['categories']
    for sub_category in sub_categories:
        sub_category_products = sub_category['products']
        for sub_category_product in sub_category_products:
            try:
                id = store.id + "_" + sub_category_product['id']
                name = sub_category_product['display_name']
                price = float(sub_category_product['price_instructions']['unit_price'])
                currency = Currency.EUR
                size = sub_category_product['price_instructions']['unit_size']
                size_format = sub_category_product['price_instructions']['size_format']
                packaging = sub_category_product['packaging']
                products.append(Product(id, name, store, price, currency, size, size_format, packaging))
            except: 
                print("[error][mercadona][parser.py] Error when parsing product")
    return products