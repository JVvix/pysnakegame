# pygame snake youtube tutorial

import turtle
import random
import time

delay = 0.1

# screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=500, height=500)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
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

# function
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up": 
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_quit():
    turtle.bye()

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
wn.onkey(go_quit, "q")

# main game loop
while True:
    wn.update()
    
    # check for a collison

    if head.xcor() > 230 or head.xcor() < -230 or head.ycor() > 230 or head.ycor() < -230:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide segments
        for segment in segments:
            segment.goto(1000, 1000)
            
        segments.clear()

# check for a collison with food
    if head.distance(food) < 20:     
        # move food to another random spot
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)  
        food.goto(x,y)
        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

    # move the end segements in order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

# check for head collison with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop" 

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear segments
            segments.clear()

    time.sleep(delay)

wn.mainloop()
