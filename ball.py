# Importing the Turtle Class in order to create the Ball class
from turtle import Turtle


class Ball(Turtle):
    """ This class creates functions that act like a ping-pong ball"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x = self.xcor()
        self.y = self.ycor()
        self.y_change = 10
        self.x_change = 10

    def move(self):
        """ This function moves the ball"""
        self.x += self.x_change
        self.y += self.y_change
        self.goto(self.x, self.y)

    def change_y(self):
        """ This function changes the balls y direction"""
        self.y_change *= -1

    def change_x(self):
        """ This function changes the balls x direction"""
        self.x_change *= -1.1

    def restart(self):
        """ This function returns the ball back to it's starting position"""
        self.x = 0
        self.y = 0
