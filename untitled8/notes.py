"""
import matplotlib.pyplot as plt
import random
freq_dice_rolls = {}
for i in range(1000):
    roll = random.randint(1,3) + random.randint(1,3)
    freq_dice_rolls[roll] = freq_dice_rolls.get(roll, 0) + 1

plt.bar(freq_dice_rolls.keys(), freq_dice_rolls.values() )
plt.title("Dice Rolls")
plt.xlabel("Roll")
plt.ylabel("Frequency")
plt.show()
"""

"""
open a file for reading and writning
there's a file object
it supppors reading writing and appaend ing
open(file_name, mode)
f = open('survey-results.csv', 'r')

mode-
r- read
w - write (will overwrite or create)
a - append

read-
realines - gives back a list
readline - reads one line at a time and keeps track of whihc line
read - gives a string of the entire file

write-
write
"""
"""
f = open('survey-results(1).csv', 'r')
#file objects are iterable objects
#loop over them

lines = f.readlines()
stripped_lines = [line.strip() for line in lines]
print(stripped_lines)

name = 0
pace = 1
d = {}

for line in f:
    #print(line[0:line.index(',')]
    line_parts = line.split(',')
    print(line_parts[name], line_parts[pace])
    k = line_parts[pace]
    d[k] = 1 if k not in d else d[k] + 1
#print(f.read())

f.close()
"""

"""
#how to write a file

f = open('foo.txt', 'w')
f.write("stuff")
f.close()
"""
"""
with open('foo.txt', 'w') as f:
    f.write('stuff')
    #no need to call close
"""
"""
import json


d = json.loads("{"foo" : "Bar"}")
"""

"""
../? go up one directory
../../? go up two directoryies
/ ?
./? current
/ ? root directory
~/Desktop.whatever.txt #starts at home then desktop

pycharm will look in current directory for the file
"""

"""
f = open("/tmp/foo.txt", "r")
for line in f:
    print(line.strip())
f.close
"""
"""
with some_expression_that_returns_value as variable_name
    do stuff

with open("/tmp/foo.txt", "r") as f:
    f = open(x, "r")
    for line in f:
        print(line.strip())
"""

"""
cant extract data without knowing delimiter/format
html
xml
json
csv (any delimiter)

CSV?
-split by delimiter

Fixed width?
-use slicing

XML?
use a parser

HTML?
use a parser
"""

"""
csv module

import csv
with open("...) as f:
    csvfile = csv.reader(f)
    for row in csvfile:
        print(row) #all elements in row in a list

    csvfile = csv.DictReader(f) #dictionary

"""

"""
fixed width
truncate extra characters when writing
"""

"""
html
beautiful soup 4 html parser
-css selectors and tag attributes

from bs4 import BeautifulSoup

dom = BeautifulSoup("""
<html>
<body>
<h1>foo</h1>
<h1 class =(".heady-stuff")>bar</h1>
<body>
</html>
""", "lxml)

h1 = dom.select(".heady-stuff")
headers = dom.select("h1")
print(headers)
for h in headers:
    print(h.string)
"""

"""
import json
#dumps - creates a string form a python dict... as json format
#loads - reads a string into a python dict (assuming string is json)
s = '{"first": "v", "last":"b"}'
d = json.loads(s)
print(d)

"""

"""
data can be
local on your file system
remote on some other server
-download it and save for later processing
-immediately process the data

import requests
res = requests.get("http://cs.nyu.edu/home/index.html")
print(res.status_code) #http response status code (you want a 200)
print(res.text) #the contents/ body of the response
"""

"""
pillow library
from PIL import Image
img = Image.new('RBG', (255, 255), "black") #create new black image
pixels = image.load()
print(pixels

for i in range(img.size[0]: # for every pixel
    for j in range(img.size[1]):
    pixels[i, j] = (i, j, 100) #set colour


img = Image.new('RGB', (400, 400))
img.show()
img.save()

#load - PixelAcess object
#reference individual pixels by a tuple of x, y coords


img = image.open('/specify path.jpg')
pixels = Image.load()
print(img.size)

for x in range(img.size[0])
    for y in range(img.size[1])
    print(pixels[x, y])


#combine two images
#load both images
#create a new image
#... go over every pixel in new image and set it to
#... weighted average of old images

def mix_img(img1, img2):
    img = Image.new('RGB', img1.size)
    pix, pix1, pix2 = img.load(), img1.load(), img2.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
        #access to new pixel
        c1 = pix1[x, y]
        c2 = pix2[x, y]
        pix[x, y] = (c1[0] + c2[0] // 2, c1[1] + c2[1] // 2, c1[2] + c2[2] // 2)
    return img

if __name__ == '__main__':
    new_img = mix_img(Image.open(specify path), Image.open(specify path))
    new_img.show()


#for weighted average: int(c1[0] * r1 + c2[0] * r2)
#where r1 is the ratio
#r2 is 1 - r1

#list comprehension



CHROMAKEY

def chromakey(source_image, dest_image, thresh=200)
    pix_source, pix_dest = source.load(), dest.load()
    for x in range(source_image.size[0])
        for y in range(dest.size[1]):
        #extract the feature from teh background
        #overlay feature on top of destination
        c = pix_source[x, y]
        if c[0] < thresh and c[1] < thresh and c[2] < thresh:
        pix_dest[x, y] = c
    return dest

"""
from PIL import Image

def flip_upsidedown(img):
    new_image = Image.new('RGB', img.size)
    pix, pix2 = img.load(), new_image.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            new_x, new_y = x, img.size[0] - 1 - y
            pix[x, y] = pix[new_x, new_y]

    return new_image


def draw_rectangle()








