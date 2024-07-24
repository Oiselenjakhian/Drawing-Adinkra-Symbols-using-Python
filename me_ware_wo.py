"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Me Ware Wo
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
def draw_me_ware_wo_quarter(x_center, y_center):
    turtle.setheading(90)
    turtle.pensize(1)
    turtle.penup()
    turtle.setposition(x_center + 30, y_center)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.setposition(x_center, y_center)
    turtle.setheading(270)
    turtle.pensize(20)
    turtle.pendown()
    turtle.forward(80)
    turtle.setheading(0)
    turtle.circle(80)

# Draw the shape in the upper left quadrant
draw_me_ware_wo_quarter(-90, 90)

# Draw the shape in the upper right quadrant
draw_me_ware_wo_quarter(90, 90)

# Draw the shape in the lower right quadrant
draw_me_ware_wo_quarter(90, -90)

# Draw the shape in the lower left quadrant
draw_me_ware_wo_quarter(-90, -90)
 
# End the program
turtle.done()
