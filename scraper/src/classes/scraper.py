import json
# from api.alcampo.request import request as get_alcampo
# from api.carrefour.request import request as get_carrefour
# from api.dia.request import request as get_dia
from api.mercadona.request import get_mercadona
from classes.category import Category as Category
from enums.category import Category as Categories
from utils.locale import get_literal

class Scraper:
    categories: []
    
    def __init__(self):
        # Initialize product categories out of Categories enum
        self.categories = []
        for item in Categories:
            category = Category(item.value, item.name, get_literal(["CATEGORIES", item.name]))
            self.categories.append(category)
                
    def __json__(self):
        return  json.dumps(self, default=lambda x: x.__dict__)

    def __str__(self):
        string = "> Scraper:\n\n"
        string += "* Categories:" + "\n"
        for category in self.categories:
            string += "\n\t" + str(category) + "\n"
        return string
        
    def alcampo(self):
        # get_alcampo(self.categories)
        pass
        
    def carrefour(self):
        # get_carrefour(self.categories)
        pass
        
    def dia(self):
        # get_dia(self.categories)
        pass
        
    def mercadona(self):
        get_mercadona(self.categories)