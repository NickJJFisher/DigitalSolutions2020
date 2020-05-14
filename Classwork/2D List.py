list2D = [['Sarah', 4156, 23], ['Sam', 4000, 21], ['Terry', 4123, 17],
          ['Michael', 4100, 3], ['Frank', 4003, 12], ['Warren', 4300, 11],
          ['Samantha', 4165, 24], ['Will', 4034, 43], ['Ben', 4025, 54],
          ['Hudini', 4010, 19], ['Zach', 4540, 20], ['Sam', 4045, 45]] #Define list, with 3 items in each
print(list2D)
print(list2D[4][2]) #Franks age
print(list2D[1][1]) #Sams Postcode
print(len(list2D)) #Length of list
print(len(list2D[4])) # Length of 5th item in list

name = input("Who are you looking for?: ")

for i in range(len(list2D)): #Loop for every time in list
    if name == list2D[i][0]:
        for j in range(len(list2D[i])):
            print(list2D[i][1+j])


        # print(list2D[i])
        # print(list2D[i]) #Print sublist of loop sequence