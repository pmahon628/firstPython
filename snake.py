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

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "right":
        head.direction = "left"

def go_left():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# keyboard bindings

wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# main game loop
while True:
    wn.update()

    # check for collision with  the border
    if  head.xcor()>290 or head.xcor()<-290 or head.ycor()>290  or  head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000,  1000)

            # clear segments
            segments.clear()


    # check for food collision
    if head.distance(food) <20:
        # move to random spot
        x = random.radiant(-290, 290)
        y = random.radiant(-290, 290)
        food.goto(x,y)

        # add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(grey)
        new_segment.penup()
        segments.append(new_segment)
    
    # move end segments first in reverse order
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

        # move segment  0 to where the  head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)


    move()

    # check for head collisions with body segments
    for segment in segments:
        if  segment.distance(head)  <  20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # hide  the segments
            for segment  in segments:
                segment.goto(1000, 1000)

            # clear the  segments  
            segments.clear()




    time.sleep(delay)

# keeps window open
wn.mainloop()
