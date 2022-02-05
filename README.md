# CommandLineStocks
As we all know, comparing stocks is often an essential process when deciding where to invest our money. If we don't have an expensive tool like Bloomberg or something else, we have to open several tabs from Yahoo Finance or another website and jump back and forth to compare some key values of different stocks. This little tool aims to solve this problem by making it easier to access and compare raw data.

![Screenshot](example1.png)

## how to install:
  - install needed packages
    - `pip install -r requirements.txt`
  - create an account at https://www.yahoofinanceapi.com/dashboard to get your `API TOKEN`
    - write the API TOKEN into `service/.env`
  - you can do 100 free requests a day

## how to use CommandLineStocks:
  - there are two versions
  - :heavy_exclamation_mark:Important: run `python app.py`:heavy_exclamation_mark:
  - list of commands:
      - `help` to show all commands and instructions
      - `clear` to clear the terminal
      - `market` to get a market overview
      - `quit` to end the program
      - `symbol name`, finds the symbol for a given stockname, for example symbol Microsoft
      - `name symbol`, returns the companys name, for example name MSFT
      - `price symbol`
      - `marketcap symbol`
      - `trailingpe symbol`
      - `forwardpe symbol`
      - `yeareps symbol`
      - `yearpe symbol`
      - `twoav symbol`
      - `divyield symbol`
      - `cmp symbol_1,...,symbol_n`, compares multiple stocks in a table