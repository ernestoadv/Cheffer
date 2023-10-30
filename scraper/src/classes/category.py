import json
from .product import Product

class Category:
    code: str
    id: str
    name: str
    products: []

    def __init__(self, id, code, name):
        self.code = code
        self.id = id
        self.name = name
        self.products = []
                
    def __json__(self):
        return json.dumps(self, default=lambda x: x.__dict__)

    def __str__(self):
        string = "> Category:\n\n"
        string += "\t* ID: " + self.id + "\n"
        string += "\t* Code: " + self.code + "\n"
        string += "\t* Name: " + self.name + "\n"
        string += "\t* Products:" + "\n"
        for product in self.products:
            string += "\n\t" + str(product) + "\n"
        return string
    
    def add_product(self, product):
        if type(product) is not Product:
            print("[error][category.py] Could not append given product. Wrong type:\n\n\t" + str(product) + "\n")
        elif product in self.products:
            print("[error][category.py] Could not append given product. This product already exists:\n\n\t" + str(product) + "\n")
        elif any(_product.id == product.id for _product in self.products):
            print("[error][category.py] Could not append given product. This product's id is already used:\n\n\t" + str(product) + "\n")
        else:
            self.products.append(product)

    def remove_product(self, product):
        if type(product) is not Product:
            print("[error][category.py] Could not add given product. Wrong type:\n\n\t" + str(product) + "\n")
        elif not any(_product.id == product.id for _product in self.products):
            print("[error][category.py] Could not remove given product. Product not found:\n\n\t" + str(product) + "\n")
        else:
            self.products[:] = [_product for _product in self.products if _product is not product]