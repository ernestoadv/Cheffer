from .__extend__ import Enum
from .__meta__ import Meta

class Store(Enum, metaclass = Meta):
    ALCAMPO = "Alcampo"
    CARREFOUR = "Carrefour"
    DIA = "Dia"
    MERCADONA = "Mercadona"