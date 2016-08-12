from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import requests

app = Flask(__name__)

#homepage should ask the user if they want to submit an image(and add a filter)
#or view previous images

#if they provide the url of an image
#use requests to retrieve it

#create an image object
#and use filters to filter it

#then... use flask to display the image on "/dislay"

#we should store processed image objects using a data structure ????
#create a decorator to do this
#it will be used every time a function is called from the photo class

if __name__ == '__main__':
    app.run(debug=True)

