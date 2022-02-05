from requests import request, get
from os import getenv
from dotenv import load_dotenv
import json


def get_stock_data(stock_symbol):
    load_dotenv()
    TOKEN = getenv("TOKEN")
    data = {}
    stocks = "https://yfapi.net/v6/finance/quote"
    headers = {'x-api-key': TOKEN}
    querystring = {"symbols": stock_symbol}
    response = request("GET", stocks, headers=headers, params=querystring)
    if response.status_code == 200:
        data = json.loads(response.text)
    return data


def get_symbol_suggestions_data(suggested_name):
    data = {}
    names = f"https://query2.finance.yahoo.com/v1/finance/search?q={suggested_name}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    response = get(names, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
    return data


def get_market_summary(region):
    load_dotenv()
    TOKEN = getenv("TOKEN")
    stocks = "https://yfapi.net/v6/finance/quote/marketSummary"
    headers = {'x-api-key': TOKEN}
    querystring = {"region": region}
    response = request("GET", stocks, headers=headers, params=querystring)
    if response.status_code == 200:
        data = json.loads(response.text)
    return data
