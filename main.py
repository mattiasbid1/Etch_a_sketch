from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def tilt_left():
    tim.left(15)


def tilt_right():
    tim.right(15)


def clear_scrn():
    tim.clear()
    tim.penup()
    setup()
    tim.pendown()


def setup():
    tim.home()
    screen.bgcolor("black")
    tim.color("cyan")
    tim.pencolor("brown")


screen.listen()
setup()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=tilt_left)
screen.onkey(key="d", fun=tilt_right)
screen.onkey(key="c", fun=clear_scrn)
screen.exitonclick()
