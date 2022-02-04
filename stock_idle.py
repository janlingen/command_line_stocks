from time import sleep
import os
import information_filter
import os
from rich import print
from rich.panel import Panel
from tabulate import tabulate


# Recommended Version !!!


def symbol(suggestion):
    lst = information_filter.get_symbol_suggestions(suggestion)
    for x in lst:
        print(
            f"[red]-->[/red] [green]{x[0]}[/green] [red]>>[/red] [bold][blue]{x[1]}[/blue][/bold]")


def name(symbol):
    data = information_filter.get_name(symbol)
    print(f"[red]-->[/red] [green]{data}[/green]")


def marketcap(symbol):
    data = information_filter.get_marketcap(symbol)
    print(
        f"[red]-->[/red] [green]{data[0]}[/green] [green]{data[1]}[/green]")


def price(symbol):
    data = information_filter.get_price(symbol)
    print(
        f"[red]-->[/red] [green]{data[0]}[/green] [green]{data[1]}[/green]")


def trailingpe(symbol):
    data = information_filter.get_trailing_pe(symbol)
    print(f"[red]-->[/red] [green]{data}[/green]")


def forwardpe(symbol):
    data = information_filter.get_forward_pe(symbol)
    print(f"[red]-->[/red] [green]{data}[/green]")


def yeareps(symbol):
    data = information_filter.get_year_eps(symbol)
    print(
        f"[red]-->[/red] [green]{data[0]}[/green] [green]{data[1]}[/green]")


def yearpe(symbol):
    data = information_filter.get_year_pe(symbol)
    print(f"[red]-->[/red] [green]{data}[/green]")


def twoav(symbol):
    data = information_filter.get_two_hundred_day_average(symbol)
    print(
        f"[red]-->[/red] [green]{data[0]}[/green] [green]{data[1]}[/green]")


def divyield(symbol):
    data = information_filter.get_trailing_dividend_yield(symbol)
    print(f"[red]-->[/red] [green]{data}[/green]")


def cmp(symbols):
    symbols_lst = symbols.split(",")
    print("[red]-[/red]"*105)
    lst = []
    for x in symbols_lst:
        lst.append(information_filter.get_stock(x))
    print(tabulate(lst, headers=["Name", "MarketCap",
          "Price", "TwoHundred Av.", "TrailingPE", "Div. Yield", "Currency"]))
    print("[red]-[/red]"*105)


def market():
    lst = information_filter.get_market()
    print(tabulate(lst))


def help():
    print(Panel(
        """    - find a symbol by typing [red]symbol suggestions [/red]
    - use a command followed by symbol
    - list of stock related commands:
    - [bold][magenta]name, marketcap, price, trailingpe, forwardpe, yeareps, yearpe, twoav, divyield[/magenta][/bold]
    - for example [red]price AAPL[/red]
    - to compare multiple stocks use: [red]cmp symbol_1,...,symbol_n[/red]
    - for a market overview [red]market[/red]
    - for help use [red]help[/red]
    - to clear the consol use [red]clear[/red]
    - to close the program use [red]quit[/red]""",
        title="[bold][green]:chart_increasing: Welcome to CommandLineStocks :chart_increasing:[/green][/bold]",
        expand=False))


def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def start():
    user_input = ""
    active = True
    while active:
        try:
            user_input = input(">>> ").split()
            if len(user_input) == 2:
                try:
                    eval(f"{user_input[0]}('{user_input[1]}')")
                except Exception:
                    print("[bold][red]Try again![/bold][/red]")
            elif user_input[0] == "market":
                market()
            elif user_input[0] == "help":
                help()
            elif user_input[0] == "clear":
                screen_clear()
            elif user_input[0] == "quit":
                active = False
            else:
                print("[bold][red]Try again![/bold][/red]")
        except:
            continue


if __name__ == "__main__":
    help()
    start()
