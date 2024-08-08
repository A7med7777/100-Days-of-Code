from turtle import Turtle

init_pos = ((0, 0), (-20, 0), (-40, 0))


class Snake:
    def __init__(self):
        self.body = []
        self.create_snack()
        self.head = self.body[0]

    def create_snack(self):
        for position in init_pos:
            tim = Turtle(shape="square")
            tim.pen(pendown=False, pencolor="white", fillcolor="white")
            tim.setpos(position)
            self.body.append(tim)

    def grow(self):
        tim = Turtle(shape="square")
        tim.pen(pendown=False, pencolor="white", fillcolor="white")
        tim.setpos(self.body[-1].pos())
        self.body.append(tim)

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            self.body[segment].goto(self.body[segment-1].pos())

        self.head.forward(20)

    def face_north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def face_west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def face_south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def face_east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
