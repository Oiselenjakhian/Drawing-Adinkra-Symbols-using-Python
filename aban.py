"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Aban
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
turtle.setheading(45)
turtle.setposition(0, 80)
 
def coordinateDistance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    D = math.sqrt((dx * dx) + (dy * dy))
    return D
 
width = coordinateDistance(120, 0, 40, 80)
length = coordinateDistance(0, 80, 80, 160)
 
turtle.pensize(width/2)
turtle.pendown()
 
def drawTong():
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length / 2)
    turtle.left(90)
    turtle.forward(length * 5 / 8)
    turtle.penup()
    turtle.backward(length * 5 / 8)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(length / 2)
    turtle.right(90)
    turtle.forward(length)
 
drawTong()
turtle.setheading(315)
drawTong()
turtle.setheading(225)
drawTong()
turtle.setheading(135)
drawTong()
 
# End the program
turtle.done()
