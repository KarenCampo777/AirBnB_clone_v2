#!/usr/bin/python3 
"""
Script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)      
def index():
    return "Hello HBNB!"
def hbnb():       
    return  "HBNB"
def c(text = "value")
    return (c {}.format(text.replace("_", " ")))
def python(text = value 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)     
"""Runs sever port: 5000")
