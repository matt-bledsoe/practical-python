# report.py
#
# Exercise 2.4
import fileparse
import stock

def read_portfolio(filename):
    with open(filename, "rt") as file:
        portdict = fileparse.parse_csv(file,
                                        select=["name", "shares", "price"],
                                        types=[str, int, float])
        portfolio = [stock.Stock(d["name"], d["shares"], d["price"]) for d in portdict]
    return portfolio

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

def print_report(report):
    headers = ("Name", "Shares", "Price", "Change")
    header_string = ""
    for h in headers:
        header_string += f"{h:>10s} "

    print(header_string)
    print(4 * ((10 * "-") + " "))
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} ${price:9.2f} {change:>10.2f}")

    return

def portfolio_report(portfolio_filename, prices_filename):

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

    return

def main(argv):
    portfolio_report(argv[1], argv[2])

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
