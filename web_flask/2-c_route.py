#!/usr/bin/python3  
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask (__name__)

@app.route('/', strict_slashes=False)  
def index():
    return "Hello HBNB!"
"""displays "Hello HBNB!" in / """
def hbnb():
    return "HBNB"
""" displays "HBNB" in /hbnb"""
def c(text = "value"):
    return (c {}.format(text.replace("_", " ")))
if __name__ == "__main__":
app.run(debug=True, host='0.0.0.0', port=5000)
""" display C  followed by the value of the text variable (replace underscore _ symbols with a space )
