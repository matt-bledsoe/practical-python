# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        portfolio = []
        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)
    
    return portfolio

def read_prices(filename):
    with open(filename, "r") as f:
        rows = csv.reader(f)
        prices = {}
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print(f"Couldn't parse: {row}")
    return prices

portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")


