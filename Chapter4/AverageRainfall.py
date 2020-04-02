years = int(input("How many years?"))
x = 0
t = 0
rain = set()
while x < years:
    while t < 12:
        s = int(input("How much rain in this month (in ml): "))
        t = t + 1
        rain.add(s)
    x = x + 1
print ("This includes", 12 * years, "months")
rain = list(rain)
d = 0
c = 0
while d < years * 12:
    c = rain[d] + c
    d = d + 1
print ("Average rain per month: ", c/(years * 12))
print ("Total rainfall is ", c)