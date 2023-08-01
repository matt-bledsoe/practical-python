# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    total_cost = 0.0

    f = open(filename, "rt")
    headers = next(f)

    for line in f:
        row = line.split(",")
        row_cost = int(row[1]) * float(row[2])
        total_cost += row_cost

    f.close()
    return(total_cost)

cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost: ${cost:,.2f}")
