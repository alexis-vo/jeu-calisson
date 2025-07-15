import turtle

L = 30
colors = {
    "gray": "#CCCCCC",
    "dark": "#4B4949",
    "light": "#FFFFFF"
}

def setup():
    turtle.clearscreen()
    turtle.title("Pavage de calissons")
    turtle.bgcolor("white")
    turtle.pencolor("black")
    turtle.pensize(2)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def draw_losange():
    turtle.begin_fill()
    for angle in [60, 120, 60, 120]:
        turtle.forward(L)
        turtle.right(angle)
    turtle.end_fill()

def draw_line(count, move_func=None):
    for _ in range(count):
        draw_losange()
        if move_func:
            move_func()

def move_forward():
    turtle.forward(L)

def move_diagonal_right():
    turtle.right(60)
    turtle.forward(L)
    turtle.left(60)

def move_diagonal_left():
    turtle.left(60)
    turtle.forward(L)
    turtle.right(60)


setup()

turtle.fillcolor(colors["gray"])

turtle.left(30)
draw_losange()

turtle.left(120)
turtle.penup()
turtle.forward(2 * L)
turtle.right(120)
turtle.pendown()

draw_line(2, move_forward)
draw_line(3, move_diagonal_right)

turtle.penup()
turtle.backward(4 * L)
turtle.pendown()

draw_line(2, move_diagonal_right)

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
turtle.backward(2 * L)
turtle.pendown()

draw_line(2, move_diagonal_right)
draw_line(3, move_forward)

turtle.right(60)
turtle.penup()
turtle.backward(4 * L)
turtle.pendown()

turtle.left(60)
draw_losange()
turtle.forward(L)

draw_line(2, move_diagonal_right)

turtle.fillcolor(colors["light"])

turtle.forward(L)
turtle.right(120)
draw_line(2, move_forward)

turtle.left(120)
turtle.backward(2 * L)
turtle.left(60)
draw_losange()

turtle.penup()
turtle.backward(L)
turtle.left(60)
turtle.forward(3 * L)
turtle.right(60)
turtle.pendown()

draw_line(2, move_forward)
draw_line(3, move_diagonal_right)


def close_window():
    turtle.bye()

turtle.listen()
turtle.onkey(close_window, "q")
turtle.done()