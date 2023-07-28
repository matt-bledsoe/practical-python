# bounce.py
#
# Exercise 1.5
height = 100.0
rebound_pct = 3/5
n_bounces = 10

while n_bounces > 0:
    height *= rebound_pct
    print(round(height, 4))
    n_bounces -= 1

