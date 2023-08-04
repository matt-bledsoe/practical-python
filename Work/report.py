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

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        name = holding["name"]
        current_price = prices[name]
        line = (name, holding["shares"], current_price, current_price - holding["price"])
        report.append(line)
    return report

portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)

headers = ("Name", "Shares", "Price", "Change")
header_string = ""
for h in headers:
    header_string += f"{h:>10s} "

print(header_string)
print(4 * ((10 * "-") + " "))
for name, shares, price, change in report:
    print(f"{name:>10s} {shares:>10d} {price:10.2f} {change:>10.2f}")

initial_value, current_value = 0.0, 0.0
for holding in portfolio:
    initial_value += holding["shares"] * holding["price"]
    current_value += holding["shares"] * prices[holding["name"]]

print(f"The initial value of the portfolio was: {initial_value:,.2f}")
print(f"The current value of the portfolio is: {current_value:,.2f}")
print(f"The gain/loss is: {current_value - initial_value:,.2f}")
