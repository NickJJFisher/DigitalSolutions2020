Hours = int(input("How many hours were you travelling?: "))
Speed = int(input("At what speed per kilometer per hour were you travelling?: "))
x = 0
while x < Hours:
    x = x + 1
    distance = x * Speed
    print (distance)
