L1 = int(input("Enter the length of the first rectangle: "))
W1 = int(input("Enter the width of the first triangle: "))
L2 = int(input("Enter the length of the second triangle: "))
W2 = int(input("Enter the width of the second triangle: "))
R1 = (L1*W1)
R2 = (L2 * W2)
if R1 > R2:
    print ("Rectangle 1 is larger")
elif R1 == R2:
    print ("Same")
else:
    print ("Rectangle 2 is larger")