import image_utils
from PIL import Image

print("***********")
print("*I*N*S*T*A*")
print("***********")

action = input("Would you like to (f)ilter and image or (q)uit?\n>")
if action != "f" and action != "q":
    print("I don't understand")
while action == "f":
    image = input("What's the full path to your image?\n>")
    image = Image.open(image)
    result = image
    filters = input("""Write a series of filters to apply:
    (p)ixelate
    (k)aleidoscope
    (g)ray-day
    (r)ighty
    Example: kpkr will run keleidoscope, pixelate, kaleidoscope and gray-day in sequence\n>""")
    if "p" in filters:
        temp = result
        result = image_utils.pixelate(temp)
    if "k" in filters:
        temp = result
        result = image_utils.kaleidoscope(temp)
    if "g" in filters:
        temp = result
        result = image_utils.gray_day(temp)
    if "r" in filters:
        temp = result
        result = image_utils.righty(temp)
    result.show()
    action = input("Would you like to (f)ilter an image or (q)uit?\n>")
    if action != "f" and action != "q":
        print("I don't understand")

