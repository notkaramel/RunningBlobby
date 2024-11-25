from pythonosc.udp_client import SimpleUDPClient
import turtle as t

# --------------- Metadata & default values --------------- #
DEFAULT_IP = "127.0.0.1"  # localhost
DEFAULT_PORT = 57110       # default SuperCollider port

GAME_TITLE = "Running Blobby"
GAME_BG_COLOR = "lightblue"
GAME_WIDTH = 800
GAME_HEIGHT = 800
BORDER = 20

# --------------- CREATE THE GAME --------------- #
STEP = 100
SPEED = 4


def create_box():
    box = t.Turtle()
    box.penup()
    box.color(0.6, 0.7, 1)
    box.speed(100)
    box.goto(-GAME_HEIGHT/2 - BORDER, -GAME_WIDTH/2 - BORDER)
    box.pensize(BORDER)
    box.pendown()

    box.goto(-GAME_HEIGHT/2 - BORDER, GAME_WIDTH/2 + BORDER)
    box.goto(GAME_HEIGHT/2 + BORDER, GAME_WIDTH/2 + BORDER)
    box.goto(GAME_HEIGHT/2 + BORDER, -GAME_WIDTH/2 - BORDER)
    box.goto(-GAME_HEIGHT/2 - BORDER, -GAME_WIDTH/2 - BORDER)


def create_character():
    character.clear()
    character.penup()
    character.color(1, 1, 1)
    character.shape("square")
    character.turtlesize(1, 1)
    character.speed(SPEED)


def move_left():
    if (character.xcor() - STEP >= - GAME_WIDTH/2):
        character.setx(character.xcor() - STEP)
        walk(character.xcor(), character.ycor())
    else:
        wall(character.xcor(), character.ycor())


def move_right():
    if (character.xcor() + STEP <= GAME_WIDTH/2):
        character.setx(character.xcor() + STEP)
        walk(character.xcor(), character.ycor())
    else:
        wall(character.xcor(), character.ycor())


def move_up():
    if (character.ycor() + STEP <= GAME_HEIGHT/2):
        character.sety(character.ycor() + STEP)
        walk(character.xcor(), character.ycor())
    else:
        wall(character.xcor(), character.ycor())


def move_down():
    if (character.ycor() - STEP >= -GAME_HEIGHT/2):
        character.sety(character.ycor() - STEP)
        walk(character.xcor(), character.ycor())
    else:
        wall(character.xcor(), character.ycor())


def action():
    character.turtlesize(2)
    spin(character.xcor(), character.ycor())
    character.tilt(360)
    character.turtlesize(1)
    print(character.xcor(), character.ycor())


# --------------- CREATE THE OSC CLIENT --------------- #
def getOSCClient():
    global client
    ip = input(f"Input your server address [{DEFAULT_IP}]: ") or DEFAULT_IP
    port = int(input(f"""Input your server's port [{
               DEFAULT_PORT}]: """) or DEFAULT_PORT)
    client = SimpleUDPClient(ip, port)
    client.send_message("/hello", "world")


def walk(x: int, y: int) -> None:
    """
    - position: [-1, +1] -1 is most left, +1 is most right
    """
    client.send_message(
        "/s_new", ["walk", -1, 1, 1, "xPosition", x, "yPosition", y])


def wall(x: int, y: int) -> None:
    """
    - position: [-1, +1] -1 is most left, +1 is most right
    """
    client.send_message(
        "/s_new", ["wall", -1, 1, 1, "xPosition", x, "yPosition", y])


def spin(x: int, y: int) -> None:
    """
    - position: [-1, +1] -1 is most left, +1 is most right
    """
    client.send_message(
        "/s_new", ["spin", -1, 1, 1, "xPosition", x, "yPosition", y])


# --------------- The Game --------------- #

if __name__ == "__main__":
    # Create the client
    getOSCClient()

    try:
        screen = t.Screen()
        screen.title(GAME_TITLE)
        screen.bgcolor(GAME_BG_COLOR)
        screen.setup(width=GAME_WIDTH, height=GAME_HEIGHT)
        create_box()

        character = t.Turtle()
        create_character()
        character.setposition(0, 0)

        screen.onkey(move_left, "Left")
        screen.onkey(move_right, "Right")
        screen.onkey(move_up, "Up")
        screen.onkey(move_down, "Down")

        screen.onkey(action, "space")
        screen.onkey(t.bye, "q")
        screen.listen()
        t.done()
    except KeyboardInterrupt:
        t.bye()
