"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Kyemfere
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
# Find the distance between two coordinates
def coordinate_distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    distance = math.sqrt((dx * dx) + (dy * dy))
    return distance

# Find the distance between (-190, 190) and (0, 0)
double_hypothenuse = coordinate_distance(-190, 190, 0, 0)

# Draw two triangle that are opposite facing and inverted
def draw_half_symbol(x_pos, y_pos, angle):
    turtle.penup()
    turtle.setposition(x_pos, y_pos)

    turtle.pendown()
    turtle.setheading(0)

    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(double_hypothenuse)
    turtle.right(135)
    turtle.forward(95)
    turtle.right(90)
    turtle.forward(190)
    turtle.left(90)
    turtle.forward(95)
    turtle.end_fill()

# Draw half symbols in various quadrants
draw_half_symbol(-190, 190, 45)
draw_half_symbol(-190, 0, 315)
draw_half_symbol(0, 190, 45)
draw_half_symbol(0, 0, 315)
draw_half_symbol(0, 0, 45)
draw_half_symbol(0, -190, 315)
draw_half_symbol(-190, 0, 45)
draw_half_symbol(-190, -190, 315)

# End the program
turtle.done()
