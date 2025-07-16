import turtle
import random

nb_cali_sur_longueur = 3
L_hexa = 100 * nb_cali_sur_longueur
L = L_hexa / nb_cali_sur_longueur

rules = {
    0: "bord",
    1: "coin aigu",
    2: "pli",
    3: "sommet",
    4: "arrêtes sur une ligne"
}

def setup():
    turtle.clearscreen()
    turtle.title("Pavage de calissons aléatoire")
    turtle.bgcolor("white")
    turtle.pencolor("black")
    turtle.pensize(2)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, L_hexa+100 / 2)
    turtle.pendown()

def draw_hexa():
    for _ in range(6):
        turtle.forward(L_hexa)
        turtle.right(60)
    return

def lines_grid_hexa():
    turtle.pencolor("lightgray")

    turtle.penup()
    turtle.forward(L)
    turtle.right(120)
    turtle.pendown()

    turtle.forward(400)
    turtle.left(60)
    turtle.penup()
    turtle.forward(L)
    turtle.left(120)
    turtle.pendown()

    turtle.forward(500)
    turtle.right(60)
    turtle.penup()
    turtle.forward(L)
    turtle.right(120)
    turtle.pendown()

    turtle.forward(600)

    turtle.left(120)
    turtle.penup()
    turtle.forward(L)
    turtle.left(60)
    turtle.pendown()

    turtle.forward(500)
    turtle.right(120)
    turtle.penup()
    turtle.forward(L)
    turtle.right(60)
    turtle.pendown()
    
    turtle.forward(400)

def grid_hexa():
    lines_grid_hexa()
    turtle.penup()
    turtle.right(60)
    turtle.forward(2 * L)
    turtle.right(60)
    turtle.forward(3 * L)
    turtle.right(60)
    turtle.pendown()
    lines_grid_hexa()
    turtle.penup()
    turtle.right(60)
    turtle.backward(L)
    turtle.left(60)
    turtle.backward(3 * L)
    turtle.pendown()
    lines_grid_hexa()

def close_window():
    turtle.bye()


if __name__ == "__main__":
    setup()
    turtle.right(30)
    draw_hexa()
    grid_hexa()

    turtle.listen()
    turtle.onkey(close_window, "q")
    turtle.done()