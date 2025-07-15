import turtle
import time

# Taille d'une arête
L = 30

# Configuration turtle
turtle.clearscreen()
turtle.title("Pavage")
turtle.bgcolor("white")
turtle.pencolor("black")
turtle.home()
turtle.pensize(2)
turtle.speed(0)
turtle.hideturtle()

time.sleep(5)

colors = {
    "gray": "#CCCCCC",
    "dark": "#4B4949",
    "light": "#FFFFFF"
}


def draw_losange():
    turtle.begin_fill()
    turtle.forward(L)
    turtle.right(60)
    turtle.forward(L)
    turtle.right(120)
    turtle.forward(L)
    turtle.right(60)
    turtle.forward(L)
    turtle.right(120)
    turtle.end_fill()


turtle.fillcolor(colors["gray"])

turtle.left(30)
draw_losange()
turtle.left(120)
turtle.penup()
turtle.forward(2*L)
turtle.right(120)
turtle.pendown()

for _ in range(2):
    draw_losange()
    turtle.forward(L)

for _ in range(3):
    draw_losange()
    turtle.right(60)
    turtle.forward(L)
    turtle.left(60)

turtle.penup()
turtle.backward(4*L)
turtle.pendown()

for _ in range(2):
    draw_losange()
    turtle.right(60)
    turtle.forward(L)
    turtle.left(60)

turtle.left(60)
turtle.penup()
turtle.forward(L)
turtle.right(60)
turtle.pendown()
draw_losange()


turtle.fillcolor(colors["dark"])

turtle.left(60)
draw_losange()

turtle.penup()
turtle.backward(2*L)
turtle.pendown()

for _ in range(2):
    draw_losange()
    turtle.right(60)
    turtle.forward(L)
    turtle.left(60)

for _ in range(3):
    draw_losange()
    turtle.forward(L)


turtle.right(60)
turtle.penup()
turtle.backward(4*L)
turtle.pendown()

turtle.left(60)
draw_losange()
turtle.forward(L)

for _ in range(2):
    draw_losange()
    turtle.right(60)
    turtle.forward(L)
    turtle.left(60)

turtle.fillcolor(colors["light"])

turtle.forward(L)
turtle.right(120)

for _ in range(2):
    draw_losange()
    turtle.forward(L)

turtle.left(120)
turtle.backward(2*L)
turtle.left(60)
draw_losange()

turtle.penup()
turtle.backward(L)
turtle.left(60)
for _ in range(3):
    turtle.forward(L)

turtle.right(60)

turtle.pendown()
for _ in range(2):
    draw_losange()
    turtle.forward(L)

for _ in range(3):
    draw_losange()
    turtle.right(60)
    turtle.forward(L)
    turtle.left(60)

def close_window():
    turtle.bye()

turtle.listen()
turtle.onkey(close_window, "q")

turtle.done()