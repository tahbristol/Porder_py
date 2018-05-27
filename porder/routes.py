from flask import render_template, url_for, flash, redirect
from porder import app, db, bcrypt
from porder.forms import SignupForm, LoginForm, ItemForm
from porder.models import User, Item
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = SignupForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(name=form.name.data, email=form.email.data, password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		flash('Account created for {}! You are now able to login.'.format(form.name.data), 'success')
		return redirect(url_for('login'))
	return render_template('users/new.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			flash("Welcome Back, {}!".format(user.name), 'success')	
			return redirect(url_for('user_show'))
		else:
			flash('Login Unsuccessful. Please check your email and password', 'danger')
	return render_template('users/login.html', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route('/users/show')
@login_required
def user_show():
	form = ItemForm()
	return render_template('users/show.html', user=current_user, form=form)
	
@app.route('/items/new', methods=['GET','POST'])
@login_required
def item_new():
	form = ItemForm()
	if form.validate_on_submit():
		user = current_user
		new_item = Item(name=form.name.data, quantity=form.quantity.data, vendor=form.vendor.data, price=form.price.data, user_id=user.id)
		db.session.add(new_item)
		db.session.commit()
		return redirect(url_for('user_show'))
	return render_template('items/new.html', form=form)