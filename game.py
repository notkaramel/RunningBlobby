from pythonosc.udp_client import SimpleUDPClient
import turtle as t

DEFAULT_IP      = "127.0.0.1" # localhost
DEFAULT_PORT    = 57110       # default SuperCollider port

GAME_TITLE      = "Running Blobby"
GAME_BG_COLOR   = "lightblue"
GAME_WIDTH      = 800
GAME_HEIGHT     = 400

STEP            = 10

# LEFT = -window.window_width() / 2
# RIGHT = window.window_width() / 2
# TOP = window.window_height() / 2
# BOTTOM = -window.window_height() / 2

# --------------- CREATE THE GAME --------------- #
# Set up the game


def move_left():
    character.setx(character.xcor() - STEP)
    create_character()
    walk(1)

def move_right():
    character.setx(character.xcor() + STEP)
    create_character()
    walk(-1)


character = t.Turtle()

def create_character():
    global character
    character.clear()
    character.penup()
    character.color(1, 1, 1)
    character.shape("square")

    character.turtlesize(1, 4)  # Base
    character.stamp()
    character.sety(10)
    character.turtlesize(1, 1.5)  # Next tier
    character.stamp()
    character.sety(20)
    character.turtlesize(0.8, 0.3)  # Tip of cannon
    character.stamp()
    character.sety(0)

    character.setposition(0, 0)


# --------------- CREATE THE OSC CLIENT --------------- #
def getOSCClient():
    global client
    ip = input(f"Input your server address [{DEFAULT_IP}]: ") or DEFAULT_IP
    port = int(input(f"Input your server's port [{DEFAULT_PORT}]: ") or DEFAULT_PORT) 
    client = SimpleUDPClient(ip, port)
    client.send_message("/hello", "world")

def walk(position: int) -> None:
    """
    - position: [-1, +1] -1 is most left, +1 is most right
    - speed: frequency kind of
    """
    client.send_message("/s_new", ["walk", -1, 1, 1, "position", position])


def jump(position: int, speed: int) -> None:
    """
    - position: [-1, +1] -1 is most left, +1 is most right
    - speed: frequency kind of
    """
    client.send_message("/s_new", ["jump", -1, 1, 1, "position", position, "speed", speed])

if __name__ == "__main__":
    getOSCClient()
    create_character()

    screen = t.Screen()
    screen.title(GAME_TITLE)
    screen.bgcolor(GAME_BG_COLOR)
    screen.setup(width=GAME_WIDTH, height=GAME_HEIGHT)

    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    screen.onkeypress(t.bye, "q")
    screen.listen()
    t.done()
