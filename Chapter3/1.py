number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
elif number == 0:
    print("even")
a = (number % 2)
if a == 1:
    print ("Odd")
if a == 0:
    print ("Even")
