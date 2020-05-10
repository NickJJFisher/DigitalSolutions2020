from guizero import App, Window, TextBox, Text, PushButton

app = App(title= "Login Screen", layout= "grid", bg="#add8e6", height=200) #initialise app
window = Window(app, title= "GUI") #initialise second window
window.hide() #hide second window

def check_cred():
    text = Text(app, grid=[0,2])
    if username_txt.value == user_un and password_txt.value == user_pw:
        window.show()
        app.hide()
    else:
        text = Text(app, text="Incorrect Credentials", grid=[0,3])

#define variables
user_un = 'Nicholas'
user_pw = "ABClike123"

#Set Obects on first screen
username_txt = TextBox(app, grid=[0,0])
password_txt = TextBox(app, grid=[0,1])
PushButton(app, command=check_cred, grid = [0,2], text= "Login")


#Set Objects on Second Screen
PushButton(window, grid = [1,1], text= "Good Job You remember'd your password.")
app.display()