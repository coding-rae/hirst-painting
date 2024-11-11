import colorgram
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed(("fastest"))
#rgb_colors = []

#colors = colorgram.extract('image.jpg.png', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

color_shades = [(189, 46, 74), (231, 118, 144), (115, 90, 46), (110, 107, 189), (216, 60, 77), (114, 186, 136), (122, 176, 212),
 (52, 178, 110), (204, 16, 40), (115, 171, 36), (223, 57, 47), (31, 58, 117), (154, 223, 195),(182, 168, 223),
 (23, 142, 107), (29, 164, 172), (85, 35, 37), (39, 45, 84), (229, 169, 182), (232, 174, 161), (81, 39, 38),
 (151, 206, 223), (92, 43, 42)]

timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)

num_of_dots = 101

for dot_count in range(1, num_of_dots):
    timmy.dot(20, random.choice(color_shades))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)





screen = t.Screen()
screen.exitonclick()


#10 x 10 rows of spots
#draw dots
#move turtle to create pattern
#dot 20 in size - spaces by 50 paces