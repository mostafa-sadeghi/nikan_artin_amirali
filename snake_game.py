import turtle
import random
import time
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(600,600)


def create_turtle(s, c):
    my_turtle = turtle.Turtle()
    my_turtle.shape(s)
    my_turtle.color(c)
    my_turtle.penup()
    return my_turtle

def change_position():
    x = random.randint(-270, 270)
    y = random.randint(-270, 230)
    snake_food.goto(x,y)
def move():
    if snake_head.direction == "up":
        ypos = snake_head.ycor()
        ypos += 20
        snake_head.sety(ypos)

    if snake_head.direction == "down":
        ypos = snake_head.ycor()
        ypos -= 20
        snake_head.sety(ypos)

    if snake_head.direction == "right":
        xpos = snake_head.xcor()
        xpos += 20
        snake_head.setx(xpos)
    if snake_head.direction == "left":
        xpos = snake_head.xcor()
        xpos -= 20
        snake_head.setx(xpos)   














def go_up():
    snake_head.direction = "up" 
        
def go_down():
    snake_head.direction = "down"

def go_right():
    snake_head.direction = "right"

def go_left():
    snake_head.direction = "left"



snake_head = create_turtle("square", "darkgreen")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position()
screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_right,"Right")
screen.onkeypress(go_left,"Left")


running = True
while running:
    screen.update()
    move()
    time.sleep(0.2)


