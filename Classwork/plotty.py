#Imports
import random
from guizero import App, Picture, PushButton, Window, TextBox, Text

guessbox = int(0)
total = int(0)
#App and Window formatting
app = App(layout="grid")
window = Window(app, title="Second Window", layout="grid")
window2 = Window(app, title="Third Window", layout="grid")
window.hide()
window2.hide()

#Generations
picture = Picture (app, image="PlayingCards/1.png", grid= [0,1]) #placeholder
mylist = list(range(1,53)) #create list of 52 integars

#Functions
def card():
    random.shuffle(mylist) #randomly shuffer
    cardNum = mylist[0] #define card Number to the first on the list
    randCard = "PlayingCards/" + str(cardNum) + ".png" #define rankcard as file directory of a card
    picture = Picture(app, image=randCard, grid =[0,1]) #define the picture
    mylist.remove(cardNum)

def fourcard():
    random.shuffle(mylist) #randomly shuffer
    cardNum1 = mylist[0] #define card Number to the first on the list
    cardNum2 = mylist[1]  # define card Number to the second on the list
    cardNum3 = mylist[2]  # define card Number to the third on the list
    cardNum4 = mylist[3]  # define card Number to the fourth on the list
    randCard1 = "PlayingCards/" + str(cardNum1) + ".png"
    randCard2 = "PlayingCards/" + str(cardNum2) + ".png"
    randCard3 = "PlayingCards/" + str(cardNum3) + ".png"
    randCard4 = "PlayingCards/" + str(cardNum4) + ".png"#define rankcard as file directory of a card
    mylist.remove(cardNum1) #Remove the card just used from list
    mylist.remove(cardNum2)
    mylist.remove(cardNum3)
    mylist.remove(cardNum4)
    picture1 = Picture(app, image=randCard1, grid =[2,1]) #define the picture
    picture2 = Picture(app, image=randCard2, grid=[2, 2])  # define the picture
    picture3 = Picture(app, image=randCard3, grid=[2, 3])  # define the picture
    picture4 = Picture(app, image=randCard4, grid=[2, 4])  # define the picture
    total = cardNum1 + cardNum2 + cardNum3 + cardNum4
    Text(app, text=(total), grid=[6,6])
    guessbox = TextBox(app, grid=[3, 0])
    if len(mylist) == 0:
        window.show()
        app.hide()
def check():
    if guessbox == total:
        window2.show()
        app.hide()
    else:
        text = Text(app, text="Incorrect Guess", grid=[0, 3])
#App Display
PushButton(app, command=card, grid = [1,1], text = "Single")
PushButton(app, command=fourcard, grid = [1,2], text= "Four")
PushButton(app, command=check, grid=[3, 1], text="Check")

#Window1 Display
PushButton(window, grid = [1,1],image="dt.png", text= "Imagine being out of cards lol xd")

#Window2 Display
PushButton(window2, grid = [1,1], text= "Good Job")
#App Displays
app.display()


