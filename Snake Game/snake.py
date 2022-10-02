from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for newposition in POSITIONS:
            self.add_seg(newposition)
    def move(self):
     for segnum in range(len(self.segments) - 1, 0, -1):
        new_x = self.segments[segnum - 1].xcor()
        new_y = self.segments[segnum - 1].ycor()
        self.segments[segnum].goto(new_x, new_y)
     self.head.forward(MOVE_DISTANCE)
     self.head.speed("fastest")
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def add_seg(self,newposition):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(newposition)
        self.segments.append(new_segment)

    def extend(self):
        self.add_seg(self.segments[-1].position())
    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)

    def down(self):
          if self.head.heading() != UP:
             self.head.setheading(DOWN)
    def left(self):
          if self.head.heading() != RIGHT:
             self.head.setheading(LEFT)
    def right(self):
           if self.head.heading() != LEFT:
              self.head.setheading(RIGHT)