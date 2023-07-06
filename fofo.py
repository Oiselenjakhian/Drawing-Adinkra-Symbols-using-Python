"""
Project Name: Drawing Adinkra Symbols using Python
Symbol Name: Fofoo
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

# Move the turtle to the position that is 50 pixels from the centre of the symbol
turtle.setposition(0, -50)

# Place the pen down
turtle.pendown()

# Set the pensize to 40 pixels
turtle.pensize(40)

# Draw a circle of radius 50 pixels
turtle.circle(50)

# Draw petal function
def draw_petal(heading):
    # Lift up the turtle
    turtle.penup()

    # Move the turtle back to the centre
    turtle.home()

    # Change the pensize to 30 pixels
    turtle.pensize(30)

    # Set the heading
    turtle.setheading(heading)

    # Move forward by 50 pixels
    turtle.forward(50)

    # Place the pen down
    turtle.pendown()

    # Move the turtle forward by 80 pixels
    turtle.forward(80)

    # Set the heading to heading - 90
    turtle.setheading(heading - 90)

    # Set the pensize to 1 pixel
    turtle.pensize(1)

    # Draw a filled circle of radius 30 degrees
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

heading = 90
while(heading <= 410):
    draw_petal(heading)
    heading = heading + 40
 
# End the program
turtle.done()
