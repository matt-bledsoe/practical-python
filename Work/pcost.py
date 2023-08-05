# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                shares, price = int(record["shares"]), float(record["price"])
                total_cost += shares * price
            except ValueError:
                print(f"Row {rowno}. Couldn't parse", row)
    return(total_cost)

if len(sys.argv) == 2:
    filename = sys.argv[1]
    print(f"Using input filename: {filename}")
else:
    filename = "Data/portfolio.csv"
    print(f"Using default filename: {filename}")

cost = portfolio_cost(filename)
print(f"Total cost: ${cost:,.2f}")
