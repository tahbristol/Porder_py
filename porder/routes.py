from flask import render_template, url_for, flash, redirect, jsonify, request
from porder import app, db, bcrypt
from porder.forms import SignupForm, LoginForm, ItemForm
from porder.models import User, Item, UserSchema, ItemSchema
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
		return redirect(url_for('user_show'))
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
	user = current_user
	if form.validate_on_submit():
		new_item = Item(name=form.name.data, quantity=form.quantity.data, vendor=form.vendor.data, price=form.price.data, user_id=user.id)
		db.session.add(new_item)
		db.session.commit()
		return redirect(url_for('user_show'))
	elif request.get_json():
		data = request.get_json()
		new_item = Item(name=data['name'], quantity=data['quantity'], vendor=data['vendor'], price=data['price'], user_id=data['user_id'])
		db.session.add(new_item)
		db.session.commit()
		item_schema = ItemSchema()
		result = item_schema.dump(new_item)
		return jsonify(result.data)
	return render_template('items/new.html', form=form)
	
@app.route('/items/', methods=['GET'])
@login_required
def item_index():
	item_schema = ItemSchema()
	item_schema = ItemSchema(many=True)
	all_items = Item.query.all()
	result = item_schema.dump(all_items)
	return jsonify(result.data)

@app.route('/users/<int:id>/items', methods=['GET'])
@login_required
def user_items(id):
	item_schema = ItemSchema()
	item_schema = ItemSchema(many=True)
	user_items = Item.query.filter(Item.user_id == id)
	result = item_schema.dump(user_items)
	return jsonify(result.data)
