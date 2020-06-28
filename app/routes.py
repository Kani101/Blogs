from flask import render_template, flash, redirect, url_for
from app import application, db, login
from app.Login import LoginForm, RegistrationForm
from app.models import User, Blog
from flask_login import login_required, current_user, login_user, logout_user

@application.route('/')
@application.route('/index')
@login_required
def index(user, blog):
    return render_template('index',user = user, data = blog)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@application.route('/login', methods= ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user and user.checkPwd(form.password.data):
            flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
            blogs = Blog.query.filter_by(user_id= user.id)
            login_user(user, remember=form.remember_me.data)
            return render_template('index.html',user = user, data = blogs)

    return render_template('login.html', form=form)

@application.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(User.query.all())
        try:
            user = User(username=form.username.data, email=form.email.data, contact=form.contact.data)
            user.set_pwd_hash(form.password.data)
            db.session.add(user)
            print("User added to the session")
            db.session.commit()
            print("committed")
            flash('Sign Up successful for userId {}'.format(
                form.username))
            return redirect(url_for('login'))
        except Exception as e:
            flash(' username {} or email {} already exists'.format(
                form.username.data, form.email.data))
            return redirect(url_for('register'))
    return render_template('registration.html', form = form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))