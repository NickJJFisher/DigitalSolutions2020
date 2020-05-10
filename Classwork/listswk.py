from random import randint

myList = list()
i = 0
while i < 50:
    num = randint(1, 100)
    print(num)
    myList.append(num)  # add an item to the end of the list
    i += 1
print(myList)

myList.remove(3)  # removes an item from list

print(myList)
myList.sort()
print(myList)

print(min(myList))
print(max(myList))