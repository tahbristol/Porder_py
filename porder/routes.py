from flask import render_template, url_for, flash, redirect
from porder import app
from porder.forms import SignupForm, LoginForm
from porder.models import User, Item

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		flash('Account created for {}!'.format(form.name.data), 'success')
		return redirect(url_for('home'))
	return render_template('users/new.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('home'))
	return render_template('users/login.html', form=form)

