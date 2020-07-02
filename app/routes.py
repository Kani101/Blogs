from flask import render_template, flash, redirect, url_for, request
from app import application, db, login
from app.Form import LoginForm, RegistrationForm
from app.models import User, set_pwd_hash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.urls import url_parse

@application.route('/')
@application.route('/index')
@login_required
def index():
    return render_template('index.html')

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@application.route('/welcome')
@login_required
def welcome():
    return render_template('Welcome.html')

@application.route('/login', methods= ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.checkPwd(form.password.data):
            flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
            # blogs = Blog.query.filter_by(user_id= user.id)
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login.html', form=form)

@application.route('/register', methods = ['GET', "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        '''
        Check all details
        - Username, email -> unique
        Register my user
        '''
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if user or email:
            flash("Username/Email already registered")
            return render_template('registration.html', form = form)
        else:
            pwdHash = set_pwd_hash(pwd=form.password.data)
            newUser = User(username=form.username.data, email=form.email.data, contact=form.contact.data, password_hash= pwdHash)
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('login'))
    else:
        return render_template('registration.html', form=form )

@application.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))