import turtle
import time

box_size = 200
caught = False
score = 0


def up():
    mouse.forward(10)
    checkbound()


def left():
    mouse.left(45)


def right():
    mouse.right(45)


def back():
    mouse.backward(10)
    checkbound()


def quit_turtles():
    window.bye()


def check_bound():
    global box_size
    if mouse.xcor() > boxsize:
        mouse.goto(boxsize, mouse.ycor())
    if mouse.xcor() < -boxsize:
        mouse.goto(-boxsize, mouse.ycor())
    if mouse.ycor() > boxsize:
        mouse.goto(mouse.xcor(), boxsize)
    if mouse.ycor() < -boxsize:
        mouse.goto(mouse.xcor(), -boxsize)


window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle()
mouse.penup()
mouse.penup()
mouse.goto(100, 100)

window.onkeypress(up, 'Up')
window.onkeypress(left, 'Left')
window.onkeypress(right, 'Right')
window.onkeypress(back, 'Down')
window.onkeypress(quit_turtles, 'Escape')

difficulty = window.numinput('Difficulty', 'Enter a difficulty from easy(1), for hard(5)', minval=1, maxval=5)

window.listen()
while not caught:
    cat.setheading(cat.towards(mouse))
    cat.forward(8 + difficulty)
    score += 1
    if cat.distance(mouse) < 5:
        caught = True
    time.sleep(0.2 - (0.01 * difficulty))
window.textinput('GAME OVER', "Well done. Your score: " + str(score * difficulty))
window.bye()
