import json
from enums.config import Config
from enums.currency import Currency
from enums.locale import Locale
from utils.functions import get_currency_conversion

class App:
  __config = {
    Config.CURRENCY.value: Currency.EUR,
    Config.LOCALE.value: Locale.ES,
    Config.ROOT.value: ""
  }
  __setters = [Config.CURRENCY, Config.LOCALE, Config.ROOT]

  def __init__(self, currency: Currency, locale: Locale, root: str) -> None:
      App.__config[Config.CURRENCY.value] = currency
      App.__config[Config.LOCALE.value] = locale
      App.__config[Config.ROOT.value] = root
                
  def __json__(self):
      return json.dumps(self, default=lambda x: x.__dict__)

  @staticmethod
  def get(name: Config):
    return App.__config[name.value]

  @staticmethod
  def set(name: Config, config: Currency | Locale | str):
    if name in App.__setters:
      App.__config[name.value] = config
    else:
      raise NameError("Name not accepted in set() method")