# pygame snake youtube tutorial

import turtle
import random
import time
import winsound

delay = 0.1

# Score
score = 0
high_score = 0

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

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, -235)
pen.write("Score: 0 Highscore: 0", align="center", font=("Courier", 24, "normal"))

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

    if head.xcor() > 235 or head.xcor() < -235 or head.ycor() > 235 or head.ycor() < -235:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide segments
        for segment in segments:
            segment.goto(1000, 1000)
            
        segments.clear()

        # reset score
        score = 0
        # change the score
        pen.clear()
        pen.write("Score: {} Highscore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        # reset delay 
        delay = 0.1

# check for a collison with food
    if head.distance(food) < 20:     
        winsound.PlaySound("C:\...\aud_chomp.wav", winsound.SND_ASYNC)
        # move food to another random spot
        x = random.randint(-235, 235)
        y = random.randint(-235, 235)  
        food.goto(x,y)
        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # increase the score
        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} Highscore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        #shorten the delay
        delay -= 0.002

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

            # reset the score
            score = 0

            # change the score
            pen.clear()
            pen.write("Score: {} Highscore: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # reset the delay
            delay = 0.1
    time.sleep(delay)

wn.mainloop()
