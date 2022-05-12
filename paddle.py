# Importing the Turtle class in order to create the Bat class
from turtle import Turtle


class Bat(Turtle):
    """ This class creates objects that act like a ping-pong bat"""
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def move_up(self):
        """ This function moves the bat up"""
        self.forward(20)

    def move_down(self):
        """ This function moves the bat down"""
        self.backward(20)
