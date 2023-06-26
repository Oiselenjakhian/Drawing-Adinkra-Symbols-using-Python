"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: 
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
# Lift up the turtle
turtle.penup()

# Increase the pensize to 10
turtle.pensize(10)

# Set the heading of the turtle to 90
turtle.setheading(90)

# Move the turtle to the position (165, -160) at the right edge of the circle
turtle.setposition(165, -160)

# Place the turtle down
turtle.pendown()

# Draw a semi-circle of radius 165
turtle.circle(165, 180)

# Set the heading of the turtle to 0
turtle.setheading(0)

# Move the turtle to the position (-80, -160)
turtle.setposition(-80, -160)

# Move the turtle to the position (0, -80)
turtle.setposition(0, -80)

# Move the turtle to the position (80, -160)
turtle.setposition(80, -160)

# Move the turtle to the position (165, -160)
turtle.setposition(165, -160)

# Lift up the pen
turtle.penup()

# Move the turtle to the position (125, -140)
turtle.setposition(125, -140)

# Place the pen down
turtle.pendown()

# Set the heading of the circle to 90
turtle.setheading(90)

# Draw a semi-circle of radius 125
turtle.circle(125, 180)

# Move the turtle to the position (-90, -140)
turtle.setposition(-90, -140)

# Move the turtle to the position (0, -50)
turtle.setposition(0, -50)

# Move the turtle to the position (90, -140)
turtle.setposition(90, -140)

# Move the turtle to the position (125, -140)
turtle.setposition(125, -140)

# Lift up the turtle
turtle.penup()

# Move the turtle to the position (-165, 160)
turtle.setposition(-165, 160)

# Set the heading of the turtle to 270
turtle.setheading(270)

# Place the pen down
turtle.pendown()

# Draw a semi-circle of radius 165
turtle.circle(165, 180)

# Move the turtle to the position (80, 160)
turtle.setposition(80, 160)

# Move the turtle to the position (0, 80)
turtle.setposition(0, 80)

# Move the turtle to the position (-80, 160)
turtle.setposition(-80, 160)

# Move the turtle to the position (-165, 160)
turtle.setposition(-165, 160)

# Lift up the pen
turtle.penup()

# Move the turtle to the position (-125, 140)
turtle.setposition(-125, 140)

# Place the pen down
turtle.pendown()

# Set the heading of the pen to 270
turtle.setheading(270)

# Draw a semi-circle of radius 125
turtle.circle(125, 180)

# Move to the position (90, 140)
turtle.setposition(90, 140)

# Move to the position (0, 50)
turtle.setposition(0, 50)

# Move to the position (-90, 140)
turtle.setposition(-90, 140)

# Move the turtle to the position (-125, 140)
turtle.setposition(-125, 140)

# Draw the line that erases the point of intersection between the two semi-circles
turtle.penup()
turtle.setposition(-30, 0)
turtle.setheading(0)
turtle.pendown()
turtle.pencolor(255, 255, 255)
turtle.pensize(20)
turtle.forward(60)

# End the program
turtle.done()
