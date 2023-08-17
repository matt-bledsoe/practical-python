# pcost.py
#
# Exercise 1.27
import sys
import report

def portfolio_cost(filename):
    total_cost = 0.0
    portfolio = report.read_portfolio(filename)
    for record in portfolio:
        total_cost += record["shares"] * record["price"]
    return(total_cost)

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
        print(f"Using input filename: {filename}")
    else:
        filename = "Data/portfolio.csv"
        print(f"Using default filename: {filename}")

    cost = portfolio_cost(filename)
    print(f"Total cost: ${cost:,.2f}")

if __name__ == "__main__":
    main(sys.argv)