import turtle
import time



# Path
path = turtle.Turtle()
path.hideturtle()
path.speed(0)
path.penup()
path.goto(-400, -50)
path.pendown()
path.pensize(5)
path.color("black")
path.forward(800)

# Blob character
blob = turtle.Turtle()
blob.shape("square")
blob.color("green")
blob.penup()
blob.goto(0, -25)

# Variables
is_jumping = False
jump_height = 100
movement_speed = 10

# Movement functions
def move_left():
    x = blob.xcor() - movement_speed
    if x > -400:  # Keep blob within bounds
        blob.setx(x)

def move_right():
    x = blob.xcor() + movement_speed
    if x < 400:  # Keep blob within bounds
        blob.setx(x)

def jump():
    global is_jumping
    if not is_jumping:
        is_jumping = True
        # Jump up
        for _ in range(10):
            blob.sety(blob.ycor() + jump_height / 10)
            time.sleep(0.02)
        # Fall down
        for _ in range(10):
            blob.sety(blob.ycor() - jump_height / 10)
            time.sleep(0.02)
        is_jumping = False

# Key bindings
screen.listen()
screen.onkeypress(move_left, "Left")  # Arrow key left
screen.onkeypress(move_right, "Right")  # Arrow key right
screen.onkeypress(jump, "Up")  # Arrow key up for jump
screen.onkeypress(jump, "space")  # Space key for
