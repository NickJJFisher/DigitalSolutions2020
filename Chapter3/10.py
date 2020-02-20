penny = int(input("Enter the amount of pennies: "))
nickles = int (input("Enter the amount of Nickles"))
dimes = int(input("Enter the amount of Dimes"))
Quarters = int(input("Enter the amount of quarters"))

Money = (penny + nickles * 5 + dimes * 10 + Quarters * 25)
print (Money)
if Money > 100:
    print ("Your coins add to ", Money - 100, "over $1" )
if Money == 100:
    print ("Your coins add to $1" )
if Money < 100:
    print ("Your coins add to ", 100 - Money, "below $1" )
#Create a change-counting game that gets the user to enter the number of coins required
#to make exactly one dollar. The program should prompt the user to enter the number of
#pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one
#dollar, the program should congratulate the user for winning the game. Otherwise, the
#program should display a message indicating whether the amount entered was more than
#or less than one dollar.