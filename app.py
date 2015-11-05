#!/usr/bin/env python
#_*_ coding: utf-8 _*_

# --- Flask Hello World --- #


from flask import Flask

app = Flask(__name__)

# Using decorators to link the function to a Url

@app.route('/')
@app.route('/hello')
def hello_world():
    return "Hello, World...!!"


if __name__ == '__main__':
    app.run()
