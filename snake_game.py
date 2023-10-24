import turtle
my_screen = turtle.Screen()
my_screen.bgcolor('black')
my_screen.setup(600, 600)
my_screen.title("Snake")

snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("green")
snake_head.direction = ""
snake_head.penup()
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)
    # if

def go_up():
    snake_head.direction = "up"

# def go_down():

my_screen.listen()
my_screen.onkeypress(go_up, "Up")
# my_screen.onkeypress(go_down, "Down")
# TODO هر وقت از روی کیبورد دکمه جهت پایین را فشار می دهیم سر مار به سمت پایین حرکت نماید
def close():
    global running
    running = False

root = my_screen._root
root.protocol("WM_DELETE_WINDOW", close)
running = True
while running == True:
    my_screen.update()
    move()

