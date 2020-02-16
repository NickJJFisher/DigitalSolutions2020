P = float(input("the principal amount that was originally deposited into the account:"))
r = float(input("the annual interest rate: "))
n = float(input("the number of times per year that the interest is compounded: "))
t = float(input("the specified number of years: "))

print ("Your compound interest is", P * (1 + (r / n) ** (n * t)))