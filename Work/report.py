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

initial_value, current_value = 0.0, 0.0
for holding in portfolio:
    initial_value += holding["shares"] * holding["price"]
    current_value += holding["shares"] * prices[holding["name"]]

print(f"The initial value of the portfolio was: {initial_value:,.2f}")
print(f"The current value of the portfolio is: {current_value:,.2f}")
print(f"The gain/loss is: {current_value - initial_value:,.2f}")
