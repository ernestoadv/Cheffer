from currency_converter import CurrencyConverter
# Determines the conversion rate between two currencies
def get_currency_conversion(currency_1: str, currency_2: str):
    currency_converter = CurrencyConverter()
    return currency_converter.convert(1, currency_1, currency_2)


# Calculates the index of an item in an enum
def get_index_from_enum(enum_list, enum_item):
    try:
        list(enum_list).index(enum_item)
    except:
        print("[error][functions.py][get_index_from_enum] Error when calculating index")

# Retrieve a value from an object 
# The key is a string separated by commas
def get_value_from_key(key, data):
    _data = data
    for _key in key.split('.'):
        _data = _data[_key]
    return _data

# Retrieve a value from an object 
# The key is a list of strings
def get_value_from_list(keys, data):
    if keys:
        return get_value_from_list(keys[1:], data[keys[0]])
    else:
        return data
    
# Limits the decimals displayed in a float
def limit_float(value: float, decimals: int):
    value = round(value, decimals)
    if float.is_integer(value):
         return int(value)
    else:
        return float("{:.2f}".format(value))
    