import turtle
import random
# import os
import winsound

score_a = 0
score_b = 0
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("gray")
win.setup(width=810, height=600)
win.tracer(0)
# A
wall_a = turtle.Turtle()
wall_a.speed(0)
wall_a.shape("square")
wall_a.color("blue")
wall_a.shapesize(stretch_wid=6, stretch_len=1)
wall_a.penup()
wall_a.goto(-375, 0)
# B
wall_b = turtle.Turtle()
wall_b.speed(0)
wall_b.shape("square")
wall_b.color("blue")
wall_b.shapesize(stretch_wid=6, stretch_len=1)
wall_b.penup()
wall_b.goto(375, 0)
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
x = 1.0
ball.dx = 0.5 if random.choice([True, False]) else -0.5
ball.dy = 0.5 if random.choice([True, False]) else -0.5

# score bar
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# functions
def wall_a_up():
    y = wall_a.ycor()
    y += 25
    wall_a.sety(y)


def wall_a_down():
    y = wall_a.ycor()
    y -= 25
    wall_a.sety(y)


def wall_b_up():
    y = wall_b.ycor()
    y += 25
    wall_b.sety(y)


def wall_b_down():
    y = wall_b.ycor()
    y -= 25
    wall_b.sety(y)


def print_score():
    pen.clear()
    pen.write("player A: {}  player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


def play_bounce():
    # os.system("aplay bounce.wav&")
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


def play_scoring():
    winsound.PlaySound("bad.wav", winsound.SND_ASYNC)


# bindings
win.listen()
win.onkeypress(wall_a_up, "w")
win.onkeypress(wall_a_down, "s")
win.listen()
win.onkeypress(wall_b_up, "Up")
win.onkeypress(wall_b_down, "Down")
# game loop
while True:
    win.update()
    print_score()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 295 or ball.ycor() < -285:
        ball.dy *= -1
        play_bounce()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        play_scoring()
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        play_scoring()

    if 370 < ball.xcor() < 375 and wall_b.ycor() + 60 > ball.ycor() > wall_b.ycor() - 60:
        ball.dx *= -1
        play_bounce()

    if -370 > ball.xcor() > -375 and wall_a.ycor() + 60 > ball.ycor() > wall_a.ycor() - 60:
        ball.dx *= -1
        play_bounce()
