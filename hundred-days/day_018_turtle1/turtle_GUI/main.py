import turtle as t
import random
import math

t.colormode(255)

timmy = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

def random_walk():
    direction = random.choice([0, 90, 180, 270])
    timmy.setheading(direction)
    timmy.pencolor(random_color())
    timmy.forward(30)

def draw_spirograph(gap_size):
    for _ in range(int(math.ceil(360/gap_size))):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)

# for shape_side in range(3, 11):
#     timmy.color(random_color())
#     draw_shape(shape_side)


timmy.speed('fastest')
draw_spirograph(5)
    
screen = t.Screen()
screen.exitonclick()

