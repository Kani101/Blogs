from flask import render_template
from app import application


@application.route('/')
@application.route('/index')
def index():
    user = {"username": "kanika"}
    blog = [
        {
            "author": {'username': "alpha"},
            "title": 'Blog by alpha'
        },
        {
            "author": {'username': "beta"},
            "title": 'Blog By beta'
        }
    ]
    return render_template('index.html',user = user, data = blog)


@application.route('/login')
def user():
    return render_template('login.html')