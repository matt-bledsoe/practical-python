# pcost.py
#
# Exercise 1.27
import report

def portfolio_cost(filename):
    """
    Computes the total cost (shares * price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    return sum([s.cost for s in portfolio])

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f"Usage: {argv[0]} portfoliofile")
    filename = argv[1]
    print(f"Total cost: ${portfolio_cost(filename):,.2f}")

if __name__ == "__main__":
    import sys
    main(sys.argv)