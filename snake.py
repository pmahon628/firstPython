import turtle
import time

delay = 0.1

# set screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("Black")
wn.setup(width=600, height=600)
wn.tracer(0) 

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# functions

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_right():
    head.direction = "right"

def go_left():
    head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+ 20)

    if head.direction == "down":
        y = head.ycor(
            head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x -20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    )

# keyboard bindings

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# main game loop
while True:
    wn.update()

    move()

    time.sleep(delay)

# keeps window open
wn.mainloop()