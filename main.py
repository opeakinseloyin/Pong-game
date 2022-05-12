# Importing the time module, Ball, Bat, Score and Screen classes from their respective files
import time
from ball import Ball
from paddle import Bat
from score import Score
from turtle import Screen

# Creating a screen object from the Screen class and setting it's width and height to 800
# as well as using the tracer function to prevent lags
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ope's Pong game")
screen.tracer(0)

# Creating the bat and score objects for the right player from the Bat and Score class
r_bat = Bat()
r_score = Score()
# Creating the bat and score objects for the right player from the Bat and Score class
l_bat = Bat()
l_score = Score()
# Creating a ball object from the Ball class
ball = Ball()

# Defining a game_on variable that allows the game to continuously play until certain conditions are made
game_on = True

# Moving the right player's bat and score object to the right side of the screen
r_bat.goto(380, 0)
r_score.goto(200, 250)
# Moving the left player's bat and score object to the left side of the screen
l_bat.goto(-380, 0)
l_score.goto(-200, 250)

# Using the listen function to allow for the game to take key inputs
screen.listen()
# Defining the key inputs and their functions for the right player
screen.onkey(r_bat.move_up, "Up")
screen.onkey(r_bat.move_down, "Down")
# Defining the key inputs and their functions for the left player
screen.onkey(l_bat.move_up, "w")
screen.onkey(l_bat.move_down, "s")

# Using the while loop to loop around the game program to allow the game to play continuously
while game_on:
    # Works in hand with the tracer function to prevent lags
    screen.update()
    # Using the time.sleep function to slow down the speed of the program so as to make the game playable
    time.sleep(0.1)
    # Using the ball.move function to cause the ball to move continuously
    ball.move()
    # Using the r_score.writing function to write the score at the top of the screen for the right player
    r_score.writing()
    # Using the l_score.writing function to write the score at the top of the screen for the left player
    l_score.writing()

    # Using the if and logic statements to create the wall boundary that the ball bounces of from
    # while changing its y direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y()

    # Using the if and logic statements to make the ball bounce back when hit by the right bat
    if ball.xcor() > 365 and ball.distance(r_bat) < 50:
        ball.change_x()
    # Using the if and logic statements to make the ball bounce back when hit by the left bat
    if ball.xcor() < -365 and ball.distance(l_bat) < 50:
        ball.change_x()

    # Using the if and logic statements to create the goal scenario for the left player
    # and restarting the game again to bounce the ball the other way
    if ball.xcor() > 400:
        l_score.add_score()
        ball.restart()
        ball.change_x()
    # Using the if and logic statements to create the goal scenario for the right player
    # and restarting the game again to bounce the ball the other way
    if ball.xcor() < -400:
        r_score.add_score()
        ball.restart()
        ball.change_x()

# This function allows the screen to stay on until the game has come to an end
screen.exitonclick()
