# Devin Theriault
# 06/29/2026
# P4LAB1
# Using turtle and loops to draw a house

# import turtle library
import turtle

# Create the turtle window and object
canvas = turtle.Screen()
canvas.bgcolor("blue")
cursor = turtle.Turtle()

# Set turtle options
cursor.pensize(5)
cursor.pencolor("orange")
cursor.shape("arrow")

# Code to draw the base of the house
for side in range(4):
    cursor.forward(100)
    cursor.left(90)

# Code to move cursor to roof position
cursor.left(90)
cursor.forward(100)
cursor.right(90)

# While loop that executes 3 times to draw the roof also fill color or roof.
cursor.fillcolor("red")
cursor.begin_fill()
sides = 3
while sides > 0:
    cursor.forward(100)
    cursor.left(120)
    sides = sides - 1
cursor.end_fill()



# Wait for user to close window
canvas.mainloop()
