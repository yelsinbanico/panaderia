from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
SECRET_REGISTRATION_KEY = "777"  # Puedes cambiar esto por la clave que desees.


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
    username = current_user.username  # Obtiene el nombre de usuario del usuario actualmente logueado
    products = Product.query.all()
    return render_template('admin_independent.html', username=username, products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        new_product = Product(name=name, description=description, price=price)
        try:
            db.session.add(new_product)
            db.session.commit()
            flash('Producto agregado correctamente', 'success')
            return redirect(url_for('admin'))  # Cambio aquí: redirige a 'products' en lugar de 'index'
        except:
            flash('Hubo un problema al momento de agregar el producto', 'error')
            return redirect(url_for('admin'))

    return render_template('add_product.html')

@app.route('/update_product/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = request.form['price']
        try:
            db.session.commit()
            flash('Producto actualizado correctamente', 'success')
            return redirect(url_for('admin'))
        except:
            flash('Hubo un problema al momento de actualizar el producto', 'error')
            return render_template('update_product.html', product=product)
    else:
        return render_template('update_product.html', product=product)

@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    try:
        db.session.delete(product)
        db.session.commit()
        flash('Producto eliminado correctamente', 'success')
        return redirect(url_for('admin'))
    except:
        flash('Hubo un problema al momento de eliminar el producto', 'error')
        return redirect(url_for('admin', product_id=product_id))

@app.route('/product/<int:product_id>')
def product(product_id):
    # Obtener el producto de la base de datos usando product_id
    product = Product.query.get_or_404(product_id)
    # Renderizar el producto en una plantilla
    return render_template('product_detail.html', product=product)

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('product.html', products=products)

@app.route('/cart')
def cart():
    return render_template('cart.html')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    unique_key = db.Column(db.String(80))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  # clave única para registrarse


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
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('admin'))  # o a donde quieras dirigir al usuario
        else:
            flash('Usuario o contraseña incorrectos.', 'error')
    return render_template('login_final.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión con éxito.', 'success')
    return redirect(url_for('index'))

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
            flash('Registro exitoso! Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Clave única incorrecta.', 'error')
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)

migrate = Migrate(app, db)