import random
Number = random.randint(0,36)
a = (Number % 2)


if Number == 0:
    print("green", Number)
elif Number <= 10:
    if a == 1:
        print("red", Number)
    if a == 0:
        print("black", Number)
elif Number <= 18:
    if a == 1:
        print("black", Number)
    if a == 0:
        print("red", Number)
elif Number <= 28:
    if a == 1:
        print("red", Number)
    if a == 0:
        print("black", Number)
elif Number <= 36:
    if a == 1:
        print("black", Number)
    if a == 0:
        print("red", Number)
