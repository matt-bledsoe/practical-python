# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
n_months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if n_months >= extra_payment_start_month and n_months <= extra_payment_end_month :
        # Make an extra payment for the first 12 months
        principal = principal * (1 + rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    n_months += 1
    print(f"{n_months:>3} {round(total_paid, 2):>10,.2f} {round(principal, 2):>10,.2f}")

print(f"Total paid: {total_paid:,.2f}")
print(f"Number of months: {n_months:>3}")
