from flask import Blueprint
from app import db, bcrypt
from flask import render_template, flash, redirect, url_for, request
from app.main.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import current_user, login_user, login_required, logout_user

main = Blueprint('main',__name__)


@main.route('/')
def home():
    return render_template('home.html', title='Home')

@main.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created. Please Login ','success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


@main.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash('User logged in!','success')
            return redirect(url_for('main.home'))
        else:
            flash('Unsuccessful Login','danger')
            return redirect(url_for('main.login'))
    return render_template('login.html', title='Login',form=form)


@main.route("/logout",methods=["GET"])
@login_required
def logout():
    logout_user()
    flash('User logged Out!', 'success')
    return redirect(url_for('main.home'))
