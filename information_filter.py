from raw_data_provider import get_stock_data, get_symbol_suggestions_data


def validate_data(data):
    if len(data["quoteResponse"]["result"]) == 0:
        raise Exception("Data is not valid, try again!")


def get_name(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    return data["quoteResponse"]["result"][0]["shortName"]


def get_marketcap(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    marketcap = data["quoteResponse"]["result"][0]["marketCap"]
    currency = data["quoteResponse"]["result"][0]["currency"]
    return (marketcap, currency)


def get_price(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    price = data["quoteResponse"]["result"][0]["ask"]
    if price == 0:
        price = data["quoteResponse"]["result"][0]["preMarketPrice"]
    currency = data["quoteResponse"]["result"][0]["currency"]
    return (price, currency)


def get_trailing_pe(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    return data["quoteResponse"]["result"][0]["trailingPE"]


def get_forward_pe(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    return data["quoteResponse"]["result"][0]["forwardPE"]


def get_year_eps(symbol):
    data = get_stock_data(symbol)
    eps = data["quoteResponse"]["result"][0]["epsCurrentYear"]
    currency = data["quoteResponse"]["result"][0]["currency"]
    validate_data(data)
    return (eps, currency)


def get_year_pe(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    return data["quoteResponse"]["result"][0]["priceEpsCurrentYear"]


def get_trailing_dividend_yield(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    return "{:.2f}".format(data["quoteResponse"]["result"][0].get("trailingAnnualDividendYield", 0)*100) + " %"


def get_two_hundred_day_average(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    average = data["quoteResponse"]["result"][0]["twoHundredDayAverage"]
    currency = data["quoteResponse"]["result"][0]["currency"]
    return (average, currency)


def get_symbol_suggestions(suggestion):
    data = get_symbol_suggestions_data(suggestion)
    data = data["quotes"]
    suggestions = []
    for x in data:
        name = x.get("shortname", "no Name")
        symbol = x.get("symbol", "no Symbol")
        suggestions.append((name, symbol))
    return suggestions


def get_stock(symbol):
    data = get_stock_data(symbol)
    name = data["quoteResponse"]["result"][0]["shortName"]
    marketcap = data["quoteResponse"]["result"][0]["marketCap"]
    price = data["quoteResponse"]["result"][0]["ask"]
    if price == 0:
        price = data["quoteResponse"]["result"][0]["preMarketPrice"]
    twoav = data["quoteResponse"]["result"][0]["twoHundredDayAverage"]
    trailingpe = data["quoteResponse"]["result"][0]["trailingPE"]
    currency = data["quoteResponse"]["result"][0]["currency"]
    divyield = "{:.2f}".format(data["quoteResponse"]["result"][0].get(
        "trailingAnnualDividendYield", 0)*100) + " %"
    return [name, marketcap, price, twoav, trailingpe, divyield, currency]
