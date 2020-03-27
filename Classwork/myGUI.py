from guizero import App, Text, Picture, PushButton, MenuBar

app = App()
text = Text(app, align="bottom", text="It's the Kungflu", color="#A3125C", font="Calibri", size="56")
text1 = Text(app, align="top", text="Keep Schools Open", color="#ABC123", font="Ariel", size="39")


def Blue():
    button.bg = "blue"


def Green():
    button.bg = "green"


def Red():
    button.bg = "red"


def Yellow():
    button.bg = "yellow"

def Black():
    button.bg = "black"

def White():
    button.bg = "white"


menubar = MenuBar(app,
                  toplevel=["Basic", "Spicey", "Shades"],
                  options=[
                      [["Blue", Blue], ["Green", Green]],
                      [["Red", Red], ["Yellow", Yellow]],
                      [["White", White], ["Black", Black]]
                  ])

button = PushButton(app, image="dt.png", command=Blue)

button.bg = "red"

app.display()
