import random
import turtle
import Drawings

def SimulateRandom(turt: turtle, color, screen):

    HEIGHT = 10
    WIDTH = 10
    Drawings.drawCilinder(HEIGHT, WIDTH, color, screen, 0)

    turt.shape('circle')
    turt.penup()
    turt.speed(1)
    turt.goto(0, 0)
    turt.back(1220)
    
    y_limit = HEIGHT * 10 / 2

    while True:
        x = random.uniform(-1220, -500)
        y = random.uniform(-y_limit, y_limit)
        turt.goto(x, y)