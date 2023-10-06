# report.py
#
# Exercise 2.4
import fileparse
from stock import Stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename, **opts):
    with open(filename, "rt") as file:
        portdict = fileparse.parse_csv(file,
                                        select=["name", "shares", "price"],
                                        types=[str, int, float],
                                        **opts)
        portfolio = [Stock(**d) for d in portdict]
    return Portfolio(portfolio)

def read_prices(filename):
    with open(filename, "rt") as file:
        prices = dict(fileparse.parse_csv(file, types=[str, float],
                                        has_headers=False))
    return prices

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        name = holding.name
        current_price = prices[name]
        line = (name, holding.shares, current_price, current_price - holding.price)
        report.append(line)
    return report

def print_report(report, formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change)
    tuples
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)
    return

def portfolio_report(portfolio_filename, prices_filename, fmt="txt"):

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

    return

def main(argv):
    portfolio_report(argv[1], argv[2], argv[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)
# initial_value, current_value = 0.0, 0.0
# for holding in portfolio:
#     initial_value += holding["shares"] * holding["price"]
#     current_value += holding["shares"] * prices[holding["name"]]

# print(f"The initial value of the portfolio was: {initial_value:,.2f}")
# print(f"The current value of the portfolio is: {current_value:,.2f}")
# print(f"The gain/loss is: {current_value - initial_value:,.2f}")
