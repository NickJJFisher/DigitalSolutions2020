D = int(input("Enter day: "))
M = int(input("Enter Month: "))
Y = int(input("Enter Year "))
print (D, "/", M, "/", Y)
if D * M == Y:
    print ("This is magic")
else:
    print ("This is not magic")