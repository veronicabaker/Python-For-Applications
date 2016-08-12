import random
import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()
t.hideturtle()
t2.hideturtle()
wn.tracer(0)
wn.bgcolor("black")
wn.setup(500, 500)

x, y, v, c, d, q = 0, -150, 5, 250, 0, 5
square_side_length = 100
a, b = 200, 100

def draw_square():
    t.setheading(0)
    t.color("pink")
    t.begin_fill()
    for i in range(4):
        t.forward(square_side_length)
        t.right(90)
    t.end_fill()

def draw_rectangle():
    t2.color("green")
    t2.begin_fill()
    for i in range(2):
        t2.forward(a)
        t2.right(90)
        t2.forward(b)
        t2.right(90)
    t2.end_fill()

def point_in_rectangle(x, y, x1, y1, x2,y2):
    return x >= x1 and x <= x2 and y >= y2 and y <= y1

keep_going = not (point_in_rectangle(x + 100, y, d, c, d + 200, c + 100))

def draw_rectangles():
    global c, d, t2, q, keep_going
    keep_going = not (point_in_rectangle(x + 100, y, d, c, d + 200, c -100)) and not (point_in_rectangle(x, y, d, c, d+200, c - 100)) and not (point_in_rectangle(x + 100, y -100, d, c, d +200, c- 100)) and not (point_in_rectangle(x, y, d, c, d +200, c - 100))
    t2.clear()
    t2.up()
    t2.goto(d, c)
    t2.down()
    draw_rectangle()
    if c < -250:
        c = 250
        d = random.randint(-250, 250)
    c -= q
    if keep_going:
        wn.ontimer(draw_rectangles, 75)
    wn.update()


def handle_left():
    global v
    v = -5

def handle_right():
    global v
    v = 5

def next_frame_player():
    global x, v, y, t, c, d, keep_going
    keep_going = not (point_in_rectangle(x + 100, y, d, c, d + 200, c - 100)) and not (point_in_rectangle(x, y, d, c, d + 200, c - 100)) and not (point_in_rectangle(x + 100, y -100, d, c, d +200, c- 100)) and not (point_in_rectangle(x, y, d, c, d +200, c - 100))
    t.clear()
    t.up()
    t.goto(x, y)
    t.down()
    draw_square()
    if x == -250 or x == 150:
        v = -v
    x += v
    if keep_going:
        wn.ontimer(next_frame_player, 50)
    else:
        wn.bgcolor("white")
    wn.update()





wn.onkeypress(handle_left, "Left")
wn.onkeypress(handle_right, "Right")

next_frame_player()
draw_rectangles()



wn.listen()
wn.mainloop()