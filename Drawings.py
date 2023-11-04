import turtle

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

def drawAxis(screenSize: float):
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()
    t5 = turtle.Turtle()
    t6 = turtle.Turtle()

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
def drawCilinder(radius: float, length: float):

    radius = radius * 10
    length = length * 100

    SIZE = 20

    turt = turtle.Turtle()

    turt.setposition( length / 2 , 0)
    turt.shape('square')
    turt.shapesize(radius * 2 / SIZE, length / SIZE)
    turt.fillcolor("orange")
    turt.stamp()

    turt.shape('circle')
    turt.shapesize(stretch_len= radius / SIZE)
    turt.backward(length/2)
    turt.stamp()

    turt.forward(2)
    turt.pencolor('orange')
    turt.stamp()

    turt.forward(length - 5)
    turt.color('black')
    turt.stamp()

    print("This is a cilinder")

    turtle.done()