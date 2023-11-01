""" 
    Aplicación: Scraper de productos de supermercados
    Autor: Ernesto Aranda del Valle
    Uso: Privado

    Este script realiza scraping de datos de productos de supermercados para uso privado.
    Ernesto Aranda del Valle es el autor de este programa.

    Cualquier uso que no esté autorizado expresamente por el autor está prohibido.
    Se prohíbe la reproducción, distribución o cualquier otro uso sin consentimiento.
"""

import argparse
import os
from classes.app import App
from enums.currency import Currency
from enums.locale import Locale
from utils.stream import write_json

# Before creating the scraper, we need to initialize the app's config

root = os.path.dirname(os.path.abspath(__file__))

App(Currency.EUR, Locale.ES, root)

# Scraper must be imported afterwards

from classes.scraper import Scraper

# Check what supermarkets we will retrieve information from

parser = argparse.ArgumentParser(description='Fetch supermarkets\' products.')
parser.add_argument("--all", const=True, default=False, help = 'Obtains data from all sites', nargs='?', type=bool)
parser.add_argument("--alcampo", const=True, default=False, help = 'Obtains data from Alcampo', nargs='?', type=bool)
parser.add_argument("--carrefour", const=True, default=False, help = 'Obtains data from Carrefour', nargs='?', type=bool)
parser.add_argument("--dia", const=True, default=False, help = 'Obtains data from Dia', nargs='?', type=bool)
parser.add_argument("--mercadona", const=True, default=False, help = 'Obtains data from Mercadona', nargs='?', type=bool)

args = parser.parse_args()

# If no supermarket is request on execution, print usage message
    
if not (args.alcampo or args.carrefour or args.dia or args.mercadona or args.all):
    print("\nUsage: scrap.py --all, --alcampo | --carrefour | --dia | --mercadona")
    print("\nNo arguments provided. Finishing process.")    

# Request and store supermarkets' products in a JSON file

else:
    
    dir = '../output/'
    if args.alcampo or args.all:
        # name = 'alcampo'
        # scraper = Scraper()
        # scraper.alcampo()
        # write_json(dir, name, scraper)
        print("\nThis supermarket is not available yet. Sorry for the inconvenience.")    
        print("\nFinishing process.")    
        pass

    if args.carrefour or args.all:
        # name = 'carrefour'
        # scraper = Scraper()
        # scraper.carrefour()
        # write_json(dir, name, scraper)
        print("\nThis supermarket is not available yet. Sorry for the inconvenience.")    
        print("\nFinishing process.")    
        pass

    if args.dia or args.all:
        # name = 'dia'
        # scraper = Scraper()
        # scraper.dia()
        # write_json(dir, name, scraper)
        print("\nThis supermarket is not available yet. Sorry for the inconvenience.")  
        print("\nFinishing process.")     
        pass

    if args.mercadona or args.all:
        name = 'mercadona'
        scraper = Scraper()
        scraper.mercadona()
        write_json(dir, name, scraper)
        pass