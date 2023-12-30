"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Hwemudua
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
turtle.speed(1000000)
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
 
# Place code here
# Lift up the pen
turtle.penup()

# Set the pen size to 40
turtle.pensize(40)

# Move the turtle to the position (-160, -170)
turtle.setposition(-160, -170)

# Place the pen down
turtle.pendown()

# Move forward by 320 pixels
turtle.forward(320)

# Lift up the pen
turtle.penup()

# Move the turtle to the position (-120, 170)
turtle.setposition(-120, 170)

# Place the pen down
turtle.pendown()

# Move forward by 240 pixels
turtle.forward(240)

# Lift up the pen
turtle.penup()

# Move the pen to (-170, -80)
turtle.setposition(-170, -80)

# Set the heading to 90 degrees
turtle.setheading(90)

# Place the pen down
turtle.pendown()

# Move forward by 130 pixels
turtle.forward(130)

# Set the heading of the pen to 0 degrees
turtle.setheading(0)

# Move the turtle forward by 340
turtle.forward(340)

# Set the heading of the pen to 270 degrees
turtle.setheading(270)

# Move the pen 130 pixels forward
turtle.forward(130)

# Lift up the pen
turtle.penup()

# Move the pen to the position (-80, -170)
turtle.setposition(-80, -170)

# Set the heading of the turtle to 90 degrees
turtle.setheading(90)

# Place the pen down
turtle.pendown()

# Move the turtle forward by 200 pixels
turtle.forward(200)

# Lift up the pen
turtle.penup()

# Move the pen to the position (0, -80)
turtle.setposition(0, -80)

# Set the heading of the turtle to 90 degrees
turtle.setheading(90)

# Place the pen down
turtle.pendown()

# Move forward by 250 pixels
turtle.forward(250)

# Lift up the pen
turtle.penup()

# Move the pen to the position (80, -170)
turtle.setposition(80, -170)

# Set the heading of the turtle to 90 degrees
turtle.setheading(90)

# Place the pen down
turtle.pendown()

# Move forward by 200 pixels
turtle.forward(200)
 
# End the program
turtle.done()
