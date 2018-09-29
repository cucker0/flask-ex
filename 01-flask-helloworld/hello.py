#!/usr/bing/env python
#-*- coding: utf-8 -*-

from flask import Flask, url_for, request
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World!!'

# @app.route('/user/<username>')
# def show_user_profile(username):
#     return "User %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('static', filename='style.css'))


@app.route('/method', methods=['GET', 'POST'])
def save():
    if request.method == 'POST':
        return save_post()
    else:
        return save_get()

def save_post():
    return "request method:post"

def save_get():
    return "request method:get"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)