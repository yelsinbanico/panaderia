from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from .. import db
from .models import Product

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates/admin')

@admin.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_product = Product(name=name, description=description)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('add_product.html')

@admin.route('/edit_product/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    product = Product.query.get(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('edit_product.html', product=product)
