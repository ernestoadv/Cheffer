from currency_converter import CurrencyConverter

# Determines the conversion rate between two currencies
def get_currency_conversion(currency_1: str, currency_2: str):
    try:
        currency_converter = CurrencyConverter()
        return currency_converter.convert(1, currency_1, currency_2)
    except Exception as error:
        print("[error][functions.py][get_currency_conversion]", error, "->", currency_1, ",", currency_2)
        return 1


# Calculates the index of an item in an enum
def get_index_from_enum(enum_list, enum_item):
    try:
        return list(enum_list).index(enum_item)
    except Exception as error:
        print("[error][functions.py][get_index_from_enum]", error)
        return -1

# Retrieve a value from an object 
# The key is a string separated by commas
def get_value_from_key(key, data):
    try:
        _data = data
        for _key in key.split('.'):
            _data = _data[_key]
        return _data
    except Exception as error:
        print("[error][functions.py][get_value_from_key]", error, "->", key, ",", data)
        return -1

# Retrieve a value from an object 
# The key is a list of strings
def get_value_from_list(keys, data):
    try:
        if keys:
            return get_value_from_list(keys[1:], data[keys[0]])
        else:
            return data
    except Exception as error:
        print("[error][functions.py][get_value_from_list]", error, "->", keys, ",", data)
        return -1
    
# Limits the decimals displayed in a float
def limit_float(value: float, decimals: int):
    try:
        value = round(value, decimals)
        if float.is_integer(value):
            return int(value)
        else:
            return float("{:.2f}".format(value))
    except Exception as error:
        print("[error][functions.py][limit_float]", error, "->", value)
        return value or 0
    
    