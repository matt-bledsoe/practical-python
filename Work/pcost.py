# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    total_cost = 0.0

    f = open(filename, "rt")
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        try:
            shares = int(row[1])
        except ValueError:
            print("Couldn't parse", line)
        try:
            price = float(row[2])
        except ValueError:
            print("Couldn't parse", line)
        row_cost = shares * price
        total_cost += row_cost

    f.close()
    return(total_cost)

cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost: ${cost:,.2f}")
