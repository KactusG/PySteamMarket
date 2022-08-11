import requests

'''
TODO:
  * add all currencies supported by the Steam Marketplace to `curAbbrev`
  * create docstrings for all functions
  * listings parser; get total number of listings (`total_count` in JSON)
  * get price overview via http://steamcommunity.com/market/priceoverview/
'''

# Currency abbreviations
curAbbrev = {
    "USD": 1,  # United States dollar
    "GBP": 2,  # British pound sterling
    "EUR": 3,  # The euro
    "CHF": 4,  # Swiss franc
    "RUB": 5,  # Russian ruble
    "PLN": 6,  # Polish złoty
    "BRL": 7,  # Brazilian real
    "JPY": 8,  # Japanese yen
    "SEK": 9,  # Swedish krona
    "IDR": 10,  # Indonesian rupiah
    "MYR": 11,  # Malaysian ringgit
    "BWP": 12,  # Botswana pula
    "SGD": 13,  # Singapore dollar
    "THB": 14,  # Thai baht
    "VND": 15,  # Vietnamese dong
    "KRW": 16,  # South Korean won
    "TRY": 17,  # Turkish lira
    "UAH": 18,  # Ukrainian hryvnia
    "MXN": 19,  # Mexican Peso
    "CAD": 20,  # Canadian dollar
    "AUD": 21,  # Australian dollar
    "NZD": 22,  # New Zealand dollar
    "CNY": 23,  # Chinese yuan
    "INR": 24,  # Indian rupee
    "CLP": 25,  # Chilean peso
    "PEN": 26,  # Peruvian sol
    "COP": 27,  # Colombian peso
    "ZAR": 28,  # South African rand
    "HKD": 29,  # Hong Kong dollar
    "TWD": 30,  # New Taiwan dollar
    "SAR": 31,  # Saudi riyal
    "AED": 32  # United Arab Emirates dirham
}

def get_item(appid, name, currency='EUR'):
    r"""
    Gets item listings from the `Steam Marketplace`.

    @appid ID of game item belongs to.

    @name: Name of item to lookup.
    
    @currency: Abbreviation of currency to return listing prices in.
    Accepted currencies:`USD,GBP,EUR,CHF,RUB,KRW,CAD`
    
    Defaults to `EUR`.
    Please lookup the proper abbreviation for your currency of choice.
    
    Returns a json object
    Example:
    ```
    {
        "success": true,
        "lowest_price": "0,92€",
        "volume": "15",
        "median_price": "0,80€"
    }
    ```
    """
    url = 'http://steamcommunity.com//market/priceoverview'
    market_item = requests.get(url,params={
        'appid': appid,
        'market_hash_name': name,
        'currency': curAbbrev[currency]        
    })
    return market_item.json()

def get_multiple(items,appid=440,currency='EUR'):
    """Fetch multiple items using get_item()."""
    result ={}
    for item in items:
        result[item] = get_item(appid,item,currency)
    return result
def get_tf2_item(item, currency='EUR'):
    """Fetches an item from TF2. (Defaults the `appid` to 440)"""
    return get_item('440', item, currency)
def get_csgo_item(item, currency='EUR'):
    """Fetches an item from CSGO. (Defaults the `appid` to 730)"""
    return get_item('730', item, currency)
