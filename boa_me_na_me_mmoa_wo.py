"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Boa Me Na Me Mmoa Wo
Developer Name: Truston Ailende
Email Address: trustonailende@gmail.com
"""
import turtle
import math
 
# Square
def drawSquare(length):
    turtle.penup()
    turtle.setposition(-length/2.0, length/2.0)
    turtle.pendown()
    for i in range(0, 4):
        turtle.forward(length)
        turtle.right(90)
    turtle.penup()
    turtle.home()
 
# Horizontal lines
def drawHorizontalLine(length, division):
    pixelSpace = int(length / division)
    half = int(length / 2)
    for j in range((-half + pixelSpace), half, pixelSpace):
        turtle.penup()
        turtle.setposition(-half, j)
        turtle.pendown()
        turtle.forward(length)
    turtle.penup()
    turtle.home()
 
# Vertical lines
def drawVerticalLine(length, division):
    pixelSpace = int(length / division)
    half = int(length / 2)
    turtle.right(90)
    for k in range((-half + pixelSpace), half, pixelSpace):
        turtle.penup()
        turtle.setposition(k, half)
        turtle.pendown()
        turtle.forward(length)
    turtle.penup()
    turtle.home()
 
# Draw the grid
turtle.speed(0)
drawSquare(400)
drawHorizontalLine(400, 40)
drawVerticalLine(400, 40)
 
# Change the colour mode
turtle.colormode(255)
 
# Change the pencolor to red
turtle.pencolor(255, 0, 0)
 
# Draw the horizontal centre line
turtle.setposition(-200, 0)
turtle.pendown()
turtle.forward(400)
turtle.penup()
 
# Draw the vertical centre line
turtle.setposition(0, 200)
turtle.setheading(270)
turtle.pendown()
turtle.forward(400)
 
# Reset all the properties
turtle.home()
turtle.pencolor(0, 0, 0)
 
# Lift up the pen
turtle.penup()

# Move the pen to the position (0, -170)
turtle.setposition(0, -170)

# Set the pen size to 60 pixels
turtle.pensize(60)

# Set the heading of the pen to 90 degrees
turtle.setheading(90)

# Place the pen down
turtle.pendown()

# Move forward by 30 pixels
turtle.forward(30)

# Reduce the pen size to 1
turtle.pensize(1)

# Lift up the pen
turtle.penup()

# Move the pen to the location (-80, -140)
turtle.setposition(-80, -140)

# Put the pen down
turtle.pendown()

# Draw a filled shape from (-80, -140) to (80, -140) to (0, 0) and back to (-80, -140) with a fill colour of black
turtle.color("black", "black")
turtle.begin_fill()
turtle.setposition(80, -140)
turtle.setposition(0, 0)
turtle.setposition(-80, -140)
turtle.end_fill()

# Lift up the pen
turtle.penup()

# Move the pen to the location (90, 0)
turtle.setposition(90, 0)

# Set the heading of the pen to 90 degrees
turtle.setheading(90)

# Set the pen size to 30
turtle.pensize(30)

# Place the pen down
turtle.pendown()

# Draw a circle of radius 90
turtle.circle(90)

# Lift up the pen
turtle.penup()

# Move the pen to the location (0, -85)
turtle.setposition(30, -85)

# Set the heading of the pen to 90 degrees
turtle.setheading(90)

# Set the fill colour to white
turtle.color("black", "white")

# Place the pen down
turtle.pendown()

# Reduce the pen size to 1
turtle.pensize(1)

# Draw a filled circle of radius 30 pixels
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# Lift up the pen
turtle.penup()

# Move the pen to the location (0, 0)
turtle.setposition(0, 0)

# Set the fill colour to black
turtle.color("black", "black")

# Place the pen down
turtle.pendown()

# Draw a filled shape from (0, 0) to (80, 135) to (-80, 135) and back to (0, 0) with a fill colour of black
turtle.begin_fill()
turtle.setposition(80, 135)
turtle.setposition(-80, 135)
turtle.setposition(0, 0)
turtle.end_fill()

# Lift up the pen
turtle.penup()

# Move the pen to the location (-25, 60)
turtle.setposition(-25, 60)

# Draw a filled square of length 50 pixels
turtle.color("black", "white")
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.end_fill()

# Lift up the pen
turtle.penup()

# Move the pen to the location (33, 167)
turtle.setposition(33, 167)

# Place the pen down
turtle.pendown()

# Reset the colour of the pen back to black
turtle.color("black", "black")

# Draw a filled circle of radius 32.5 pixel
turtle.begin_fill()
turtle.circle(33)
turtle.end_fill()
 
# End the program
turtle.done()
