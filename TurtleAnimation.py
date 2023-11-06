import sys
from turtle import *
import colorsys

h = 0.1

def fun(jorge):
    global h
    for i in range (4):
        c = colorsys.hsv_to_rgb(h,1,1)
        jorge.fillcolor(c)
        h += 0.04
        jorge.begin_fill()
        jorge.fd(50)
        jorge.rt(20)
        jorge.fd(40)
        jorge.rt(9)
        jorge.end_fill()

def startAnimation(jorge):
    try:
        jorge.speed(0)
        jorge._color("black")
        jorge.pensize(4)
        while(1 == 1):
            for j in range(300):
                fun(jorge) 
                jorge.goto(0,0)
                jorge.rt(10)
    
    except:
        sys.exit()