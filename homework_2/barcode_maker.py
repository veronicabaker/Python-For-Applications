"""
barcode_maker.py
=====
Use the turtle module and your upc module to:

1. Ask the user for a barcode
2. Check if the barcode is valid
3. If the barcode is valid, draw a barcode!
4. If the barcode is not valid:
    * ask for another barcode
    * the text on the prompt should display an error message

You can use the Screen object's textinput method to ask for a barcode:

# Screen object
wn = turtle.Screen()

# ask for a barcode
barcode_number = wn.textinput('barcode', 'Please enter a barcode')

# or... if the previous input was not valid...
barcode_number = wn.textinput('barcode', \
    'NOT A VALID BARCODE\n\nPlease enter another barcode')

See the official documentation:
https://docs.python.org/3.5/library/turtle.html#turtle.textinput
"""
import upc
import turtle

wn = turtle.Screen()
t = turtle.Turtle()
barcode_number = wn.textinput("barcode", "Please enter a barcode")
t.hideturtle()
wn.tracer(0)
wn.setup(500, 500)
x, y = -100, 100
pixels = 3

def draw_rectangle(width):
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.color("black")
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

if upc.valid_barcode(barcode_number) == False:
    barcode_number= wn.textinput('barcode', "Not a valid barcode. Try again")

bar_widths = upc.generate_bar_widths(barcode_number)
draw_rectangle(1 * pixels)
x += pixels +1

draw_rectangle(1 * pixels)

for i in range(32):
    if i == 0 or i == 1 or i == 2:
        continue
    if i % 2 == 1:
        x += int(bar_widths[i]) * pixels

    else:
        draw_rectangle(pixels * int(bar_widths[i]))
        x += int(bar_widths[i]) * pixels

for i in range(32, 54):
    if i % 2 == 1:
        draw_rectangle(pixels * int(bar_widths[i]))
        x += int(bar_widths[i]) * pixels
    else:
        x += int(bar_widths[i]) * pixels

draw_rectangle(1 * pixels)

x += pixels + 1

draw_rectangle(1 * pixels)



wn.mainloop()