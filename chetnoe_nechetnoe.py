import turtle


class My_turtle(turtle.Turtle):
    def __init__(self, color, pensize, shape, speed):
        super().__init__(shape)
        self.color(color)
        self.pensize(pensize)
        self.shape(shape)
        self.speed(speed)


Leonardo = My_turtle("blue", 2, "turtle", 0)
Raphael = My_turtle("red", 10, "turtle", 0)
Leonardo.forward(100)
Raphael.left(90)
Raphael.forward(100)
turtle.mainloop()
