#Snake Game By Corey Olley

import turtle
import time
import random

delay = 0.1

# Keeping score
score = 0
high_score = 0

# Window Object

window = turtle.Screen()
window.title("Corey's Snake Game")
window.bgcolor("orange")
window.setup(width=600, height=600)


# Head of snake

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Objective

obj = turtle.Turtle()
obj.speed(0)
obj.shape("square")
obj.color("red")
obj.penup()
obj.goto(0,100)

body = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("SCORE: 0  HIGHSCORE: 0", align="center", font=("Times New Roman", 28, "normal"))


# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

# Key Bindings

window.listen()
window.onkeypress(goup, "Up")
window.onkeypress(godown, "Down")
window.onkeypress(goleft, "Left")
window.onkeypress(goright, "Right")


# looping the game
while True:
    window.update()

    # Check if lost by border
    if head.xcor() > 290 or head.xcor() <-290 or head.ycor() > 290 or head.ycor() <- 290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Delete body when lost
        for new_body in body:
            new_body.goto(1000, 1000)
        # Actual clearing of the body
        body.clear()

        # Clear score
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("SCORE: {}  HIGHSCORE: {}".format(score, high_score), align="center", font=("Times New Roman", 28, "normal"))


    # Check for obj cap
    if head.distance(obj) < 20:
        #obj position change
        x = random.randint(-290, 290)
        y= random.randint(-290, 290)
        obj.goto(x, y)

        # Add body part
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("circle")
        new_body.color("purple")
        new_body.penup()
        body.append(new_body)

        # Fix the delay
        delay -= 0.001

        # Up the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("SCORE: {}  HIGHSCORE: {}".format(score, high_score), align="center", font=("Times New Roman", 28, "normal"))

    # end body moves in reverse order
    for index in range(len(body)-1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)

    # 0 body needs to go to head
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    move()
    # Checks for body collision loss
    for new_body in body:
        if new_body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
           # Delete body when lost
            for new_body in body:
                new_body.goto(1000, 1000)
            # Actual clearing of the body
            body.clear()

            # Clear score
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("SCORE: {}  HIGHSCORE: {}".format(score, high_score), align="center", font=("Times New Roman", 28, "normal"))


    time.sleep(delay)

window.mainloop()