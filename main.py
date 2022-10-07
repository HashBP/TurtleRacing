import random
from tkinter import Y
from turtle import Turtle, Screen
import turtle

screen = Screen()
screen.setup(width=500, height=400)

is_game_on = False
user_bet = screen.textinput(
    "Make your bet.", "Which turtle wins the race? Tell a color.").lower()

color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -100
for t in range(6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color[t])
    tim.shape("turtle")
    tim.goto(x=-225, y=y)
    y += 30
    all_turtles.append(tim)

if user_bet:
    is_game_on = True
while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_game_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                screen.title(f"🥳🥳🥳Hurray!! Your {winning_color} turtle won.")
            else:
                screen.title(f"😪Your {user_bet} turtle Lost😒. {winning_color} turtle is the winner👑.")
        steps = random.randint(0, 11)
        turtle.forward(steps)


screen.listen()
screen.exitonclick()
