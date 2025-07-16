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

lim = {
    "N": 0,
    "NE": 0,
    "SE": 0,
    "S": 0,
    "SW": 0,
    "NW": 0
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
    turtle.goto(0, L_hexa)
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
    turtle.penup()
    turtle.right(60)
    turtle.forward(2 * L)
    turtle.right(60)
    turtle.forward(3 * L)
    turtle.right(60)
    turtle.pendown()

def setheading(dir):
    if dir == "N":
        turtle.setheading(90)
    elif dir == "NE":
        turtle.setheading(30)
    elif dir == "SE":
        turtle.setheading(-30)
    elif dir == "S":
        turtle.setheading(-90)
    elif dir == "SW":
        turtle.setheading(-150)
    elif dir == "NW":
        turtle.setheading(150)

def update_lim(direction):
    if direction == "N":
        lim["N"] += 1
        lim["S"] -= 1
    elif direction == "NE":
        lim["NE"] += 1
        lim["SW"] -= 1
    elif direction == "SE":
        lim["SE"] += 1
        lim["NW"] -= 1
    elif direction == "S":
        lim["S"] += 1
        lim["N"] -= 1
    elif direction == "SW":
        lim["SW"] += 1
        lim["NE"] -= 1
    elif direction == "NW":
        lim["NW"] += 1
        lim["SE"] -= 1

def check_lim():
    for key in lim:
        if lim[key] >= 3:
            return False
    return True

def random_move():
    cap = ["N", "NE", "SE", "S", "SW", "NW"]
    while True:
        tmp = random.choice(cap)
        setheading(tmp)
        turtle.forward(L)
        update_lim(tmp)
        print(lim)
        if not check_lim():
            return

def close_window():
    turtle.bye()


if __name__ == "__main__":
    setup()
    
    turtle.right(30)
    
    draw_hexa()
    grid_hexa()

    turtle.pencolor("blue")

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    # random_move()

    turtle.listen()
    turtle.onkey(close_window, "q")
    turtle.done()