import turtle


def draw_smiley():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(5)

    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.begin_fill()
    t.color("yellow")
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-35, -50)
    t.pendown()
    t.begin_fill()
    t.color("black")
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(35, -50)
    t.pendown()
    t.begin_fill()
    t.color("black")
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(-50, -80)
    t.setheading(-60)
    t.pendown()
    t.width(5)
    t.circle(50, 120)

    t.penup()
    t.goto(-65, -70)
    t.pendown()
    t.begin_fill()
    t.color("pink")
    t.circle(8)
    t.end_fill()

    t.penup()
    t.goto(65, -70)
    t.pendown()
    t.begin_fill()
    t.color("pink")
    t.circle(8)
    t.end_fill()

    t.hideturtle()
    screen.mainloop()


draw_smiley()
