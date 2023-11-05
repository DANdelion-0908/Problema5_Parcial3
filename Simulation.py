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
    
    #Variable to store the cable material
    cableMaterial = "Cobre" 

    #To use the method drawCilinder(radius, length), the radius passed to the method has to be in mm and the length in meters
    #The conversions are made inside the method so the scale is better for the simulation 
    #(Here I use 4mm for radius and 4 meters of length)
    

    if(cableMaterial == "Oro"):
        drawCilinder(4, 3, "yellow")
    
    elif(cableMaterial == "Plata"):
        drawCilinder(4, 3, "white")

    elif(cableMaterial == "Cobre"):
        drawCilinder(4, 3, "orange")
        
    elif(cableMaterial == "Aluminio"):
        drawCilinder(4, 3, "grey")
        
    elif(cableMaterial == "Grafito"):
        drawCilinder(4, 3, "black")

    turtle.done()

Simulation()