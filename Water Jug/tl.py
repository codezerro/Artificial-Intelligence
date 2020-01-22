import waterJugvtwo
import turtle
import time


def jugOneLevel(val):

    if val == 4:
        d = turtle.Turtle()
        d.penup()
        d.goto(-100, 0)
        d.pendown()
        d.begin_fill()
        d.speed(0)
        d.fillcolor("black")
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.end_fill()
        d.hideturtle()

        # dd
        dd = turtle.Turtle()
        dd.penup()
        # box 2
        dd.goto(-50, 50)
        dd.pendown()
        dd.begin_fill()
        dd.speed(0)
        dd.fillcolor("red")
        dd.right(90)
        dd.backward(50)
        dd.right(90)
        dd.forward(50)
        dd.left(90)
        dd.forward(50)
        dd.left(90)
        dd.forward(50)
        dd.end_fill()
        dd.hideturtle()

        # ddd
        ddd = turtle.Turtle()
        ddd.penup()
        # box 2
        ddd.goto(-50, 100)
        ddd.pendown()
        ddd.begin_fill()
        ddd.speed(0)
        ddd.fillcolor("black")
        ddd.right(90)
        ddd.backward(50)
        ddd.right(90)
        ddd.forward(50)
        ddd.left(90)
        ddd.forward(50)
        ddd.left(90)
        ddd.forward(50)
        ddd.end_fill()
        ddd.hideturtle()

        # dddd
        dddd = turtle.Turtle()
        dddd.penup()
        # box 2
        dddd.goto(-50, 150)
        dddd.pendown()
        dddd.begin_fill()
        dddd.speed(0)
        dddd.fillcolor("green")
        dddd.right(90)
        dddd.backward(50)
        dddd.right(90)
        dddd.forward(50)
        dddd.left(90)
        dddd.forward(50)
        dddd.left(90)
        dddd.forward(50)
        dddd.end_fill()
        dddd.hideturtle()

        # clear
        # d.delay()
        # d.clear()
        # dd.clear()
        # ddd.clear()
        # dddd.clear()

    elif val == 3:
        d = turtle.Turtle()
        d.penup()
        d.goto(-100, 0)
        d.pendown()
        d.begin_fill()
        d.speed(0)
        d.fillcolor("black")
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.end_fill()
        d.hideturtle()

        # dd
        dd = turtle.Turtle()
        d.speed(0)
        dd.penup()
        # box 2
        dd.goto(-50, 50)
        dd.pendown()
        dd.begin_fill()
        dd.speed(0)
        dd.fillcolor("red")
        dd.right(90)
        dd.backward(50)
        dd.right(90)
        dd.forward(50)
        dd.left(90)
        dd.forward(50)
        dd.left(90)
        dd.forward(50)
        dd.end_fill()
        dd.hideturtle()

        # ddd
        ddd = turtle.Turtle()
        ddd.penup()
        # box 2
        ddd.goto(-50, 100)
        ddd.pendown()
        ddd.begin_fill()
        ddd.speed(0)
        ddd.fillcolor("black")
        ddd.right(90)
        ddd.backward(50)
        ddd.right(90)
        ddd.forward(50)
        ddd.left(90)
        ddd.forward(50)
        ddd.left(90)
        ddd.forward(50)
        ddd.end_fill()
        ddd.hideturtle()

        # dddd
        dddd = turtle.Turtle()
        dddd.penup()
        # box 2
        dddd.goto(-50, 150)
        dddd.pendown()
        dddd.begin_fill()
        dddd.speed(0)
        # dddd.fillcolor("green")
        dddd.right(90)
        dddd.backward(50)
        dddd.right(90)
        dddd.forward(50)
        dddd.left(90)
        dddd.forward(50)
        dddd.left(90)
        dddd.forward(50)
        dddd.end_fill()

        # clear
        # d.clear()
        # dd.clear()
        # ddd.clear()
        # dddd.clear()
    elif val == 2:
        d = turtle.Turtle()
        d.penup()
        d.goto(-100, 0)
        d.pendown()
        d.begin_fill()
        d.speed(0)
        d.fillcolor("black")
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.end_fill()
        d.hideturtle()

        # dd
        dd = turtle.Turtle()
        dd.penup()
        # box 2
        dd.goto(-50, 50)
        dd.pendown()
        dd.begin_fill()
        dd.speed(0)
        dd.fillcolor("red")
        dd.right(90)
        dd.backward(50)
        dd.right(90)
        dd.forward(50)
        dd.left(90)
        dd.forward(50)
        dd.left(90)
        dd.forward(50)
        dd.end_fill()
        dd.hideturtle()

        # ddd
        ddd = turtle.Turtle()
        ddd.penup()
        # box 2
        ddd.goto(-50, 100)
        ddd.pendown()
        ddd.begin_fill()
        ddd.speed(0)
        ddd.fillcolor("white")
        ddd.right(90)
        ddd.backward(50)
        ddd.right(90)
        ddd.forward(50)
        ddd.left(90)
        ddd.forward(50)
        ddd.left(90)
        ddd.forward(50)
        ddd.end_fill()
        ddd.hideturtle()
        # dddd
        dddd = turtle.Turtle()
        d.speed(0)
        dddd.penup()
        # box 2
        dddd.goto(-50, 150)
        dddd.pendown()
        dddd.begin_fill()
        dddd.speed(0)
        dddd.fillcolor("white")
        dddd.right(90)
        dddd.backward(50)
        dddd.right(90)
        dddd.forward(50)
        dddd.left(90)
        dddd.forward(50)
        dddd.left(90)
        dddd.forward(50)
        dddd.end_fill()
        dddd.hideturtle()

        # clear
        # d.speed(1)
        # dd.speed(1)
        # ddd.speed(1)
        # dddd.speed(1)
        # d.clear()
        # dd.clear()
        # ddd.clear()
        # dddd.clear()

    elif val == 1:
        d = turtle.Turtle()
        d.penup()
        d.goto(-100, 0)
        d.pendown()
        d.begin_fill()
        d.speed(0)
        d.fillcolor("black")
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.forward(50)
        d.left(90)
        d.end_fill()
        d.hideturtle()
        # dd
        dd = turtle.Turtle()
        d.speed(0)
        dd.penup()
        # box 2
        dd.goto(-50, 50)
        dd.pendown()
        dd.begin_fill()
        dd.speed(0)
        # dd.fillcolor("red")
        dd.right(90)
        dd.backward(50)
        dd.right(90)
        dd.forward(50)
        dd.left(90)
        dd.forward(50)
        dd.left(90)
        dd.forward(50)
        dd.end_fill()
        dd.hideturtle()

        # ddd
        ddd = turtle.Turtle()
        ddd.penup()
        # box 2
        ddd.goto(-50, 100)
        ddd.pendown()
        ddd.begin_fill()
        ddd.speed(0)
        # ddd.fillcolor("black")
        ddd.right(90)
        ddd.backward(50)
        ddd.right(90)
        ddd.forward(50)
        ddd.left(90)
        ddd.forward(50)
        ddd.left(90)
        ddd.forward(50)
        ddd.end_fill()
        ddd.hideturtle()

        # dddd
        dddd = turtle.Turtle()
        dddd.penup()
        # box 2
        dddd.goto(-50, 150)
        dddd.pendown()
        dddd.begin_fill()
        dddd.speed(0)
        # dddd.fillcolor("green")
        dddd.right(90)
        dddd.backward(50)
        dddd.right(90)
        dddd.forward(50)
        dddd.left(90)
        dddd.forward(50)
        dddd.left(90)
        dddd.forward(50)
        dddd.end_fill()
        dddd.hideturtle()

        # clear
        # d.clear()
        # dd.clear()
        # ddd.clear()
        # dddd.clear()

    if val == 0:
        # clear
        d.clear()
        dd.clear()
        ddd.clear()
        dddd.clear()


# time.sleep(2)


# for new jug 2########
def jugTwoLevelOn(val):

    # if val == 4:
    d = turtle.Turtle()
    # d.speed(1)
    d.penup()
    d.goto(0, 0)
    d.pendown()
    d.begin_fill()
    d.fillcolor("black")
    d.forward(50)
    d.left(90)
    d.forward(50)
    d.left(90)
    d.forward(50)
    d.left(90)
    d.forward(50)
    d.left(90)
    d.end_fill()


def jugTwoLevelTwo():
    dd = turtle.Turtle()

    dd.penup()
    # box 2
    dd.goto(50, 50)
    dd.pendown()
    dd.begin_fill()
    dd.fillcolor("red")
    dd.right(90)
    dd.backward(50)
    dd.right(90)
    dd.forward(50)
    dd.left(90)
    dd.forward(50)
    dd.left(90)
    dd.forward(50)
    dd.end_fill()
    # d.hideturtle()

# ddd


def jugTwoLevelThree():
    ddd = turtle.Turtle()

    ddd.penup()
    # box 2
    ddd.goto(50, 100)
    ddd.pendown()
    ddd.begin_fill()
    ddd.fillcolor("black")
    # ddd.speed(0)
    ddd.right(90)
    ddd.backward(50)
    ddd.right(90)
    ddd.forward(50)
    ddd.left(90)
    ddd.forward(50)
    ddd.left(90)
    ddd.forward(50)
    ddd.end_fill()


# ddd
# dddd = turtle.Turtle()

# dddd.penup()
# # box 2
# dddd.goto(50, 150)
# dddd.pendown()
# dddd.begin_fill()
# dddd.fillcolor("green")
# dddd.right(90)
# dddd.backward(50)
# dddd.right(90)
# dddd.forward(50)
# dddd.left(90)
# dddd.forward(50)
# dddd.left(90)
# dddd.forward(50)
# dddd.end_fill()


# keith.clear()

# k = turtle.Turtle()


# k.forward(100)
# k.left(45)
# k.forward(100)
# time.sleep(2)

# d.clear()
waterJugvtwo.WaterJug(4, 3, 2)

# for i in range(3):
jugOneLevel(3)
time.sleep(3)
jugOneLevel(0)

jugOneLevel(4)

# jugTwoLevelThree()

turtle.done()
