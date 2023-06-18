"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Epa
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
# Set the pensize to 40
turtle.pensize(40)

# Lift up the pen
turtle.penup()

# Move the pen to the position (-170, 0)
turtle.setposition(-170, 0)

# Draw the line from (-170, 0) to (-80, 100)
turtle.pendown()
turtle.setposition(-80, 100)

# Draw a line to position
turtle.setposition(80, 0)

# Draw the inner upper line for the left side
turtle.penup()
turtle.setposition(-80, 100)
turtle.pendown()
turtle.setposition(50, 0)

# Move the pen back to the starting position
turtle.penup()
turtle.setposition(-170, 0)

# Move to the position (-70, -100)
turtle.pendown()
turtle.setposition(-70, -100)

# Move to the position (80, 0)
turtle.setposition(80, 0)

# Draw the inner lower line for the left side
turtle.penup()
turtle.setposition(-70, -100)
turtle.pendown()
turtle.setposition(50, 0)

# Move the pen to the position (170, 0)
turtle.penup()
turtle.setposition(170, 0)

# Draw the line from (170, 0) to (-80, 100)
turtle.pendown()
turtle.setposition(80, 100)

# Draw a line to position
turtle.setposition (-80, 0)

# Draw the inner upper line for the right side
turtle.penup()
turtle.setposition(80, 100)
turtle.pendown()
turtle.setposition(-50, 0)

# Move the pen back to the starting position
turtle.penup()
turtle.setposition(170, 0)

# Move to the position (70, -100)
turtle.pendown()
turtle.setposition(70, -100)

# Move to the position (80, 0)
turtle.setposition(-80, 0)

# Draw the inner lower line for the left side
turtle.penup()
turtle.setposition(70, -100)
turtle.pendown()
turtle.setposition(-50, 0)
