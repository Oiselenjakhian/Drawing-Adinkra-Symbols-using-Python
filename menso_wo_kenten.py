"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Menso Wo Kenten
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
 
# Place code here
# Set the pensize of the turtle to 10
turtle.pensize(10)

# Lift up the pen
turtle.penup()

# Place the turtle at the position (0, 55)
turtle.setposition(0, 55)

# Place the turtle down
turtle.pendown()

# Move the turtle to the position (15, 30)
turtle.setposition(15, 30)

# Move the turtle to the position (50, 30)
turtle.setposition(50, 30)

# Move the turtle to the position (35, 0)
turtle.setposition(35, 0)

# Move the turtle to the position (50, -30)
turtle.setposition(50, -30)

# Move the turtle to the position (15, -30)
turtle.setposition(15, -30)

# Move the turtle to the position (0, -55)
turtle.setposition(0, -55)

# Move the turtle to the position (-15, -30)
turtle.setposition(-15, -30)

# Move the turtle to the position (-50, -30)
turtle.setposition(-50, -30)

# Move the turtle to the position (-35, 0)
turtle.setposition(-35, 0)

# Move the turtle to the position (-50, 30)
turtle.setposition(-50, 30)

# Move the turtle to the position (-15, 30)
turtle.setposition(-15, 30)

# Move the turtle the the position (0, 55)
turtle.setposition(0, 55)

# Lift up the pen
turtle.penup()

# Place the turtle at the position (0, 110)
turtle.setposition(0, 110)

# Place the turtle down
turtle.pendown()

# Move the turtle to the position (30, 60)
turtle.setposition(30, 60)

# Move the turtle to the position (100, 60)
turtle.setposition(100, 60)

# Move the turtle to the position (70, 0)
turtle.setposition(70, 0)

# Move the turtle to the position (100, -60)
turtle.setposition(100, -60)

# Move the turtle to the position (30, -60)
turtle.setposition(30, -60)

# Move the turtle to the position (0, -110)
turtle.setposition(0, -110)

# Move the turtle to the position (-30, -60)
turtle.setposition(-30, -60)

# Move the turtle to the position (-100, -60)
turtle.setposition(-100, -60)

# Move the turtle to the position (-70, 0)
turtle.setposition(-70, 0)

# Move the turtle to the position (-100, 60)
turtle.setposition(-100, 60)

# Move the turtle to the position (-30, 60)
turtle.setposition(-30, 60)

# Move the turtle the the position (0, 110)
turtle.setposition(0, 110)

# Lift up the pen
turtle.penup()

# Place the turtle at the position (0, 165)
turtle.setposition(0, 165)

# Place the turtle down
turtle.pendown()

# Move the turtle to the position (45, 90)
turtle.setposition(45, 90)

# Move the turtle to the position (150, 90)
turtle.setposition(150, 90)

# Move the turtle to the position (105, 0)
turtle.setposition(105, 0)

# Move the turtle to the position (150, -90)
turtle.setposition(150, -90)

# Move the turtle to the position (45, -90)
turtle.setposition(45, -90)

# Move the turtle to the position (0, -165)
turtle.setposition(0, -165)

# Move the turtle to the position (-45, -90)
turtle.setposition(-45, -90)

# Move the turtle to the position (-150, -90)
turtle.setposition(-150, -90)

# Move the turtle to the position (-105, 0)
turtle.setposition(-105, 0)

# Move the turtle to the position (-150, 90)
turtle.setposition(-150, 90)

# Move the turtle to the position (-45, 90)
turtle.setposition(-45, 90)

# Move the turtle the the position (0, 165)
turtle.setposition(0, 165)
 
# End the program
turtle.done()
