"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Abusua Pa
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
turtle.penup()
turtle.pensize(40)
turtle.setposition(-100, 100)
turtle.pendown()
 
def coordinateDistance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    D = math.sqrt((dx * dx) + (dy * dy))
    return D
 
length = coordinateDistance(-100, -100, 100, -100)
drawSquare(length)
 
turtle.setposition(-100, 0)
turtle.pendown()
turtle.forward(length)
turtle.penup()
turtle.setheading(90)
turtle.setposition(0, -100)
turtle.pendown()
turtle.forward(length)
 
turtle.penup()
turtle.setposition(50, 120)
turtle.pendown()
turtle.circle(50, 180)
 
turtle.penup()
turtle.setposition(120, -50)
turtle.setheading(0)
turtle.pendown()
turtle.circle(50, 180)
 
turtle.penup()
turtle.setposition(-50, -120)
turtle.setheading(270)
turtle.pendown()
turtle.circle(50, 180)
 
turtle.penup()
turtle.setposition(-120, 50)
turtle.setheading(180)
turtle.pendown()
turtle.circle(50, 180)
 
turtle.penup()
turtle.pensize(5)
turtle.setposition(-60, -100)
turtle.setheading(90)
turtle.pendown()
turtle.forward(length)
 
turtle.penup()
turtle.setposition(-40, -100)
turtle.setheading(90)
turtle.pendown()
turtle.forward(length)
 
turtle.penup()
turtle.setposition(40, -100)
turtle.setheading(90)
turtle.pendown()
turtle.forward(length)
 
turtle.penup()
turtle.setposition(60, -100)
turtle.setheading(90)
turtle.pendown()
turtle.forward(length)
 
turtle.penup()
turtle.setposition(-100, -60)
turtle.setheading(0)
turtle.pendown()
turtle.forward(length)
 
turtle.penup()
turtle.setposition(-100, -40)
turtle.setheading(0)
turtle.pendown()
turtle.forward(length)
 
turtle.penup()
turtle.setposition(-100, 40)
turtle.setheading(0)
turtle.pendown()
turtle.forward(length)
 
turtle.penup()
turtle.setposition(-100, 60)
turtle.setheading(0)
turtle.pendown()
turtle.forward(length)
 
# End the program
turtle.done()
