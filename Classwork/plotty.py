import random
from guizero import App, Picture, PushButton
app = App()
def card():
    mylist = list(range(1,53)) #create list of 52 integars
    random.shuffle(mylist) #randomly shuffer
    cardNum = mylist[0]
    randCard = "PlayingCards/" + str(cardNum) + ".png"
    picture = Picture(app, image=randCard)
button = PushButton(app, command=card)

app.display()


#Using this string