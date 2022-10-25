import turtle as t
import math

t.shape("turtle")
t.speed(0)


def draw_house(
    walls_x,
    walls_y,
    walls_width,
    walls_height,
    walls_color,
    door_width,
    door_height,
    door_color
):
    """
    walls_x - левый нижний угол стены
    walls_y - левый нижний угол стены
    walls_width - ширина стен
    walls_height - высота стен
    walls_color - hex цвет заливки стен
    door_width - ширина двери
    door_height - высота двери
    door_color - цвет заливки двери
    """

    door_x = walls_x / 2
    door_y = walls_y

    draw_walls(walls_x, walls_y, walls_width, walls_height, walls_color)
    draw_door(door_x, door_y, door_width, door_height, door_color)
    draw_roof()


def draw_walls(walls_x, walls_y, walls_width, walls_height, walls_color):
    t.penup()
    t.goto(walls_x, walls_y)
    t.pendown()
    t.fillcolor(walls_color)
    t.begin_fill()
    for i in range(2):
        t.fd(walls_width)
        t.left(90)
        t.fd(walls_height)
        t.left(90)
    t.end_fill()    


def draw_door(door_x, door_y, door_width, door_height, door_color):
    t.penup()
    t.goto(door_x, door_y)
    t.pendown()
    t.fillcolor(door_color)
    t.begin_fill()
    for i in range(2):
        t.fd(door_width)
        t.left(90)
        t.fd(door_height)
        t.left(90)
    t.end_fill()   


def draw_roof():
    print("нарисовали крышу")


draw_house(-100, -200, 200, 100, "#ff00ff", 70, 90, "#00ff00")
draw_house(100, 100, 200, 100, "#ff00ff", 70, 90, "#00ff00")

t.done()