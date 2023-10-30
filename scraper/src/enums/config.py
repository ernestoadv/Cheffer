from .__extend__ import Enum
from .__meta__ import Meta

class Config(Enum, metaclass = Meta):
    BASE_CURRENCY = "base_currency"
    CURRENCY = "currency"
    LOCALE = "locale"
    ROOT = "root"