"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Mframadan
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
# Lift up the pen
turtle.penup()

# Set the pensize to 10
turtle.pensize(10)

# Draw the outer square
drawSquare(380)

# Draw the inner square
drawSquare(300)

# Draw the lower left line
turtle.penup()
turtle.setposition(-110, -150)
turtle.pendown()
turtle.setposition(150, 110)

# Draw the upper left line
turtle.penup()
turtle.setposition(-150, -110)
turtle.pendown()
turtle.setposition(110, 150)

# Draw the lower right line
turtle.penup()
turtle.setposition(110, -150)
turtle.pendown()
turtle.setposition(-150, 110)

# Draw the upper right line
turtle.penup()
turtle.setposition(150, -110)
turtle.pendown()
turtle.setposition(-110, 150)

# Draw the first horizontal line at the bottom
turtle.penup()
turtle.setposition(-80, -120)
turtle.pendown()
turtle.setposition(80, -120)

# Draw the second horizontal line at the bottom
turtle.penup()
turtle.setposition(-60, -100)
turtle.pendown()
turtle.setposition(60, -100)

# Draw the third horizontal line at the bottom
turtle.penup()
turtle.setposition(-40, -80)
turtle.pendown()
turtle.setposition(40, -80)

# Draw the fourth horizontal line at the bottom
turtle.penup()
turtle.setposition(-20, -60)
turtle.pendown()
turtle.setposition(20, -60)

# Draw the first horizontal line at the top
turtle.penup()
turtle.setposition(-80, 120)
turtle.pendown()
turtle.setposition(80, 120)

# Draw the second horizontal line at the top
turtle.penup()
turtle.setposition(-60, 100)
turtle.pendown()
turtle.setposition(60, 100)

# Draw the third horizontal line at the top
turtle.penup()
turtle.setposition(-40, 80)
turtle.pendown()
turtle.setposition(40, 80)

# Draw the fourth horizontal line at the top
turtle.penup()
turtle.setposition(-20, 60)
turtle.pendown()
turtle.setposition(20, 60)

# End the program
turtle.done()
