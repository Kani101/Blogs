from flask import render_template, flash, redirect
from app import application
from app.Login import LoginForm

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


@application.route('/login', methods= ['GET', 'POST'])
def user():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}').format(form.username.data, form.remember_me.data)
        return redirect('/index')
    return render_template('login.html', form=form)