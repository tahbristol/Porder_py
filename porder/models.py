from datetime import datetime
from porder import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=False, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	requests = db.relationship('Item', backref='requestor', lazy=True)
	
	def __repr__(self):
		return "User('{}','{}',{})".format(self.name, self.email, self.image_file)

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), unique=False, nullable=False)
	quantity = db.Column(db.Integer, nullable=False)
	vendor = db.Column(db.String(120), nullable=False)
	price = db.Column(db.Float)
	link = db.Column(db.String(120))
	ordered = db.Column(db.Boolean, default=False)
	date_requested = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return "Item: {}, Qty: {}, Vendor: {}, Price: {}".format(self.name, self.quantity, self.vendor, self.price)

