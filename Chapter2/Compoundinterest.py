P = int(input("the principal amount that was originally deposited into the account:"))
r = int(input("the annual interest rate: "))
n = int(input("the number of times per year that the interest is compounded: "))
t = int(input("the specified number of years: "))

print ("Your compound interest is", P * (1 + (r / n) ** (n * t)))