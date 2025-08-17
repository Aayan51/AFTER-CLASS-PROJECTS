import turtle


t = turtle.Turtle()
s = turtle.Screen()
colours = ["white", "blue", "red", "green", "yellow", "orange", "purple"]
s.bgcolor("black")
t.speed('slow')
t.hideturtle()


def draw_triangle():
    t.pencolor("blue")
    for _ in range(3):
        t.forward(100)
        t.left(120)



def draw_hexagon():
    t.pencolor("green")
    for _ in range(6):
        t.forward(100)
        t.left(60)


def draw_rectangle():
    t.pencolor("red")
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(100)
        t.left(90)


draw_triangle()
t.penup()
t.goto(-200, 0)  
t.pendown()
draw_hexagon()
t.penup()
t.goto(200, 0)  
t.pendown()
draw_rectangle()


turtle.done()