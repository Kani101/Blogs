from flask import render_template, flash, redirect, url_for
from app import application, db
from app.Form import LoginForm, RegistrationForm
from app.models import User, set_pwd_hash

@application.route('/')
@application.route('/index')
def index(user, blog):
    return render_template('index',user = user, data = blog)

@application.route('/login', methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user and user.checkPwd(form.password.data):
            flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
            # blogs = Blog.query.filter_by(user_id= user.id)
            return render_template('index.html',user = user, data = "")

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
