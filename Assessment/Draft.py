#Import Modules
import random
from guizero import App, Picture, PushButton, Window, TextBox, Text

#Mainpage UI
app = App(height= 360, width= 520, title= "Score the cards!",bg= "#00FFFF")

#Define Variables which will be used in future
score = 0  #SP Score
players = 0 #Amount of Players
scoremsg = str("pholder") #Final Score Message
addcheck = False #Check addition gamemode
subcheck = False #Check subtraction gamemode
inputcheck = "pholder"
RHeart = list(range(1, 13)) #Different suites
RDiamo = list(range(1, 13))
BSpade = list(range(1, 13))
BClove = list(range(1, 13))
cardList = [RHeart, RDiamo, BSpade, BClove] # Create 2D list from previous 4 lists
#2 Player variables
p1total = 0
p2total = 0
p1score = 0
p2score = 0
p1field = "pholder"
p2field = "pholder"
cards = 52



#Functions

"""
Hide all windows
Calls on all the aforementioned windows
"""
def reset():
    window.hide()
    window2.hide()
    window3.hide()
    window4.hide()
    window5.hide()
    window6.hide()
    window7.hide()
    window8.hide()
"""
Hide all windows
Display Window 2
"""
def ShowWTwo():
    reset()
    window2.show()
"""
Hide all windows
Display Window 3
"""
def ShowWThr():
    reset()
    window3.show()
"""
Hide all windows
Display Window 4
"""
def ShowWFou():
    reset()
    window4.show()
"""
Hide all windows
Display Window 5
"""
def ShowWFiv():
    reset()
    window5.show()
"""
Globally use the variables defined at the beginning
Reset the variables back to startup values
"""
def HomePage():
    global score, scoremsg, addcheck, subcheck, inputcheck, cardList, RHeart, RDiamo, BSpade, BClove, players, p1score, p1total, p2score, p2total, p1field, cards, p2field
    cards = 52
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
""" 
Globally use Addcheck
Set addcheck to T permenantly 
Show the window required 
hide mainpage
"""
def Addition():
    global addcheck
    addcheck = True
    window.show()
    app.hide()
""" 
Globally use SubCheck
Set Subcheck to T permenantly 
Show the window required 
hide mainpage
"""
def Subtraction():
    global subcheck
    subcheck = True
    window.show()
    app.hide()
""" 
Globally use players, subcheck and addcheck
Define Players number
Shows/Hides required UI
"""
def OnePlayer():
    global players
    players = 1
    if addcheck == True:
        DisplayTwo()
        ShowWTwo()
    elif subcheck == True:
        window3.show()
        DisplayTwo()
    app.hide()
""" 
Globally use players, subcheck and addcheck
Define Players number
Shows/Hides required UI
"""
def TwoPlayer():
    global players
    players = 2
    if addcheck == True:
        DisplayTwo()
        ShowWFou()
    elif subcheck == True:
        DisplayTwo()
        ShowWFiv()
    app.hide()
"""
Clear All Checkboxes
Generate Cards, and Display them
Use total, input player fields and player totals
return the totals of the cards
Show the window of the gamemode
"""
def DisplayTwo():
    button15.enable()
    button18.enable()
    button16.enable()
    button21.enable()
    checkbox.clear() #Clears Textboxes
    checkbox2.clear()
    checkbox3.clear()
    checkbox4.clear()
    checkbox5.clear()
    checkbox6.clear()
    suite1 = random.randint(0,3) #Define suites randomly33
    suite2 = random.randint(0,3)
    suite3 = random.randint(0,3)
    suite4 = random.randint(0,3)
    random.shuffle(RDiamo) #Shuffle each suite
    random.shuffle(RHeart)
    random.shuffle(BClove)
    random.shuffle(BSpade)
    cardno1 = cardList[suite1][0] #choose cards
    cardno2 = cardList[suite2][1]
    cardno3 = cardList[suite3][2]
    cardno4 = cardList[suite4][3]
    card1val = cardno1 + 13*(suite1) #display card as the suite
    card2val = cardno2 + 13*(suite2)
    card3val = cardno3 + 13*(suite3)
    card4val = cardno4 + 13*(suite4)
    randCard1 = "Images/" + str(card1val) + ".png" #define what card is going to be displayed
    randCard2 = "Images/" + str(card2val) + ".png"
    randCard3 = "Images/" + str(card3val) + ".png"
    randCard4 = "Images/" + str(card4val) + ".png"
    Text(window5, text="                                                    ", color="#000000", size="10", grid=[0,5])
    Text(window4, text="                                                    ", color="#000000", size="10", grid=[0,5])
    Title = Text(window6, text="Correct!                                    ", color="#000000", font="Ariel", size="25", grid=[1, 1])
    Title = Text(window8, text="Results                                      ", color="#000000", font="Ariel", size="25", grid=[0, 0])
    picture1 = Picture(window2, image=randCard1, grid = [0,1]) #define the picture
    picture2 = Picture(window2, image=randCard2, grid = [0,2])
    picture3 = Picture(window3, image=randCard1, grid=[0, 1])
    picture4 = Picture(window3, image=randCard2, grid=[0, 2])
    picture5 = Picture(window4, image=randCard1, grid = [0,1])
    picture6 = Picture(window4, image=randCard2, grid = [0,2])
    picture7 = Picture(window4, image=randCard3, grid = [2,1])
    picture8 = Picture(window4, image=randCard4, grid = [2,2])
    picture9 = Picture(window5, image=randCard1, grid = [0,1])
    picture10 = Picture(window5, image=randCard2, grid = [0,2])
    picture11 = Picture(window5, image=randCard3, grid = [2,1])
    picture12 = Picture(window5, image=randCard4, grid = [2,2])

    global total, inputcheck, p1field, p2field, p1total, p2total, cards, score, p1score, p2score, p1dis, p2dis#Globally define variables
    if players == 1: #Determine Total for one player game
        cards -= 2
        if addcheck == True: #Addition gamemode
            total = cardList[suite1][0] + cardList[suite2][1]
            ShowWTwo()
            inputcheck = checkbox
        if subcheck == True: #Subtraction gamemode
            total = cardList[suite1][0] - cardList[suite2][1]
            ShowWThr()
            inputcheck = checkbox2
        if cards == 0 or cards <= 0:
            reset()
            score = score
            Title = Text(window6, text="Final Score (Out Of Cards)", color="#000000", font="Ariel", size="50", grid=[1, 1])
            window6.show()
            button16.disable()
        print ("Single Player Total: ", total)
    if players == 2: #Determine Total's for two player game
        cards -= 4

        if addcheck == True: #Addition Gamemode
            p1total = cardList[suite1][0] + cardList[suite2][1]
            p2total = cardList[suite3][2] + cardList[suite4][3]
            ShowWFou()
            p1field = checkbox3
            p2field = checkbox4
        if subcheck == True: #Subtraction Gamemode
            p1total = cardList[suite1][0] - cardList[suite2][1]
            p2total = cardList[suite3][2] - cardList[suite4][3]
            ShowWFiv()
            p1field = checkbox5
            p2field = checkbox6
        if cards == 0 or cards <= 0:
            reset()
            p1score = p1score
            p2score = p2score
            Title = Text(window8, text="Results (Out Of Cards)", color="#000000", font="Ariel", size="25", grid=[0, 0])
            window8.show()
            button21.disable()

        print("Player 1: ", p1total)
        print("Player 2: ", p2total)
    scoremsg = ("Your Score Is: " + str(score))
    p1dis = ("Player One Scored: " + str(p1score))
    p2dis = ("Player Two Scored: " + str(p2score))
    Dis = Text(window8, text=p1dis, color="#000000", font="Ariel", size="10", grid=[0, 1])
    Dis1 = Text(window8, text=p2dis, color="#000000", font="Ariel", size="10", grid=[0, 2])
    Score = Text(window6, text=scoremsg, color="#000000", font="Ariel", size="25", grid=[1, 3])
    Score1 = Text(window7, text=scoremsg, color="#000000", font="Ariel", size="25", grid=[1, 3])
"""
Globally use score message, score, player's scores and displays
Determine the field is a valid integar
Display window depending on if the user guessed the correct answer
Return the score message
"""
def Check():
    global scoremsg, score, p1dis, p2dis, p1score, p2score
    if players == 1:
        try:
            test = int(inputcheck.value)
        except:
            reset()
            window7.show()
        else:
            if int(inputcheck.value) == total:
                score = score + 1
                reset()
                window6.show()
            elif int(inputcheck.value) != total:
                score = score
                reset()
                window7.show()

        scoremsg = ("Your Score Is: " + str(score))
        Score = Text(window6, text=scoremsg, color="#000000", font="Ariel", size="25", grid = [1,3])
        Score1 = Text(window7, text=scoremsg, color="#000000", font="Ariel", size="25", grid = [1,3])
    if players == 2:
        try:
            test = int(p1field.value)
            test = int(p2field.value)
        except:
            Text(window5, text="One or Both of the inputs are invalid", color="#000000", size="10", grid=[0,5])
            Text(window4, text="One or Both of the inputs are invalid", color="#000000", size="10", grid=[0,5])
        else:
            if int(p1field.value) == p1total:
                p1score = p1score + 1
            if int(p2field.value) == p2total:
                p2score = p2score + 1
            if int(p1field.value) != p1total:
                p1score = p1score
            if int(p2field.value) != p2total:
                p2score = p2score
            p1dis = ("Player One Scored: " + str(p1score))
            p2dis = ("Player Two Scored: " + str(p2score))
            Dis = Text(window8, text=p1dis, color="#000000", font="Ariel", size="10", grid = [0,1])
            Dis1 = Text(window8, text=p2dis, color="#000000", font="Ariel", size="10", grid = [0,2])
            reset()
            window8.show()

#User Interfaces -----------------------------------------------------------------------------------------------

#Create seperate windows
window = Window(app, title="Score The Cards",  height= 360, width= 520, bg= "#00FFFF")
window2 = Window(app, title="Single Player Addition", height= 360, width= 520, bg= "#FFFF00", layout= "grid")
window3 = Window(app, title="Single Player Subtraction",  height= 360, width= 520, bg= "#FFFF00", layout= "grid")
window4 = Window(app, title="Two Player Addition",  height= 360, width= 520, bg= "#FFFF00", layout= "grid")
window5 = Window(app, title="Two Player Subtraction", height= 360, width= 520, bg= "#FFFF00", layout= "grid")
window6 = Window(app, title="Score The Cards", height= 360, width= 520, layout= "grid", bg="#FFA500")
window7 = Window(app, title="Score The Cards", height= 360, width= 520, layout= "grid", bg="#FFA500")
window8 = Window(app, title="Score The Cards", height= 360, width= 520, layout= "grid", bg= "#FFA500")

#Main Menu
Title = Text(app, text="Score the Cards!", color="#000000", font="Ariel", size="25", align= "top")
Formatting = Text(app, text="LLLLLLL", color="#00FFFF", font="Ariel", size="10", align= "left")
Formatting2 = Text(app, text="LLLLLLL", color="#00FFFF", font="Ariel", size="10", align= "right")
Addbut = PushButton(app, command=Addition, align= "left", text = "Addition")
Subbut = PushButton(app, command=Subtraction, align = "right", text= "Subtraction")


#Player Select
Title = Text(window, text="Score the Cards!", color="#000000", font="Ariel", size="25", align= "top")
Formatting = Text(window, text="LLLLL", color="#00FFFF", font="Ariel", size="10", align= "left")
Formatting2 = Text(window, text="LLLLL", color="#00FFFF", font="Ariel", size="10", align= "right")
button1 = PushButton(window, command=OnePlayer, align= "left", text = "One Player")
button2 = PushButton(window, command=TwoPlayer,  align = "right", text= "Two Player")
button3 = PushButton(window, command=HomePage, text= "Home", align = "bottom")

#Adding single player
Title = Text(window2, text="Single Player Addition", color="#000000", font="Ariel", size="25", grid=[0,0])
button4 = PushButton(window2, command=Check,  text="Check", grid=[0,4])
checkbox = TextBox(window2, grid=[0,3])
button5 = PushButton(window2, command=DisplayTwo, text="Redeal", grid=[1,4])
button6 = PushButton(window2, command=HomePage, text= "Home", grid= [5,5])

#taking single player
Title = Text(window3, text="Single Player Subtraction", color="#000000", font="Ariel", size="25", grid=[0,0])
button7 = PushButton(window3, command=Check,  text="Check", grid=[0,4])
checkbox2 = TextBox(window3, grid=[0,3])
button8 = PushButton(window3, command=DisplayTwo, text="Redeal", grid=[1,4])
button9 = PushButton(window3, command=HomePage, text= "Home", grid= [5,5])

#taking 2 player
Title = Text(window5, text="2 Player Subtraction", color="#000000", font="Ariel", size="25", grid=[0,0])
button10 = PushButton(window5, command=Check,  text="Check", grid=[3,2])
checkbox5 = TextBox(window5, grid=[0,3])
checkbox6 = TextBox(window5, grid=[2,3])
button11 = PushButton(window5, command=DisplayTwo, text="Redeal", grid=[3,1])
button12 = PushButton(window5, command=HomePage, text= "Home", grid= [4,5])

#Adding 2 player
Title = Text(window4, text="2 Player Addition", color="#000000", font="Ariel", size="25", grid=[0,0])
button13 = PushButton(window4, command=Check,  text="Check", grid=[3,2])
checkbox3 = TextBox(window4, grid=[0,3])
checkbox4 = TextBox(window4, grid=[2,3])
button14 = PushButton(window4, command=DisplayTwo, text="Redeal", grid=[3,1])
button15 = PushButton(window4, command=HomePage, text= "Home", grid= [4,5])



#Correct
# Title = Text(window6, text="Correct!", color="#000000", font="Ariel", size="25", grid = [1,1])
button16 = PushButton(window6, command=DisplayTwo,  text="Again?", grid = [1,2])
button17 = PushButton(window6, command=HomePage, text= "Home", grid= [3,5])


#Incorrect
# Title = Text(window7, text="Incorrect!", color="#000000", font="Ariel", size="25", grid = [1,1])
button18 = PushButton(window7, command=DisplayTwo,  text="Again?", grid = [1,2])
button19 = PushButton(window7, command=HomePage, text= "Home", grid= [3,5])

#2 Player
Title = Text(window8, text="Results", color="#000000", font="Ariel", size="25", grid = [0,0])
button20 = PushButton(window8, command=HomePage, text= "Home", grid = [3,4])
button21 = PushButton(window8, command=DisplayTwo,  text="Again?", grid = [3,5])

#colours
checkbox.bg = "White"
checkbox2.bg = "White"
checkbox3.bg = "White"
checkbox4.bg = "White"
checkbox5.bg = "White"
checkbox6.bg = "White"
Subbut.bg = "White"
Addbut.bg = "White"
button1.bg = "white"
button2.bg = "white"
button3.bg = "white"
button4.bg = "white"
button5.bg = "white"
button6.bg = "white"
button7.bg = "white"
button8.bg = "white"
button9.bg = "white"
button10.bg = "white"
button11.bg = "white"
button12.bg = "white"
button13.bg = "white"
button14.bg = "white"
button15.bg = "white"
button16.bg = "white"
button17.bg = "white"
button18.bg = "white"
button19.bg = "white"
button20.bg = "white"
button21.bg = "white"

#Functions executed on startup
reset()
app.display()
