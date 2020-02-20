No = int(input("Enter a weight in kilograms"))
We = No * 9.8
if We > 500:
    print ("It is too heavy")
if We < 100:
    print ("It is too light")
else:
    print ("It is okay")