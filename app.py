#!/usr/bin/env python
#_*_ coding: utf-8 _*_

# --- Flask Hello World --- #


from flask import Flask

app = Flask(__name__)

# Using decorators to link the function to a Url

# static route
@app.route('/')
@app.route('/hello')
def hello_world():
    return "Hello, World...!!"

# dynamic route
@app.route('/test/<search_query>')
def search(search_query):
    return search_query

@app.route('/integer/<int:value>')
def int_type(value):
    print value + 1
    return 'correct'

@app.route('/float/<float:value>')
def float_type(value):
    print value + 1
    return 'correct'

# dynamic route accepts slashes
@app.route('/path/<path:value>')
def path_type(value):
    print value
    return 'correct'

@app.route('/name/<name>')
def index(name):
    if name.lower() == 'chema':
        return 'Hello, {}'.format(name), 200
    else:
        return 'Not Found', 404


if __name__ == '__main__':
    app.run()
