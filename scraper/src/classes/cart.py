import json
from .product import Product

class CartProduct: 
    product: Product
    quantity: int

    def __init__(self, product):
        self.product = product
        self.quantity = 1

    def __str__(self):
        string = "\n\t" + str(self.product)
        string += "\n\t* Quantity: " + str(self.quantity)
        string += "\n\t* Total: " + str(self.quantity * self.product.price) + self.product.currency
        return string


class Cart:
    products: []
    total: float

    def __init__(self, name, currency):
        self.currency = currency
        self.name = name
        self.products = []
        self.total = 0
                
    def __json__(self):
        return json.dumps(self, default=lambda x: x.__dict__)

    def __str__(self):
        string = "> Cart:\n"
        if len(self.products) < 1:
            string += " Empty"
        else:
            string += "\n"
            string +=  "* Total: " + str(self.total) + self.currency + "\n"
            string +=  "* Products: \n"
            for product in self.products:
                string += str(product) + "\n"
        return string

    def add_product(self, product):
        if type(product) is not Product:
            print("[error][cart.py][add_product] Could not add given product. Wrong type:\n\n\t" + str(product) + "\n")
        elif any(_cart_p.product.id == product.id for _cart_p in self.products):
            cart_p = next((_cart_p for _cart_p in self.products if _cart_p.product.id == product.id), None)
            if type(cart_p) is CartProduct:
                cart_p.quantity += 1
                self.total += cart_p.product.price
            else:
                print("[error][cart.py][add_product] Could not add given product. Product not found:\n\n\t" + str(product) + "\n")

        else:
            cart_p = CartProduct(product)
            self.products.append(cart_p)
            self.total += cart_p.product.price

    def remove_product(self, product, delete = False):
        if type(product) is not Product:
            print("[error][cart.py][remove_product] Could not remove given product. Wrong type:\n\n\t" + str(product) + "\n")
        elif any(_cart_p.product.id == product.id for _cart_p in self.products):
            _product = next((_cart_p for _cart_p in self.products if _cart_p.product.id == product.id), None)
            if type(_product) is CartProduct:
                if delete:
                    self.total -= _product.product.price * _product.quantity
                    self.products[:] = [_cart_p for _cart_p in self.products if _cart_p.product is not product]
                else:
                    _product.quantity -= 1
                    self.total -= _product.product.price
                    if (_product.quantity < 1):
                        self.products[:] = [_cart_p for _cart_p in self.products if _cart_p.product is not product]
            else:
                print("[error][cart.py][add_product] Could not remove given product. Product not found:\n\n\t" + str(product) + "\n")
                return
        else:
            print("[error][cart.py][remove_product] Could not remove given product. Product not found:\n\n\t" + str(product) + "\n")