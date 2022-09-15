"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Akoma Ntoaso
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
 
# Place code here
def coordinateDistance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    D = math.sqrt((dx * dx) + (dy * dy))
    return D

# Draw the top left diagonal
turtle.penup()
turtle.setposition(-200, 200)
turtle.setheading(315)
diagonalLength = coordinateDistance(-200, 200, 200, -200)
turtle.pendown()
turtle.forward(diagonalLength)

# Draw the bottom left diagonal
turtle.penup()
turtle.setposition(-200, -200)
turtle.setheading(45)
diagonalLength = coordinateDistance(-200, -200, 200, 200)
turtle.pendown()
turtle.forward(diagonalLength)

# Reset the colour back to black
turtle.pencolor(0, 0, 0)

# Reset the heading to 0
turtle.setheading(0)
turtle.penup()
turtle.home()

# Draw the center circle
turtle.penup()
turtle.setposition(0, -70)
turtle.pendown()
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()

# Draw a line in the upper left quadrant
turtle.penup()
turtle.setposition(-165, 30)
turtle.setheading(45)
diagonalLength = coordinateDistance(-165, 30, -30, 165)
turtle.pendown()
turtle.forward(diagonalLength)

# Draw a semi-circle in the upper left quadrant
turtle.penup()
turtle.setposition(-30, 165)
turtle.pendown()
turtle.setheading(135)
turtle.begin_fill()
turtle.circle(diagonalLength/2, 180)
turtle.end_fill()

# Draw a line from the center of the circle to the upper left semi-circle
turtle.penup()
turtle.home()
turtle.setheading(135)
turtle.pendown()
turtle.pensize(30)
turtle.forward(diagonalLength * 0.75)

# Draw a line in the upper right quadrant
turtle.penup()
turtle.home()
turtle.pensize(1)
turtle.setposition(30, 165)
turtle.setheading(-45)
diagonalLength = coordinateDistance(30, 165, 165, 30)
turtle.pendown()
turtle.forward(diagonalLength)

# Draw a semi-circle in the upper right quadrant
turtle.penup()
turtle.setposition(165, 30)
turtle.pendown()
turtle.setheading(45)
turtle.begin_fill()
turtle.circle(diagonalLength/2, 180)
turtle.end_fill()

# Draw a line from the center of the circle to the upper right semi-circle
turtle.penup()
turtle.home()
turtle.setheading(45)
turtle.pendown()
turtle.pensize(30)
turtle.forward(diagonalLength * 0.75)

# Draw a line in the lower right quadrant
turtle.penup()
turtle.home()
turtle.pensize(1)
turtle.setposition(165, -30)
turtle.setheading(-135)
turtle.pendown()
turtle.forward(diagonalLength)

# Draw a semi-circle in the lower right quadrant
turtle.penup()
turtle.setposition(30, -165)
turtle.pendown()
turtle.setheading(-45)
turtle.begin_fill()
turtle.circle(diagonalLength/2, 180)
turtle.end_fill()

# Draw a line from the center of the circle to the lower right quadrant
turtle.penup()
turtle.home()
turtle.setheading(-45)
turtle.pendown()
turtle.pensize(30)
turtle.forward(diagonalLength * 0.75)

# Draw a line in the lower left quadrant
turtle.penup()
turtle.home()
turtle.pensize(1)
turtle.setposition(-30, -165)
turtle.setheading(135)
turtle.pendown()
turtle.forward(diagonalLength)

# Draw a semi-circle in the lower left quadrant
turtle.penup()
turtle.setposition(-165, -30)
turtle.pendown()
turtle.setheading(225)
turtle.begin_fill()
turtle.circle(diagonalLength/2, 180)
turtle.end_fill()

# Draw a line from the center of the circle to the lower left quadrant
turtle.penup()
turtle.home()
turtle.setheading(225)
turtle.pendown()
turtle.pensize(30)
turtle.forward(diagonalLength * 0.75)

# End the program
turtle.done()
