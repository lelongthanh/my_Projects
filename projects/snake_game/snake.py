
from turtle import Turtle

POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        super().__init__()
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    # create body of snake with different position
    def create_snake(self):
        for body_part_position in POSITION:
            self.add_snake_body(body_part_position)

    def add_snake_body(self, position):
        snake_body = Turtle()
        snake_body.shape('square')
        snake_body.color('white')
        snake_body.penup()
        snake_body.goto(position)
        self.snake.append(snake_body)

    def extend(self):
        self.add_snake_body(self.snake[-1].position())

    # automatically move forward, after the first body part moves
    # the second will replace the first's position, so on and so fort
    def move(self):
        for each_body_part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[each_body_part - 1].xcor()
            new_y = self.snake[each_body_part - 1].ycor()
            self.snake[each_body_part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # if snake turn down, it cant turn up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # if snake turn up, it cant turn down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # if snake turn left, it cant turn right
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # if snake turn right, it cant turn left
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


