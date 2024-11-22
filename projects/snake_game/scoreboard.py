from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=270)
        self.write(f'Score: {self.score}', False, 'center', ('Arial', 15, 'normal'))


    def update_scoreboard(self):
        self.write(f'Score: {self.score}', False, 'center', ('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f'GAME OVER', False, 'center', ('Arial', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()








