import turtle
turtle.showturtle()
turtle.speed(50)
turtle.bgcolor('blue')
def southern_cross():
    def star_seven():
        turtle.pencolor('white')
        turtle.fillcolor('white')
        turtle.right(180)
        turtle.begin_fill()
        for x in range(7):
            turtle.forward(30)
            turtle.right(180-180/7)
        turtle.end_fill()

    def star_five():
        turtle.pencolor('white')
        turtle.fillcolor('white')
        turtle.right(180)
        turtle.begin_fill()
        for x in range(5):
            turtle.forward(15)
            turtle.right(180-180/5)
        turtle.end_fill()

    turtle.penup()
    turtle.goto (100,-30)
    turtle.pendown()
    star_seven()

    turtle.penup()
    turtle.goto(120, 60)
    turtle.pendown()
    star_seven()

    turtle.penup()
    turtle.goto(110, 30)
    turtle.pendown()
    star_five()

    turtle.penup()
    turtle.goto(25, 45)
    turtle.pendown()
    star_seven()

    turtle.penup()
    turtle.goto (100,100)
    turtle.pendown()
    star_seven()
def Union_jack():
    turtle.penup()
    turtle.goto(-90,80)
    turtle.pendown()

    turtle.pensize(20)
    turtle.pencolor('white')
    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)

    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)

    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)



#Diagonals
    turtle.penup()
    turtle.goto(-90,80)
    turtle.pendown()
    turtle.right(65)
    turtle.pensize(20)
    turtle.pencolor('white')

    turtle.right(90)
    turtle.forward(80)
    turtle.right(180)
    turtle.forward(160)
    turtle.right(180)
    turtle.forward(80)
    turtle.left(65)

    turtle.goto(-90,80)
    turtle.right(295)
    turtle.forward(80)
    turtle.right(180)
    turtle.forward(160)
    turtle.right(180)
    turtle.forward(80)

#Red
    turtle.pensize(12)
    turtle.pencolor('red')
    turtle.right(65)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)

    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)

    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)

    turtle.penup()
    turtle.goto(-90,80)
    turtle.pendown()
#Red Diagonals

    turtle.penup()
    turtle.goto(-90,80)
    turtle.pendown()
    turtle.right(65)
    turtle.pensize(10)
    turtle.pencolor('red')

    turtle.right(90)
    turtle.forward(80)
    turtle.right(180)
    turtle.forward(160)
    turtle.right(180)
    turtle.forward(80)
    turtle.left(65)

    turtle.goto(-90,80)
    turtle.right(295)
    turtle.forward(80)
    turtle.right(180)
    turtle.forward(160)
    turtle.right(180)
    turtle.forward(80)

#White Box
turtle.pensize(20)
turtle.pencolor('white')
turtle.penup()
turtle.goto(-200,150)
turtle.pendown()
turtle.forward(400)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.pensize(1)
southern_cross()
Union_jack()
turtle.done()

