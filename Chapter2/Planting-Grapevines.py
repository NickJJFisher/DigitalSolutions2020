r = int(input ("Enter the Length of the rows in feet: "))
e = int(input ("Enter the amount of space used by an end-post assembly: "))
s = int(input ("Enter the space between vines: "))
v = ((r - 2 * e)/s)

print ("The number of grapevines that will fit in the row is", v // 1)