from flask import Flask, render_template, url_for, flash, redirect
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd65cee974fbbc376f5d5866c69dade58'

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
		import pdb; pdb.set_trace()
		flash('Account created for {}!'.format(form.name.data), 'success')
		return redirect(url_for('home'))
	
	return render_template('users/new.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('home'))
	return render_template('users/login.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)