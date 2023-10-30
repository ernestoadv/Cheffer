from .__extend__ import Enum
from .__meta__ import Meta
from enum import auto

class Category(Enum, metaclass = Meta):
    BEER = auto()
    BUTCHER = auto()
    CHARCUTERIE = auto()
    CHEESE = auto()
    ENERGETIC_ISOTONIC_DRINKS = auto() 
    FISH = auto() 
    FRUITS = auto() 
    JUICE = auto() 
    LIQUEURS = auto() 
    OIL_AND_VINEGAR  = auto() 
    OTHER_DRINKS  = auto() 
    SAUCES = auto() 
    SEAFOOD = auto() 
    SODA  = auto() 
    SPICES = auto() 
    SUMMER_WINE = auto() 
    TONIC  = auto() 
    VEGETABLES  = auto() 
    WATER  = auto() 
    WINE  = auto() 