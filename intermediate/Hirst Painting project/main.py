# The Hits Painting Project

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
color_list = [(252, 250, 246), (252, 244, 247), (246, 253, 249), (243, 247, 251), (46, 104, 159), (144, 179, 190), (225, 171, 125), (184, 148, 160), (125, 81, 90), (127, 73, 53), (37, 48, 65), (111, 174, 125), (214, 80, 58), (70, 6, 23), (40, 131, 105), (176, 102, 149), (238, 186, 135), (84, 98, 181), (64, 52, 45), (118, 41, 55), (218, 172, 179), (235, 177, 154), (180, 189, 210), (85, 153, 111), (79, 56, 52), (70, 65, 54), (23, 77, 101), (167, 204, 185), (166, 201, 205), (53, 59, 77)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dots_count in range(1,number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dots_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)