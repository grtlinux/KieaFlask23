#!/bin/python3 -v
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# app.py
#
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello():
    '''Return a friendly HTTP greeting.'''
    return 'Welcome to the Flask App! 강석'

@app.route('/create')
def create():
    '''Create a new user'''
    return 'Create a new user'

# @app.route('/read/<id>')  # id's type str
@app.route('/read/<int:id>')  # id's type int
def read(id):
    '''Read a user with the given id'''
    print('Read user with id: ' + str(id))
    return 'Read user with id: ' + str(id)

@app.route('/rand')
def rand():
    '''Generate a random number between 1 and 10 '''
    random_number = random.randint(1, 1000)
    return 'Random value: ' + str(random_number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
