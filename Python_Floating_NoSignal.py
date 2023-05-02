import turtle
import random
import math

#Let us set up the turtle screen
canvas = turtle.Screen()
canvas.bgcolor("black")
canvas.title("Floating No Signal")

#Let us create the turtle for 'No Signal' message.
no_signal = turtle.Turtle()
no_signal.hideturtle()
no_signal.penup()
no_signal.color("white")
no_signal.setpos(-50, 0)
no_signal.write("NO SIGNAL", font=("Fixedsys", 45, "bold"))

#Let us define the boundries of the screen 
max_x = int(canvas.window_width()) - 250
max_y = int(canvas.window_height()) - 250
min_x = -max_x
min_y = -max_y

#Let us define movement parameter for our script('NO SIGNAL').
step_size = 2
angle_range = 10

# We need to turn off turtle's automatic screen updates.
turtle.tracer(0)

# In this step, we need a loop for moving our turtle randomly and redrawing the message('NO SIGNAL').
while True:
    # Let us get the current position of 'NO SIGNAL'.
    x, y = no_signal.position()
    angle = no_signal.heading()

    # Determine the new position and angle of the "no signal" message
    angle += random.randint(-angle_range, angle_range)
    x += step_size * math.cos(math.radians(angle))
    y += step_size * math.sin(math.radians(angle))

    # Time to check if 'NO SIGNAL' text comes to the edges of the screen
    if x > max_x:
        x = max_x
        angle = 180 - angle
    elif x < min_x:
        x = min_x
        angle = 180 - angle
    if y > max_y:
        y = max_y
        angle = 360 - angle
    elif y < min_y:
        y = min_y
        angle = 360 - angle - 180 # Here, 360 degrees are subtracted after subtracting 180 degrees from the turtle's current direction. As a result of this action, the direction is updated as the direction it's facing straight ahead (ie, 180 degrees opposite).


   # Below codes to move 'NO SIGNAL' message to new position and angle
    no_signal.setheading(angle)
    no_signal.goto(x, y)
    no_signal.clear()
    no_signal.write("NO SIGNAL", font=("Fixedsys", 45, "bold"))
    turtle.update()