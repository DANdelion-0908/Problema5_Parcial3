import turtle
import time

def electronAnimation(turti: turtle, len: float):
    """
    The function `electronAnimation` uses the turtle module to animate the movement of a blue circle
    representing an electron.
    
    :param turti: The parameter "turti" is a turtle object that is used to control the turtle graphics.
    It is passed as an argument to the function so that the function can use the turtle object to draw
    and animate the electron
    :type turti: turtle
    :param len: The parameter "len" represents the length or distance that the turtle will move forward
    :type len: float
    """
    turti.penup()
    turti.setposition(0, 0)
    turti.back(1200)
    time.sleep(1)
    turti.pendown()

    turti.shape('circle')
    turti.pencolor('blue')
    turti.fillcolor('blue')
    turti.shapesize(1,1)
    turti.speed('slowest')
    turti.showturtle()
    
    turti.forward(len)
    
#Function to draw a grid
def draw_grid(step, size,turtle):
    """
    The function `draw_grid` takes in three parameters - `step`, `size`, and `turtle` - and uses the
    turtle module to draw a grid with horizontal and vertical lines.
    
    :param step: The step parameter determines the distance between each line in the grid. It specifies
    how far apart each line should be from each other
    :param size: The size parameter determines the size of the grid. It represents the maximum
    coordinate value in both the x and y directions. For example, if size is set to 10, the grid will
    span from -10 to 10 in both the x and y directions
    :param turtle: The "turtle" parameter is an instance of the turtle module that is used to draw on
    the screen. It is passed as an argument to the function so that the function can use the turtle to
    draw the grid
    """
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
    """
    The function `drawAxis` uses the turtle module to draw six colored lines representing the x and y
    axes on a given screen size.
    
    :param screenSize: The `screenSize` parameter represents the length of the axis that will be drawn
    on the screen
    :type screenSize: float
    :param screen: The `screen` parameter is the turtle screen object on which the axis will be drawn
    """
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
    
    t1.penup()
    t1.back(1200)
    t1.pendown()

    t2.penup()
    t2.back(1200)
    t2.pendown()

    t3.penup()
    t3.back(1200)
    t3.pendown()

    t4.penup()
    t4.back(1200)
    t4.pendown()

    t5.penup()
    t5.back(1200)
    t5.pendown()

    t6.penup()
    t6.back(1200)
    t6.pendown()

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
    """
    The function `drawCilinder` takes in parameters for the radius, length, wire color, and screen, and
    uses the turtle module to draw a cylinder shape with the specified dimensions and color.
    
    :param radius: The radius parameter represents the radius of the cylinder. It is a float value
    :type radius: float
    :param length: The "length" parameter represents the length of the cylinder
    :type length: float
    :param wireColor: The parameter "wireColor" is the color of the wireframe of the cylinder. It can be
    any valid color value, such as "red", "blue", "#FF0000", etc
    :type wireColor: float
    :param screen: The "screen" parameter is the turtle screen on which the cylinder will be drawn. It
    is the canvas or window where the turtle graphics will be displayed
    """

    radius = radius * 10
    length = length * 100

    SIZE = 30

    turt = turtle.RawTurtle(screen)
    turt.speed(4)

    turt.penup()
    turt.back(1200)
    turt.fd(length / 2)
    turt.pendown()

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