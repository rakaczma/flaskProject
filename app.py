from flask import Flask, render_template, abort
from datetime import datetime
import random
from model.country import db, find_by_name


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
    except ValueError:
        abort(404)
    return render_template('country.html', country=found_country)

print(app.url_map)


if __name__ == '__main__':
    app.run()
