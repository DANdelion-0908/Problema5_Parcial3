import turtle
from Drawings import *
import tkinter as tk
import RandomWalk as rw

def Simulation(gorge, screen, cableMaterial, radius, length):
    """
    The function Simulation takes in parameters for a gorge, screen, cable material, radius, and length,
    and uses turtle graphics to simulate drawing a cylinder on the screen based on the given parameters.
    
    :param gorge: The parameter "gorge" is likely referring to a turtle object that is used for drawing
    on the screen. It is passed to the "draw_grid" and "drawAxis" functions
    :param screen: The "screen" parameter is the turtle graphics screen object on which the simulation
    will be displayed. It is used to clear the screen, update the screen, set the screen size, and
    control the screen tracer
    :param cableMaterial: The parameter "cableMaterial" is a string that represents the material of the
    cable. It can have the following values: "Oro" (gold), "Plata" (silver), "Cobre" (copper),
    "Aluminio" (aluminum), or "Gra
    :param radius: The radius parameter represents the radius of the cable in millimeters
    :param length: The length parameter represents the length of the cable in meters
    """
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
        drawCilinder(radius, length, "yellow", screen, 1)

    elif(cableMaterial == "Plata"):
        drawCilinder(radius, length, "white", screen, 1)

    elif(cableMaterial == "Cobre"):
        drawCilinder(radius, length, "brown", screen, 1)
        
    elif(cableMaterial == "Aluminio"):
        drawCilinder(radius, length, "grey", screen, 1)
        
    elif(cableMaterial == "Grafito"):
        drawCilinder(radius, length, "black", screen, 1)

def SimulateRandomWalk(gorge, screen):
    rw.SimulateRandom(gorge, "white", screen)