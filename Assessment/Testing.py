#Imports
import random
from guizero import App, Picture, PushButton, Window, TextBox, Text
#app = App(layout="grid", height= 682, width= 1024, title= "Score the cards!")
app = App(height= 682, width= 1024, title= "Score the cards!",bg= "#00FFFF")

score = 0
players = 0
scoremsg = str("Theres something wrong with your code nick u idiot")
addcheck = "F"
subcheck = "F"
inputcheck = "pholder"
RHeart = list(range(1, 13))
RDiamo = list(range(1, 13))
BSpade = list(range(1, 13))
BClove = list(range(1, 13))
p1total = 0
p2total = 0
p1score = 0
p2score = 0
p1field = "pholder"
p2field = "pholder"
cardList = [RHeart, RDiamo, BSpade, BClove]

#Create seperate windows
window = Window(app, title="Player Select",  height= 682, width= 1024, bg= "#00FFFF")
window2 = Window(app, title="+1", height= 682, width= 1024, bg= "#FFB6C1", layout= "grid")
window3 = Window(app, title="-1",  height= 682, width= 1024, bg= "#FFB6C1", layout= "grid")
window4 = Window(app, title="+2",  height= 682, width= 1024, bg= "#FFB6C1", layout= "grid")
window5 = Window(app, title="-2", height= 682, width= 1024, bg= "#FFB6C1", layout= "grid")
window6 = Window(app, title="Correct", height= 682, width= 1024, layout= "grid")
window7 = Window(app, title="Incorrect!", height= 682, width= 1024, layout= "grid")
window8 = Window(app, title="Incorrect!", height= 682, width= 1024, layout= "grid")

#Hide all windows
def reset():
    window.hide()
    window2.hide()
    window3.hide()
    window4.hide()
    window5.hide()
    window6.hide()
    window7.hide()
    window8.hide()
reset()
#Functions
def ShowWTwo():
    reset()
    window2.show()
def ShowWThr():
    reset()
    window3.show()
def ShowWFou():
    reset()
    window4.show()
def ShowWFiv():
    reset()
    window5.show()
def HomePage():
    global score
    global scoremsg
    global addcheck
    global subcheck
    global inputcheck
    global cardList
    global RHeart
    global RDiamo
    global BSpade
    global BClove
    global players
    global p1score
    global p1total
    global p2score
    global p2total
    global p1field
    global p2field

    score = 0
    players = 1
    scoremsg = str("Theres something wrong with your code nick u idiot")
    addcheck = "F"
    subcheck = "F"
    inputcheck = "pholder"
    RHeart = list(range(1, 13))
    RDiamo = list(range(1, 13))
    BSpade = list(range(1, 13))
    BClove = list(range(1, 13))
    cardList = [RHeart, RDiamo, BSpade, BClove]
    reset()
    app.show()
    p1total = 0
    p2total = 0
    p1score = 0
    p2score = 0
    p1field = "pholder"
    p2field = "pholder"
def Addition():
    global addcheck
    addcheck = "T"
    window.show()
    app.hide()


def Subtraction():
    global subcheck
    subcheck = "T"
    window.show()
    app.hide()

def OnePlayer():
    global players
    players = 1
    if addcheck == "T":
        DisplayTwo()
        ShowWTwo()
    elif subcheck == "T":
        window3.show()
        DisplayTwo()
    app.hide()
def TwoPlayer():
    global players
    players = 2
    if addcheck == "T":
        DisplayTwo()
        ShowWFou()
    elif subcheck == "T":
        DisplayTwo()
        ShowWFiv()
    app.hide()

def DisplayTwo():
    suite1 = random.randint(0,3) #Define suites randomly
    suite2 = random.randint(0,3)
    suite3 = random.randint(0,3) #Define suites randomly
    suite4 = random.randint(0,3)
    random.shuffle(RDiamo) #Shuffle each suite
    random.shuffle(RHeart)
    random.shuffle(BClove)
    random.shuffle(BSpade)
    cardno1 = cardList[suite1][0] #choose cards
    cardno2 = cardList[suite2][1]
    cardno3 = cardList[suite3][2] #choose cards
    cardno4 = cardList[suite4][3]
    card1val = cardno1 + 13*(suite1) #display card as the suite
    card2val = cardno2 + 13*(suite2)
    card3val = cardno3 + 13*(suite3) #display card as the suite
    card4val = cardno4 + 13*(suite4)
    randCard1 = "Images/" + str(card1val) + ".png" #define what card is going to be displayed
    randCard2 = "Images/" + str(card2val) + ".png"
    randCard3 = "Images/" + str(card3val) + ".png" #define what card is going to be displayed
    randCard4 = "Images/" + str(card4val) + ".png"
    picture1 = Picture(window2, image=randCard1, grid = [2,1]) #define the picture
    picture2 = Picture(window2, image=randCard2, grid = [2,2])
    picture3 = Picture(window3, image=randCard1, grid=[2, 1])  # define the picture
    picture4 = Picture(window3, image=randCard2, grid=[2, 2])

    picture5 = Picture(window4, image=randCard1, grid = [2,1]) #define the picture
    picture6 = Picture(window4, image=randCard2, grid = [2,2])
    picture7 = Picture(window4, image=randCard3, grid = [4,1]) #define the picture
    picture8 = Picture(window4, image=randCard4, grid = [4,2])

    picture9 = Picture(window5, image=randCard1, grid = [2,1]) #define the picture
    picture10 = Picture(window5, image=randCard2, grid = [2,2])
    picture11 = Picture(window5, image=randCard3, grid = [4,1]) #define the picture
    picture12 = Picture(window5, image=randCard4, grid = [4,2])

    # define the picture
    global total
    global inputcheck
    global p1field
    global p2field
    global p1total
    global p2total
    if players == 1:
        if addcheck == "T":
            total = cardList[suite1][0] + cardList[suite2][1]
            ShowWTwo() #Displaying addition1
            inputcheck = checkbox
        if subcheck == "T":
            total = cardList[suite1][0] - cardList[suite2][1]
            ShowWThr()
            inputcheck = checkbox2
        print(total)
    if players == 2:
        if addcheck == "T":
            p1total = cardList[suite1][0] + cardList[suite2][1]
            p2total = cardList[suite3][2] + cardList[suite4][3]
            ShowWFou()
            p1field = checkbox3
            p2field = checkbox4
        if subcheck == "T":
            p1total = cardList[suite1][0] - cardList[suite2][1]
            p2total = cardList[suite3][2] - cardList[suite4][3]
            ShowWFiv()
            p1field = checkbox5
            p2field = checkbox6
        print(p1total)
        print(p2total)

    if suite1 == 0:
        RDiamo.remove(cardno1)
    if suite1 == 1:
        RHeart.remove(cardno1)
    if suite1 == 2:
        BSpade.remove(cardno1)
    if suite1 == 3:
        BClove.remove(cardno1)
    if suite2 == 0:
        RDiamo.remove(cardno2)
    if suite2 == 1:
        RHeart.remove(cardno2)
    if suite2 == 2:
        BSpade.remove(cardno2)
    if suite2 == 3:
        BClove.remove(cardno2)

def Check():
    global scoremsg
    global score
    global p1dis
    global p2dis
    global p1score
    global p2score
    if players == 1:
        if int(inputcheck.value) == total:
            score = score + 1
            reset()
            window6.show()
        elif int(inputcheck.value) != total:
            reset()
            window7.show()
        scoremsg = ("Your Score Is: ", score)
        Score = Text(window6, text=scoremsg, color="#000000", font="Ariel", size="50", grid = [1,3])
        Score1 = Text(window7, text=scoremsg, color="#000000", font="Ariel", size="50", grid = [1,3])
    if players == 2:
        print(p1total)
        print(p2total)
        if int(p1field.value) == p1total:
            p1score = p1score + 1
        if int(p2field.value) == p2total:
            p2score = p2score + 1
        p1dis = ("Player One Scored: ", p1score)
        p2dis = ("Player Two Scored: ", p2score)
        Dis = Text(window8, text=p1dis, color="#000000", font="Ariel", size="10", grid = [0,1])
        Dis1 = Text(window8, text=p2dis, color="#000000", font="Ariel", size="10", grid = [0,2])
        reset()
        window8.show()



#Main Menu
Title = Text(app, text="Score the Cards!", color="#000000", font="Ariel", size="50", align= "top")
Formatting = Text(app, text="LLLLLLL", color="#00FFFF", font="Ariel", size="75", align= "left")
Formatting2 = Text(app, text="LLLLLLL", color="#00FFFF", font="Ariel", size="75", align= "right")
PushButton(app, command=Addition, align= "left", text = "Addition")
PushButton(app, command=Subtraction, align = "right", text= "Subtraction")


#Player Select
Title = Text(window, text="Score the Cards!", color="#000000", font="Ariel", size="50", align= "top")
Formatting = Text(window, text="LLLLL", color="#00FFFF", font="Ariel", size="50", align= "left")
Formatting2 = Text(window, text="LLLLL", color="#00FFFF", font="Ariel", size="50", align= "right")
PushButton(window, command=OnePlayer, align= "left", text = "One Player")
PushButton(window, command=TwoPlayer,  align = "right", text= "Two Player")
PushButton(window, command=HomePage, text= "Home", align = "bottom")

#Adding single player
Title = Text(window2, text="Single Player Addition", color="#000000", font="Ariel", size="50", grid=[0,1])
PushButton(window2, command=Check,  text="Check", grid=[2,4])
checkbox = TextBox(window2, grid=[2,3])
PushButton(window2, command=DisplayTwo, text="Again", grid=[1,2])
PushButton(window2, command=HomePage, text= "Home", grid= [3,5])

#taking single player
Title = Text(window3, text="Single Player Subtraction", color="#000000", font="Ariel", size="50", grid=[0,1])
PushButton(window3, command=Check,  text="Check", grid=[2,4])
checkbox2 = TextBox(window3, grid=[2,3])
PushButton(window3, command=DisplayTwo, text="Again", grid=[1,2])
PushButton(window3, command=HomePage, text= "Home", grid= [3,5])

#taking 2 player
Title = Text(window5, text="2 Player Subtraction", color="#000000", font="Ariel", size="50", grid=[0,1])
PushButton(window5, command=Check,  text="Check", grid=[3,4])
checkbox5 = TextBox(window5, grid=[2,3])
checkbox6 = TextBox(window5, grid=[4,3])
PushButton(window5, command=DisplayTwo, text="Again", grid=[1,2])
PushButton(window5, command=HomePage, text= "Home", grid= [3,5])

#Adding 2 player
Title = Text(window4, text="2 Player Addition", color="#000000", font="Ariel", size="50", grid=[0,1])
PushButton(window4, command=Check,  text="Check", grid=[3,4])
checkbox3 = TextBox(window4, grid=[2,3])
checkbox4 = TextBox(window4, grid=[4,3])
PushButton(window4, command=DisplayTwo, text="Again", grid=[1,2])
PushButton(window4, command=HomePage, text= "Home", grid= [3,5])



#Correct
Title = Text(window6, text="Correct!", color="#000000", font="Ariel", size="50", grid = [1,1])
PushButton(window6, command=DisplayTwo,  text="Again?", grid = [1,2])
PushButton(window6, command=HomePage, text= "Home", grid= [3,5])


#Incorrect
Title = Text(window7, text="Incorrect!", color="#000000", font="Ariel", size="50", grid = [1,1])
PushButton(window7, command=DisplayTwo,  text="Again?", grid = [1,2])
PushButton(window7, command=HomePage, text= "Home", grid= [3,5])

#2 Player
Title = Text(window8, text="Results", color="#000000", font="Ariel", size="50", grid = [0,0])
PushButton(window8, command=HomePage, text= "Home", grid = [3,4])
PushButton(window8, command=DisplayTwo,  text="Again?", grid = [3,5])

app.display()
