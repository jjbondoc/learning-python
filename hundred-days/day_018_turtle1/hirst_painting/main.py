import turtle as t
import random
# import colorgram

t.colormode(255)
tim = t.Turtle()

# colors = colorgram.extract('image.jpg', 33)
# color_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))

# print(color_list)

colour_list = [(239, 236, 238), (26, 109, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (222, 137, 176), (143, 109, 57), (101, 197, 219), (206, 166, 29), (21, 58, 132), (212, 75, 91), (238, 89, 49), (141, 208, 227), (119, 192, 141),
               (6, 160, 87), (4, 186, 179), (106, 108, 198), (136, 29, 72), (98, 51, 37), (25, 153, 211), (228, 168, 188), (153, 213, 195), (173, 186, 221), (234, 174, 162), (30, 91, 95), (87, 47, 34), (34, 46, 84), (239, 203, 10), (33, 85, 84), (95, 27, 52)]

def random_color():
    return random.choice(colour_list)

def paint(x_dots, y_dots):
    for y in range(y_dots):
        for x in range(x_dots):
            tim.dot(20, random_color())
            tim.forward(50)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(50 * x_dots)
        tim.setheading(0)

tim.speed(0)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
paint(7, 6)

screen = t.Screen()
screen.exitonclick()