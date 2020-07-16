#Import Modules
import random
from guizero import App, Picture, PushButton, Window, TextBox, Text, MenuBar
Background = "#00FFFF"
#Mainpage UI
app = App(height= 360, width= 520, title= "Score the cards!",bg= Background)

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
    playerselect_wnd.hide()
    sinadd_wnd.hide()
    sinsub_wnd.hide()
    duoadd_wnd.hide()
    duosub_wnd.hide()
    correct_wnd.hide()
    incorrect_wnd.hide()
    results_wnd.hide()
"""
Hide all windows
Display Window 2
"""
def ShowWTwo():
    reset()
    sinadd_wnd.show()
"""
Hide all windows
Display Window 3
"""
def ShowWThr():
    reset()
    sinsub_wnd.show()
"""
Hide all windows
Display Window 4
"""
def ShowWFou():
    reset()
    duoadd_wnd.show()
"""
Hide all windows
Display Window 5
"""
def ShowWFiv():
    reset()
    duosub_wnd.show()
"""
Globally use the variables defined at the beginning
Reset the variables back to startup values
"""
def HomePage():
    global score, scoremsg, addcheck, subcheck, inputcheck, cardList, RHeart, RDiamo, BSpade, BClove, players, p1score, p1total, p2score, p2total, p1field, cards, p2field
    cards = 52
    score = 0
    players = 1
    scoremsg = str("pholder")
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
    playerselect_wnd.show()
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
    playerselect_wnd.show()
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
        sinsub_wnd.show()
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
    checkbox.when_mouse_enters = highlight #Change colour of textboxes for visiblity when hovered over
    checkbox.when_mouse_leaves = lowlight
    checkbox2.when_mouse_enters = highlight
    checkbox2.when_mouse_leaves = lowlight
    checkbox3.when_mouse_enters = highlight
    checkbox3.when_mouse_leaves = lowlight
    checkbox4.when_mouse_enters = highlight
    checkbox4.when_mouse_leaves = lowlight
    checkbox5.when_mouse_enters = highlight
    checkbox5.when_mouse_leaves = lowlight
    checkbox6.when_mouse_enters = highlight
    checkbox6.when_mouse_leaves = lowlight

    button15.enable()
    button21.enable()
    button16.enable()
    button18.enable()
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
    Text(duosub_wnd, text="                                                    ", color="#000000", size="10", grid=[0,5]) #Clear the current text boxes to reset
    Text(duoadd_wnd, text="                                                    ", color="#000000", size="10", grid=[0,5])
    Title = Text(correct_wnd, text="Correct!                                  ", color="#000000", font="Ariel", size="25", grid=[1, 1])
    Title = Text(results_wnd, text="Results                                   ", color="#000000", font="Ariel", size="25", grid=[0, 0])
    picture1 = Picture(sinadd_wnd, image=randCard1, grid = [0,1]) #define the picture's on every window
    picture2 = Picture(sinadd_wnd, image=randCard2, grid = [0,2])
    picture3 = Picture(sinsub_wnd, image=randCard1, grid=[0, 1])
    picture4 = Picture(sinsub_wnd, image=randCard2, grid=[0, 2])
    picture5 = Picture(duoadd_wnd, image=randCard1, grid = [0,1])
    picture6 = Picture(duoadd_wnd, image=randCard2, grid = [0,2])
    picture7 = Picture(duoadd_wnd, image=randCard3, grid = [2,1])
    picture8 = Picture(duoadd_wnd, image=randCard4, grid = [2,2])
    picture9 = Picture(duosub_wnd, image=randCard1, grid = [0,1])
    picture10 = Picture(duosub_wnd, image=randCard2, grid = [0,2])
    picture11 = Picture(duosub_wnd, image=randCard3, grid = [2,1])
    picture12 = Picture(duosub_wnd, image=randCard4, grid = [2,2])

    global total, inputcheck, p1field, p2field, p1total, p2total, cards, score, p1score, p2score, p1dis, p2dis#Globally define variables
    if players == 1: #Determine Total for one player game
        cards -= 2
        if addcheck == True: #Addition gamemode
            total = cardList[suite1][0] + cardList[suite2][1] #Calculate total for this section
            ShowWTwo()  #show window 2
            inputcheck = checkbox
        if subcheck == True: #Subtraction gamemode
            total = cardList[suite1][0] - cardList[suite2][1]#Calculate total for this section
            ShowWThr() #show window 3
            inputcheck = checkbox2
        if cards == 0 or cards <= 0:
            reset()
            score = score
            Title = Text(correct_wnd, text="Final Score (Out Of Cards)!!", color="#000000", font="Ariel", size="25", grid=[1, 1])
            correct_wnd.show()
            button16.disable()
        print ("Single Player Total: ", total)
    if players == 2: #Determine Total's for two player game
        cards -= 4

        if addcheck == True: #Addition Gamemode
            p1total = cardList[suite1][0] + cardList[suite2][1]
            p2total = cardList[suite3][2] + cardList[suite4][3]#Calculate total for this section
            ShowWFou() #Show window 4
            p1field = checkbox3
            p2field = checkbox4
        if subcheck == True: #Subtraction Gamemode
            p1total = cardList[suite1][0] - cardList[suite2][1]#Calculate total for this section
            p2total = cardList[suite3][2] - cardList[suite4][3]
            ShowWFiv() #show window5
            p1field = checkbox5
            p2field = checkbox6
        if cards == 0 or cards <= 0:
            reset()
            p1score = p1score
            p2score = p2score
            Title2 = Text(results_wnd, text="Results (Out Of Cards)!!", color="#000000", font="Ariel", size="25", grid=[0, 0])
            results_wnd.show()
            button21.disable()

        print("Player 1: ", p1total)
        print("Player 2: ", p2total)
    scoremsg = ("Your Score Is: " + str(score))
    p1dis = ("Player One Scored: " + str(p1score))
    p2dis = ("Player Two Scored: " + str(p2score))
    Dis = Text(results_wnd, text=p1dis, color="#000000", font="Ariel", size="10", grid=[0, 1])
    Dis1 = Text(results_wnd, text=p2dis, color="#000000", font="Ariel", size="10", grid=[0, 2])
    Score = Text(correct_wnd, text=scoremsg, color="#000000", font="Ariel", size="25", grid=[1, 3])
    Score1 = Text(incorrect_wnd, text=scoremsg, color="#000000", font="Ariel", size="25", grid=[1, 3])

"""
Globally use score message, score, player's scores and displays
Determine the field is a valid integar
Display window depending on if the user guessed the correct answer
Return the score message
"""

def Check():
    global scoremsg, score, p1dis, p2dis, p1score, p2score, Error1, Error2 #Global variables
    if players == 1: #One Player decision
        try: # Test variable is a number
            test = int(inputcheck.value)
        except:
            reset()
            incorrect_wnd.show()
        else:
            if int(inputcheck.value) == total: #Correct
                score = score + 1 #Increment score
                reset()
                correct_wnd.show()
            elif int(inputcheck.value) != total: #Incorrect
                score = score #Score stays the same
                reset()
                incorrect_wnd.show()

        scoremsg = ("Your Score Is: " + str(score)) #Show score
        Score = Text(correct_wnd, text=scoremsg, color="#000000", font="Ariel", size="25", grid = [1,3])
        Score1 = Text(incorrect_wnd, text=scoremsg, color="#000000", font="Ariel", size="25", grid = [1,3])
    if players == 2: #Two Player
        try: #Test both are integars
            test = int(p1field.value)
            test = int(p2field.value)
        except:
            Error1 = Text(duosub_wnd, text="One or Both of the inputs are invalid", color="#000000", size="10", grid=[0,5])
            Error2 = Text(duoadd_wnd, text="One or Both of the inputs are invalid", color="#000000", size="10", grid=[0,5])
        else:
            if int(p1field.value) == p1total: #correct, Increment player 1 by 1
                p1score = p1score + 1
            if int(p2field.value) == p2total: #correct, increment player 2 by 2
                p2score = p2score + 1
            if int(p1field.value) != p1total: #incorrect, player 1 stay same
                p1score = p1score
            if int(p2field.value) != p2total: #incorrect, player 2 stays same.
                p2score = p2score
            p1dis = ("Player One Scored: " + str(p1score)) #Show score messages
            p2dis = ("Player Two Scored: " + str(p2score))
            Dis = Text(results_wnd, text=p1dis, color="#000000", font="Ariel", size="10", grid = [0,1])
            Dis1 = Text(results_wnd, text=p2dis, color="#000000", font="Ariel", size="10", grid = [0,2])
            reset()
            results_wnd.show()
"""
Function Highlight
Turns all input boxes to a lightblue colour
"""
def highlight():
    checkbox.bg = "lightblue"
    checkbox2.bg = "lightblue"
    checkbox3.bg = "lightblue"
    checkbox4.bg = "lightblue"
    checkbox5.bg = "lightblue"
    checkbox6.bg = "lightblue"
"""
Function Highlight
Turns all input boxes to a white colour
"""
def lowlight():
    checkbox.bg = "White"
    checkbox2.bg = "White"
    checkbox3.bg = "White"
    checkbox4.bg = "White"
    checkbox5.bg = "White"
    checkbox6.bg = "White"

"""
Use globally, all windows
Change the background of each window to variable "Background"
Calls on "Colours" Function
"""

def ChangeColour():
    global playerselect_wnd, app, sinadd_wnd, sinsub_wnd, duoadd_wnd, duosub_wnd, correct_wnd, incorrect_wnd, results_wnd
    app.bg = Background
    playerselect_wnd.bg = Background
    sinadd_wnd.bg = Background
    sinsub_wnd.bg = Background
    duoadd_wnd.bg = Background
    duosub_wnd.bg = Background
    correct_wnd.bg = Background
    incorrect_wnd.bg = Background
    results_wnd.bg = Background
    colours()
"""
Exits the Program
"""
def Close():
    exit()
"""
Turns all windows to "Full Screen" Mode
"""
def Fullscreen():
    app.full_screen = True
    playerselect_wnd.full_screen = True
    sinadd_wnd.full_screen = True
    sinsub_wnd.full_screen = True
    duoadd_wnd.full_screen = True
    duosub_wnd.full_screen = True
    correct_wnd.full_screen = True
    incorrect_wnd.full_screen = True
    results_wnd.full_screen = True
"""
Turns all windows to "Minimise" Mode
"""
def Minimise():
    app.full_screen = False
    playerselect_wnd.full_screen = False
    sinadd_wnd.full_screen = False
    sinsub_wnd.full_screen = False
    duoadd_wnd.full_screen = False
    duosub_wnd.full_screen = False
    correct_wnd.full_screen = False
    incorrect_wnd.full_screen = False
    results_wnd.full_screen = False

"""
All following "Def [colour]" functions do same: 
Functions
Globally use "Background"
define "Background" to a colour
Run ChangeColour
"""
def Blue():
    global Background
    Background = "#00FFFF"
    ChangeColour()

def Green():
    global Background
    Background = "green"
    ChangeColour()
def Red():
    global Background
    Background = "#FF6961"
    ChangeColour()
def Yellow():
    global Background
    Background = "yellow"
    ChangeColour()
def Black():
    global Background
    Background = "#808080"
    ChangeColour()
def White():
    global Background
    Background = "#D3D3D3"
    ChangeColour()


#User Interfaces -----------------------------------------------------------------------------------------------
#All following follow some layout:
#VAR NAME = object type(window location, name, another other info...)
#Create seperate windows
playerselect_wnd = Window(app, title="Score The Cards",  height= 360, width= 520, bg= "#00FFFF")
playerselect_wnd.hide()
sinadd_wnd = Window(app, title="Single Player Addition", height= 360, width= 520, bg= "#FFFF00", layout= "grid")
sinadd_wnd.hide()
sinsub_wnd = Window(app, title="Single Player Subtraction",  height= 360, width= 520, bg= "#FFFF00", layout= "grid")
sinsub_wnd.hide()
duoadd_wnd = Window(app, title="Two Player Addition",  height= 360, width= 520, bg= "#FFFF00", layout= "grid")
duoadd_wnd.hide()
duosub_wnd = Window(app, title="Two Player Subtraction", height= 360, width= 520, bg= "#FFFF00", layout= "grid")
duosub_wnd.hide()
correct_wnd = Window(app, title="Score The Cards", height= 360, width= 520, layout= "grid", bg="#FFA500")
correct_wnd.hide()
incorrect_wnd = Window(app, title="Score The Cards", height= 360, width= 520, layout= "grid", bg="#FFA500")
incorrect_wnd.hide()
results_wnd = Window(app, title="Score The Cards", height= 360, width= 520, layout= "grid", bg= "#FFA500")
results_wnd.hide()

#Main Menu
Title = Text(app, text="Score the Cards!", color="#000000", font="Ariel", size="25", align= "top")
Addbut = PushButton(app, command=Addition, align= "left", text = "Addition")
Subbut = PushButton(app, command=Subtraction, align = "right", text= "Subtraction")


#Player Select
Title = Text(playerselect_wnd, text="Score the Cards!", color="#000000", font="Ariel", size="25", align= "top")
button1 = PushButton(playerselect_wnd, command=OnePlayer, align= "left", text = "One Player")
button2 = PushButton(playerselect_wnd, command=TwoPlayer,  align = "right", text= "Two Player")
button3 = PushButton(playerselect_wnd, command=HomePage, text= "Home", align = "bottom")

#Adding single player
Title = Text(sinadd_wnd, 9+, color="#000000", font="Ariel", size="25", grid=[0,0])
button4 = PushButton(sinadd_wnd, command=Check,  text="Check", grid=[0,4])
checkbox = TextBox(sinadd_wnd, grid=[0,3])
button5 = PushButton(sinadd_wnd, command=DisplayTwo, text="Redeal", grid=[1,4])
button6 = PushButton(sinadd_wnd, command=HomePage, text= "Home", grid= [5,5])

#taking single player
Title = Text(sinsub_wnd, text="Single Player Subtraction", color="#000000", font="Ariel", size="25", grid=[0,0])
button7 = PushButton(sinsub_wnd, command=Check,  text="Check", grid=[0,4])
checkbox2 = TextBox(sinsub_wnd, grid=[0,3])
button8 = PushButton(sinsub_wnd, command=DisplayTwo, text="Redeal", grid=[1,4])
button9 = PushButton(sinsub_wnd, command=HomePage, text= "Home", grid= [5,5])

#taking 2 player
Title = Text(duosub_wnd, text="2 Player Subtraction", color="#000000", font="Ariel", size="25", grid=[0,0])
button10 = PushButton(duosub_wnd, command=Check,  text="Check", grid=[3,2])
checkbox5 = TextBox(duosub_wnd, grid=[0,3])
checkbox6 = TextBox(duosub_wnd, grid=[2,3])
button11 = PushButton(duosub_wnd, command=DisplayTwo, text="Redeal", grid=[3,1])
button12 = PushButton(duosub_wnd, command=HomePage, text= "Home", grid= [4,5])
Error1 = Text(duosub_wnd, text="One or Both of the inputs are invalid", color="#000000", size="10", grid=[0, 5])

#Adding 2 player
Title = Text(duoadd_wnd, text="2 Player Addition", color="#000000", font="Ariel", size="25", grid=[0,0])
button13 = PushButton(duoadd_wnd, command=Check,  text="Check", grid=[3,2])
checkbox3 = TextBox(duoadd_wnd, grid=[0,3])
checkbox4 = TextBox(duoadd_wnd, grid=[2,3])
button14 = PushButton(duoadd_wnd, command=DisplayTwo, text="Redeal", grid=[3,1])
button15 = PushButton(duoadd_wnd, command=HomePage, text= "Home", grid= [4,5])
Error2 = Text(duoadd_wnd, text="One or Both of the inputs are invalid", color="#000000", size="10", grid=[0, 5])


#Correct
Title1 = Text(correct_wnd, text="Correct!", color="#000000", font="Ariel", size="25", grid = [1,1])
button16 = PushButton(correct_wnd, command=DisplayTwo,  text="Again?", grid = [1,2])
button17 = PushButton(correct_wnd, command=HomePage, text= "Home", grid= [3,5])


#Incorrect
Title = Text(incorrect_wnd, text="Incorrect!", color="#000000", font="Ariel", size="25", grid = [1,1])
button18 = PushButton(incorrect_wnd, command=DisplayTwo,  text="Again?", grid = [1,2])
button19 = PushButton(incorrect_wnd, command=HomePage, text= "Home", grid= [3,5])

#2 Player
Title2 = Text(results_wnd, text="Results", color="#000000", font="Ariel", size="25", grid = [0,0])
button20 = PushButton(results_wnd, command=HomePage, text= "Home", grid = [3,4])
button21 = PushButton(results_wnd, command=DisplayTwo,  text="Again?", grid = [3,5])

#MenuBar
menubar = MenuBar(app,
                  toplevel=["File", "Cool", "Warm", "Shades"], #The Seen Menu
                  options=[
                      [["Quit", Close], ["FullScreen", Fullscreen], ["Minimise", Minimise]], #Buttons in each submenu
                      [["Blue", Blue], ["Green", Green]],
                      [["Red", Red], ["Yellow", Yellow]],
                      [["Light Grey", White], ["Dark Grey", Black]]
                  ])


#colours
#Set all objects to white BG
def colours():
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
colours()
app.display()
