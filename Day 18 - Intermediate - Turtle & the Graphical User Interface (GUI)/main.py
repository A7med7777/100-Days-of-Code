import colorgram
import random
from turtle import Turtle, Screen


def extract_colors(img_path, num_colors):
    try:
        colors = colorgram.extract(img_path, num_colors)
        return [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
    except FileNotFoundError:
        print("The specified image file was not found.")
        return []


def create_hirst_painting(turtle, colors, dot_count, dot_size, spacing):
    turtle.pen(pendown=False, pensize=dot_size)
    turtle.setpos(-300, -250)

    for _ in range(dot_count):
        turtle.pencolor(random.choice(colors))
        turtle.dot()
        turtle.forward(spacing)

        if turtle.xcor() > 300:
            turtle.setpos(-300, turtle.ycor() + spacing)


def main():
    image_path = "image.jpg"
    num_colors = 30
    dot_count = 143
    dot_size = 12
    spacing = 50
    rgb_colors = extract_colors(image_path, num_colors)

    if not rgb_colors:
        return

    tim = Turtle(visible=False)
    screen = Screen()

    screen.title("Hirst Painting")
    screen.colormode(255)
    tim.speed(0)
    create_hirst_painting(tim, rgb_colors, dot_count, dot_size, spacing)
    screen.exitonclick()


if __name__ == "__main__":
    main()
