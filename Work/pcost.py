# pcost.py
#
# Exercise 1.27

total_cost = 0.0

f = open("Data/portfolio.csv", "rt")
headers = next(f)

for line in f:
    row = line.split(",")
    row_cost = int(row[1]) * float(row[2])
    total_cost += row_cost

print(f"Total cost: ${total_cost:,.2f}")
f.close()
