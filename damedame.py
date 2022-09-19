"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Dame Dame
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
# Set the pensize to 20
turtle.pensize(20)

# Draw the filled center square
turtle.setposition(-60, 60)
turtle.pendown()
turtle.begin_fill()
turtle.forward(120)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.end_fill()

# Draw the outer circle
turtle.penup()
turtle.setposition(0, -170)
turtle.pendown()
turtle.circle(170)

# Draw the right handle
turtle.penup()
turtle.setheading(0)
turtle.setposition(60, 20)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(50)

# Draw the line joining the right handle to the circle
turtle.penup()
turtle.setheading(0)
turtle.setposition(110, 0)
turtle.pendown()
turtle.forward(50)

# Draw the top handle
turtle.penup()
turtle.setheading(90)
turtle.setposition(-20, 60)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(50)

# Draw the line joining the top handle to the circle
turtle.penup()
turtle.setheading(90)
turtle.setposition(0, 110)
turtle.pendown()
turtle.forward(50)

# Draw the left handle
turtle.penup()
turtle.setheading(180)
turtle.setposition(-60, -20)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(50)

# Draw the line joining the left handle to the circle
turtle.penup()
turtle.setheading(180)
turtle.setposition(-110, 0)
turtle.pendown()
turtle.forward(50)

# Draw the bottom handle
turtle.penup()
turtle.setheading(270)
turtle.setposition(20, -60)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(50)

# Draw the line joining the bottom handle to the circle
turtle.penup()
turtle.setheading(270)
turtle.setposition(0, -110)
turtle.pendown()
turtle.forward(50)

# End the program
turtle.done()
