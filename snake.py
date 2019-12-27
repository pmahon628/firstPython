import turtle

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

# main game loop
while True:
    wn.update()

# keeps window open
wn.mainloop()
