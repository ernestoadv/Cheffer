import json
from classes.app import App
from enums.config import Config
from enums.locale import Locale
from utils.functions import get_value_from_list

# Gets a specific literal from the literals JSON 
def get_literal(key: str):
    try:
        literal = get_value_from_list(key, literals)
        return literal
    except:
        print("[error][locale.py][get_literal] Error retrieving literal: ", key)
    return ''

# Loads literals based on config's selected locale
def load_locale(locale: Locale, update: bool):
        if locale in Locale:
            # Update config locale
            if update:
                App.set(Config.LOCALE, locale)
            # Load new set of literals
            with open(App.get(Config.ROOT) + "\\assets\\locale\\" + locale.value + ".json") as json_file:
                return json.load(json_file)
                
        else:
            print("[error][locale.py][load_locale] Unknown locale")

# Populate literals object
literals = load_locale(App.get(Config.LOCALE), False)