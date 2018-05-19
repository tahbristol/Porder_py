from flask import Flask, render_template, url_for
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

@app.route('/users/signup')
def signup():
	form = SignupForm()
	return render_template('users/new.html', form=form)

@app.route('/users/login')
def login():
	form = LoginForm()
	return render_template('users/login.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)