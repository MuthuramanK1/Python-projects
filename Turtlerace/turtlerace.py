from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make a bet", prompt="which turtle will win the race?"
                            " enter the color")
colors = ["red", "green", "orange", "yellow", "blue", "purple"]
turt = []
turtle_position = [-70, -40, -10, 20, 50, 80]

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=turtle_position[index])
    turt.append(new_turtle)
if user_bet:
    is_game_on = True
while is_game_on:
    win = []
    for each_turtle in turt:
        if each_turtle.xcor() > 230:
            win.append(each_turtle)
            is_game_on = False
            winning_color = win[0].pencolor()
            if winning_color == user_bet:
                print(f"You've won, Winning turtle is {winning_color}")
                turt.clear()
            else:
                print(f"You've lose, winning color is {winning_color}")
                turt.clear()
        rand_distance = random.randint(0, 10)
        each_turtle.fd(rand_distance)
screen.exitonclick()
