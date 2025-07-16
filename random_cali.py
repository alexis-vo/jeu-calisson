import turtle
import random
import math

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
    # turtle.hideturtle()
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

def on_lim(pos, coord_lim):
    for arrete in coord_lim:
        if pos in arrete:
            print(True)
            return True
    print(False)
    return False
    
def random_move():
    cap = ["N", "NE", "SE", "S", "SW", "NW"]
    while True:
        tmp = random.choice(cap)
        setheading(tmp)
        turtle.forward(L)
        pos = (math.floor(turtle.xcor() * 100) / 100, math.floor(turtle.ycor() * 100) / 100)
        print(pos, tmp)
        if on_lim(pos, coord_lim):
            return

def random_color():
    return random.choice(["#F7C5CC", "#A9D6E5", "#C9E4C5"])
    

def safe_forward(distance):
    pos = (math.floor(turtle.xcor() * 100) / 100, math.floor(turtle.ycor() * 100) / 100)
    if on_lim(pos, coord_lim):
        return False
    turtle.forward(distance)

def random_losange():
    cap = ["N", "NE", "SE", "S", "SW", "NW"]
    for _ in range(7):
        tmp = random.choice(cap)
        setheading(tmp)
        print(tmp)
        draw_losange(random_color())

def get_coord_lim():
    turtle.penup()
    coord_lim = []
    turtle.goto(0, L_hexa)
    for _ in range(6):
        arrete = []
        for _ in range(3):
            arrete.append((math.floor(turtle.xcor() * 100) / 100, math.floor(turtle.ycor() * 100) / 100))
            turtle.forward(L)
        turtle.right(60)
        coord_lim.append(arrete)
    turtle.pendown()
    return coord_lim

def draw_losange(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        # if not safe_forward(L): break
        turtle.forward(L)
        turtle.right(60)
        # if not safe_forward(L): break
        turtle.forward(L)
        turtle.right(120)
    turtle.end_fill()

def close_window():
    turtle.bye()

if __name__ == "__main__":
    setup()
    
    turtle.right(30)
    
    draw_hexa()
    grid_hexa()

    turtle.pencolor("black")

    coord_lim = get_coord_lim()

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    # print(coord_lim)
    
    # random_move()
    random_losange()

    turtle.listen()
    turtle.onkey(close_window, "q")
    turtle.done()