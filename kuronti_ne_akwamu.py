"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Kuronti ne Akwamu
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
# Function to find the distance between two coordinates
def coordinate_distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    distance = math.sqrt((dx * dx) + (dy * dy))
    return distance

# Function to draw vertical lines
def draw_vertical_lines(x1, y1, division, space, length):
    for line in range(0, division):
        turtle.penup()
        turtle.setposition(x1, y1)
        x1 = x1 + space
        turtle.pendown()
        turtle.forward(length)

# Function to draw horizontal lines
def draw_horizontal_lines(x1, y1, division, space, length):
     for line in range(0, division):
         turtle.penup()
         turtle.setposition(x1, y1)
         y1 = y1 + space        
         turtle.pendown()
         turtle.forward(length)

# Lift up the pen and set the pen size to 20
turtle.penup()
turtle.pensize(20)

# Draw the outer square
length = coordinate_distance(-180, 180, 180, 180)
drawSquare(length)

# Draw the horizontal center line
turtle.setposition(-180, 0)
turtle.pendown()
turtle.forward(length)
turtle.penup()

# Draw the vertical center line
turtle.setheading(90)
turtle.setposition(0, -180)
turtle.pendown()
turtle.forward(length)

# Reduce the pen size to 5
turtle.pensize(5)

# Draw the vertical lines in the upper left quadrant
length = int(length / 2)
draw_vertical_lines(-160, 0, 15, 10, length)

# Draw the horizontal lines in the upper left quadrant
turtle.setheading(0)
draw_horizontal_lines(-180, 20, 15, 10, length)

# Draw the vertical lines in the bottom right quadrant
turtle.setheading(90)
draw_vertical_lines(20, -180, 15, 10, length)

# Draw the horizontal lines in the bottom right quadrant
turtle.setheading(0)
draw_horizontal_lines(0, -160, 15, 10, length)

# End the program
turtle.done()
