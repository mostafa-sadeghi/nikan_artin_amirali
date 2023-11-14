import turtle
import random
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


snake_head = create_turtle("square", "darkgreen")
snake_food = create_turtle("circle", "red")
change_position()
running = True
while running:
    screen.update()


