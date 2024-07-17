from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    vehicle_number = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def _repr_(self):
        return f'<User {self.username}>'

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(80), db.ForeignKey('user.vehicle_number'), unique=True, nullable=False)
    wallet_amt = db.Column(db.Float, nullable=False, default=500.0)  # Default wallet amount

    def _repr_(self):
        return f'<Wallet {self.vehicle_number} - {self.wallet_amt}>'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        vehicle_number = request.form['vehicle_number']
        email = request.form['email']
        password = request.form['password']
        existing_user = User.query.filter((User.username == username) | (User.vehicle_number == vehicle_number) | (User.email == email)).first()
        if existing_user:
            flash('You are already registered.')
            return redirect('/signup')
        new_user = User(username=username, vehicle_number=vehicle_number, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        new_wallet = Wallet(vehicle_number=vehicle_number)
        db.session.add(new_wallet)
        db.session.commit()
        return redirect('/vehicle_selection')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        vehicle_number = request.form['vehicle_number']
        password = request.form['password']
        user = User.query.filter_by(vehicle_number=vehicle_number, password=password).first()
        if user:
            session['username'] = user.username
            session['vehicle_number'] = user.vehicle_number
            return redirect('/vehicle_selection')
        else:
            flash('Invalid credentials, please try again.')
            return redirect('/login')
    return render_template('login.html')

@app.route('/vehicle_selection', methods=['GET', 'POST'])
def vehicle_selection():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        vehicle = request.form['vehicle']
        toll_charge = request.form['toll_charge']
        session['vehicle'] = vehicle
        session['toll_charge'] = toll_charge
        return redirect(url_for('location'))
    return render_template('vehicle_selection.html')

@app.route('/auto_page')
def auto_page():
    return render_template('divert_meerut.html')

@app.route('/car_page')
def car_page():
    return render_template('mathura-delhi.html')

@app.route('/bus_page')
def bus_page():
    return render_template('divert_muzaffarnagar.html')

@app.route('/truck_page')
def truck_page():
    return render_template('divert_sonipat.html')

@app.route('/location')
def location():
    # Implement your logic here
    return "Location Page - Implement your logic here"

@app.route('/payment')
def payment():
    return render_template('payment.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
