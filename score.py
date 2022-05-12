# Importing the Turtle class in order to create the Score class
from turtle import Turtle


class Score(Turtle):
    """ This class creates objects that write the score of the user and keeps track of the user's score"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0

    def writing(self):
        """ This function writes the user's score on the screen"""
        self.clear()
        self.write(arg=f"{self.score}", font=("Arial", 30, "normal"))

    def add_score(self):
        """ This function increases the user's score by 1"""
        self.score += 1
