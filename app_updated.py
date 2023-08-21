
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

SECRET_REGISTRATION_KEY = "777"  # You can change this to whatever key you'd like.

app = Flask(__name__)
app.secret_key = '123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///panaderia.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/admin')
@login_required
def admin():
    return render_template('admin_independent.html')

# ... (keeping the rest of your existing code the same)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    unique_key = db.Column(db.String(80))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Successfully logged in', 'success')
            return redirect(url_for('admin'))
        else:
            flash('Username or password is incorrect.', 'error')
    return render_template('login_final.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        unique_key = request.form.get('unique_key')
        
        if unique_key == SECRET_REGISTRATION_KEY:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Successfully registered! You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Incorrect unique key.', 'error')
    return render_template('register.html')

# ... (keeping the rest of your existing code the same)

if __name__ == '__main__':
    app.run(debug=True)

migrate = Migrate(app, db)
