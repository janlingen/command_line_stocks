from raw_data_provider import get_stock_data, get_symbol_suggestions_data


def validate_data(data):
    if len(data["quoteResponse"]["result"]) == 0:
        raise Exception("Data is not valid, try again!")


def get_name(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    return data["quoteResponse"]["result"][0].get("shortName", "noName")


def get_marketcap(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    marketcap = data["quoteResponse"]["result"][0].get("marketCap", 0)
    currency = data["quoteResponse"]["result"][0].get("currency", "none")
    return (marketcap, currency)


def get_price(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    price = data["quoteResponse"]["result"][0].get("ask", 0)
    if price == 0:
        price = data["quoteResponse"]["result"][0].get("preMarketPrice", 0)
    currency = data["quoteResponse"]["result"][0].get("currency", 0)
    return (price, currency)


def get_trailing_pe(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    return data["quoteResponse"]["result"][0].get("trailingPE", 0)


def get_forward_pe(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    return data["quoteResponse"]["result"][0].get("forwardPE", 0)


def get_year_eps(symbol):
    data = get_stock_data(symbol)
    eps = data["quoteResponse"]["result"][0].get("epsCurrentYear", 0)
    currency = data["quoteResponse"]["result"][0].get("currency", "none")
    validate_data(data)
    return (eps, currency)


def get_year_pe(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    return data["quoteResponse"]["result"][0].get("priceEpsCurrentYear", 0)


def get_trailing_dividend_yield(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    return "{:.2f}".format(data["quoteResponse"]["result"][0].get("trailingAnnualDividendYield", 0)*100) + " %"


def get_two_hundred_day_average(symbol):
    data = get_stock_data(symbol)
    validate_data(data)
    average = data["quoteResponse"]["result"][0].get("twoHundredDayAverage", 0)
    currency = data["quoteResponse"]["result"][0].get("currency", "none")
    return (average, currency)


def get_symbol_suggestions(suggestion):
    data = get_symbol_suggestions_data(suggestion)
    data = data["quotes"]
    suggestions = []
    for x in data:
        name = x.get("shortname", "noName")
        symbol = x.get("symbol", "noSymbol")
        suggestions.append((name, symbol))
    return suggestions


def get_stock(symbol):
    data = get_stock_data(symbol)
    name = data["quoteResponse"]["result"][0].get("shortName", "noName")
    marketcap = data["quoteResponse"]["result"][0].get("marketCap", 0)
    price = data["quoteResponse"]["result"][0].get("ask", 0)
    if price == 0:
        price = data["quoteResponse"]["result"][0].get("preMarketPrice", 0)
    twoav = data["quoteResponse"]["result"][0].get("twoHundredDayAverage", 0)
    trailingpe = data["quoteResponse"]["result"][0].get("trailingPE", 0)
    currency = data["quoteResponse"]["result"][0].get("currency", "none")
    divyield = "{:.2f}".format(data["quoteResponse"]["result"][0].get(
        "trailingAnnualDividendYield", 0)*100) + " %"
    return [name, marketcap, price, twoav, trailingpe, divyield, currency]
