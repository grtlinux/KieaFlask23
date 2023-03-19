from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to the Flask App!'

@app.route('/create')
def create():
    return 'Create a new user'

@app.route('/read/<id>')
def read(id):
    print('Read user with id: ' + id)
    return 'Read user with id: ' + id

@app.route('/random')
def rand():
    '''Generate a random number between 1 and 10 '''
    random_number = random.randint(1, 1000)
    return 'Random value: ' + str(random_number)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
