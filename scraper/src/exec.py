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

scraper = Scraper()

# Check what supermarkets we will retrieve information from

parser = argparse.ArgumentParser(description='Fetch supermarkets\' products.')
parser.add_argument("--all", const=True, default=False, help = 'Obtains data from all sites', nargs='?', type=bool)
parser.add_argument("--alcampo", const=True, default=False, help = 'Obtains data from Alcampo', nargs='?', type=bool)
parser.add_argument("--carrefour", const=True, default=False, help = 'Obtains data from Carrefour', nargs='?', type=bool)
parser.add_argument("--dia", const=True, default=False, help = 'Obtains data from Dia', nargs='?', type=bool)
parser.add_argument("--mercadona", const=True, default=False, help = 'Obtains data from Mercadona', nargs='?', type=bool)

# Request supermarkets' products

args = parser.parse_args()

if args.alcampo or args.all:
    # scraper.alcampo()
    pass

if args.carrefour or args.all:
    # scraper.carrefour()
    pass

if args.dia or args.all:
    # scraper.dia()
    pass

if args.mercadona or args.all:
    scraper.mercadona()
    pass
    
if not (args.alcampo or args.carrefour or args.dia or args.mercadona or args.all):
    print("\n Usage: scrap.py --all, --alcampo | --carrefour | --dia | --mercadona")
    print("\n No arguments provided. Finishing process.")
    
else:
    # Store retreived data in a JSON file
    dir = '../output/'
    write_json(dir, scraper)