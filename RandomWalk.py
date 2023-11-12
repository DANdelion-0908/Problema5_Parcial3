import random
import turtle
import Drawings

def SimulateRandom(color, screen):
    """
    The function SimulateRandom uses the turtle module to draw a cylinder of a given color on the screen
    and then moves a turtle randomly within a specified range.
    
    :param color: The "color" parameter is the color of the cylinder that will be drawn on the screen.
    It can be any valid color name or color code
    :param screen: The "screen" parameter is the turtle screen object where the drawing will be
    displayed. It is used to create a turtle object and clear the screen before drawing
    """

    screen.clearscreen()
    turt = turtle.RawTurtle(screen)

    HEIGHT = 10
    WIDTH = 10
    Drawings.drawCilinder(HEIGHT, WIDTH, color, screen, 0)

    turt.shape('circle')
    turt.penup()
    turt.speed(0)
    turt.goto(0, 0)
    turt.back(1220)
    turt.speed(1)

    y_limit = HEIGHT * 10 / 2

    keyLoop = 0

    while keyLoop <= 30:

        x = random.uniform(-1220, -500)
        y = random.uniform(-y_limit, y_limit)
        turt.goto(x, y)

        keyLoop += 1