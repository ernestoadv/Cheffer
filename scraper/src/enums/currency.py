from .__extend__ import Enum
from .__meta__ import Meta

class Currency(Enum, metaclass = Meta):
    EUR = "€"
    USD = "$"