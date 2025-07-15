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
    turtle.goto(L_hexa/2, L_hexa+100 / 2)
    turtle.pendown()

def draw_hexa():
    for _ in range(6):
        turtle.forward(L_hexa)
        turtle.right(60)
    return

def grid_hexa():
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