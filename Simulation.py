import turtle
from Drawings import *
import tkinter as tk

def Simulation(gorge, screen, cableMaterial, radius, length):
    screen.clearscreen()

    screen.tracer(False)
    screen.update()

    verticalScreenSize = 500
    horizontalScreenSize = 3000
    screen.screensize(horizontalScreenSize, verticalScreenSize)
    draw_grid(10, horizontalScreenSize, turtle=gorge)

    drawAxis(verticalScreenSize / 3, screen)

    screen.tracer(True)
    screen.update()

    #To use the method drawCilinder(radius, length), the radius passed to the method has to be in mm and the length in meters
    #The conversions are made inside the method so the scale is better for the simulation 
    #(Here I use 4mm for radius and 4 meters of length)

    if(cableMaterial == "Oro"):
        drawCilinder(radius, length, "yellow", screen)

    elif(cableMaterial == "Plata"):
        drawCilinder(4, 3, "white", screen)

    elif(cableMaterial == "Cobre"):
        drawCilinder(4, 3, "orange", screen)
        
    elif(cableMaterial == "Aluminio"):
        drawCilinder(4, 3, "grey", screen)
        
    elif(cableMaterial == "Grafito"):
        drawCilinder(4, 3, "black", screen)