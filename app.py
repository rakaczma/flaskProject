from flask import Flask, render_template, abort, url_for
from datetime import datetime
import random
from model.country import db, find_by_name, find_by_index, find_continent_by_cc, continent_map


app = Flask(__name__)



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/date')
def current_date():
    return f'Response time: {str(datetime.now())}'

counter = 0
@app.route('/counter')
def counter():
    global counter
    counter += 1
    return f'Visit counter: {counter}'

@app.route('/colour')
def select_colour():
    colour_list = ['red', 'blue', 'green']
    return random.choice(colour_list)

@app.route('/hello-world')
def hello_world_html():
    return render_template('welcome.html', message='App Server side są spoko!')

@app.route('/countries')
def random_country():
    country_index = random.randint(0, 246)
    country = db[country_index]

    return render_template('country.html', country=country)

# Path variable: <typ
@app.route('/countries/<name>')
def country_by_name(name: str):
    try:
        found_country = find_by_name(name)
    except ValueError as ex:
        abort(404, ex)
    return render_template('country.html', country=found_country)

@app.route('/countries/index/<int:index>')
def country_by_index(index: int):
    try:
        found_country = find_by_index(index)
        found_country['continent'] = find_continent_by_cc(found_country['cc'])
    except IndexError:
        abort(404, f'Country by index {index} can not be found!')
    return render_template('country_index.html', country=found_country, index=index, continent_map=continent_map)


colors = ['red', 'blue', 'green', 'yellow']

class Square:

    def __init__(self):
        self.color = colors[random.randint(0, len(colors) - 1)]
        self.counter = 0

squares = []

def create_squares():
    global squares
    squares = []
    for i in range(9):
        squares.append(Square())

@app.route('/square')
def create_square():
    create_squares()
    return render_template('square.html', squares=squares)

@app.route('/square/<int:index>')
def increment_counter_square(index: int):
    found_square = squares[index]
    found_square.counter = found_square.counter + 1
    return render_template('square.html', squares=squares)

print(app.url_map)


if __name__ == '__main__':
    app.run()
