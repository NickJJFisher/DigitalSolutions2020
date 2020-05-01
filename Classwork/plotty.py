import random
from guizero import App, Picture, PushButton
app = App()
picture = Picture (app, image="PlayingCards/1.png")
def card():
    mylist = list(range(1,53)) #create list of 52 integars
    random.shuffle(mylist) #randomly shuffer
    cardNum = mylist[0] #define card Number to the first on the list
    randCard = "PlayingCards/" + str(cardNum) + ".png" #define rankcard as file directory of a card
    picture = Picture(app, image=randCard) #define the picture
button = PushButton(app, command=card)
app.display()