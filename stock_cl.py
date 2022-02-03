import typer
import information_filter
from rich import print
from tabulate import tabulate

app = typer.Typer()


@app.command()
def symbol(suggestion: str):
    lst = information_filter.get_symbol_suggestions(suggestion)
    for x in lst:
        print(
            f"[red]-->[/red] [green]{x[0]}[/green] [red]>>[/red] [bold][blue]{x[1]}[/blue][/bold]")


@app.command()
def name(symbol: str):
    data = information_filter.get_name(symbol)
    print(f"[red]-->[/red] [green]{data}[/green]")


@app.command()
def marketcap(symbol: str):
    data = information_filter.get_marketcap(symbol)
    print(
        f"[red]-->[/red] [green]{data[0]}[/green] [green]{data[1]}[/green]")


@app.command()
def price(symbol: str):
    data = information_filter.get_price(symbol)
    print(
        f"[red]-->[/red] [green]{data[0]}[/green] [green]{data[1]}[/green]")


@app.command()
def trailingpe(symbol: str):
    data = information_filter.get_trailing_pe(symbol)
    print(f"[red]-->[/red] [green]{data}[/green]")


@app.command()
def forwardpe(symbol: str):
    data = information_filter.get_forward_pe(symbol)
    print(f"[red]-->[/red] [green]{data}[/green]")


@app.command()
def yeareps(symbol: str):
    data = information_filter.get_year_eps(symbol)
    print(
        f"[red]-->[/red] [green]{data[0]}[/green] [green]{data[1]}[/green]")


@app.command()
def yearpe(symbol: str):
    data = information_filter.get_year_pe(symbol)
    print(f"[red]-->[/red] [green]{data}[/green]")


@app.command()
def twoav(symbol: str):
    data = information_filter.get_two_hundred_day_average(symbol)
    print(
        f"[red]-->[/red] [green]{data[0]}[/green] [green]{data[1]}[/green]")


@app.command()
def divyield(symbol: str):
    data = information_filter.get_trailing_dividend_yield(symbol)
    print(f"[red]-->[/red] [green]{data} %[/green]")


@app.command()
def cmp(symbols: str):
    symbols_lst = symbols.split(",")
    print("[red]-[/red]"*105)
    lst = []
    for x in symbols_lst:
        lst.append(information_filter.get_stock(x))
    print(tabulate(lst, headers=["Name", "MarketCap",
          "Price", "TwoHundred Av.", "TrailingPE", "Div. Yield", "Currency"]))
    print("[red]-[/red]"*105)


if __name__ == "__main__":
    app()
