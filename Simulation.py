import turtle
import math
from Drawings import *

def Simulation():
    print("Hello")

    turtle.clearscreen()
    gorge = turtle.Turtle()

    turtle.tracer(False)
    turtle.update()

    verticalScreenSize = 800
    horizontalScreenSize = 2000
    turtle.setup(800, verticalScreenSize - 150)
    turtle.screensize(horizontalScreenSize, verticalScreenSize)

    draw_grid(10, horizontalScreenSize, turtle= gorge)

    drawAxis(verticalScreenSize / 3)

    turtle.tracer(True)
    turtle.update()

    #To use this method, the radius passed to the method has to be in mm and the length in meters
    #The conversions are made inside the method so the scale is better for the simulation 
    #(Here i use 4mm for radius and 2 meters of length)
    drawCilinder(4, 2)

Simulation()