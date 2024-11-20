from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = True
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter the turtle's color: ")
print(user_bet)
turtle_color = ["red", "blue", "green", "yellow", "orange", "black", "pink"]
y_position = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []
# create 7 turtle objects with different attributes
for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:

    for turtle in all_turtles:
        # The race will end when 1 turtle object touch the edge of window's height
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor() #color() return pencolor and fillcolor

            if winning_color == user_bet:
                print(f"You've won'! The winner is {winning_color} turtle")
            else:
                print(f"You've lost! The winner is {winning_color} turtle")
        # turtles will run randomly distances
        race_distances = random.randint(1, 10)
        turtle.forward(race_distances)

screen.exitonclick()