import turtle
import time

def electronAnimation(turti: turtle, len: float):

    turti.setposition(0, 0)
    time.sleep(1)

    turti.shape('circle')
    turti.pencolor('blue')
    turti.fillcolor('blue')
    turti.shapesize(1,1)
    turti.speed('slowest')
    turti.showturtle()
    
    turti.forward(len)
    
#Function to draw a grid
def draw_grid(step, size,turtle):
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(i, -size)
        turtle.pendown()
        turtle.goto(i, size)
        
    for i in range(-size, (size+1), step):
        turtle.penup()
        turtle.goto(-size, i)
        turtle.pendown()
        turtle.goto(size, i)

def drawAxis(screenSize: float, screen):
    t1 = turtle.RawTurtle(screen)
    t2 = turtle.RawTurtle(screen)
    t3 = turtle.RawTurtle(screen)
    t4 = turtle.RawTurtle(screen)
    t5 = turtle.RawTurtle(screen)
    t6 = turtle.RawTurtle(screen)

    turtles = [t1,t2,t3,t4,t5,t6]

    for x in turtles:
        x.pensize(3)
        x.shapesize(2,2,2)
    
    t1.pencolor("red")
    t2.pencolor("red")
    t3.pencolor("green")
    t4.pencolor("green")
    t5.pencolor("blue")
    t6.pencolor("blue")
    
    t1.forward(screenSize)
    t1.fillcolor("red")

    t2.left(180)
    t2.forward(screenSize)
    t2.fillcolor("red")

    t3.left(90)
    t3.forward(screenSize)
    t3.fillcolor("green")

    t4.right(90)
    t4.forward(screenSize)
    t4.fillcolor("green")

    t5.left(20)
    t5.forward(screenSize)
    t5.fillcolor("blue")

    t6.right(160)
    t6.forward(screenSize)
    t6.fillcolor("blue")

#To use this method, the radius passed to the method has to be in mm and the length in meters
#The conversions are made inside the method so the scale is better for the simulation
def drawCilinder(radius: float, length: float, wireColor: float, screen):

    radius = radius * 10
    length = length * 100

    SIZE = 30

    turt = turtle.RawTurtle(screen)
    turt.speed(4)

    turt.setposition( length / 2 , 0)
    turt.shape('square')
    turt.shapesize(radius * 2 / SIZE, length / 20)
    turt.fillcolor(wireColor)
    turt.stamp()

    turt.shape('circle')
    turt.shapesize(stretch_len= radius / SIZE)
    turt.backward(length/2)
    turt.stamp()

    turt.forward(2)
    turt.pencolor(wireColor)
    turt.stamp()

    turt.forward(length - 5)

    if(wireColor == "black"):
        turt.color("white")
    else:
        turt.color("black")

    turt.stamp()
    turt.hideturtle()

    electronAnimation(turt, length)