from flask import Blueprint
from app import db
from flask import render_template, flash, redirect, url_for, request
from app.products.forms import ProductForm
from app.models import Products
from flask_login import login_required


product_blueprint = Blueprint('product_blueprint', __name__)

@product_blueprint.route('/products')
@login_required
def products():
    products = Products.query.all()
    if len(products) > 0:
        return render_template('products.html',title = 'Products', products=products)
    else:
        msg = "No Product found"
        return render_template('products.html',title='Products',msg=msg)

@product_blueprint.route('/add_product',methods=['GET','POST'])
@login_required
def add_product():
    form = ProductForm()
    if request.method == 'POST':
        product = Products(product_name=form.product.data, quantity= form.quantity.data)
        db.session.add(product)
        db.session.commit()
        flash("Your Product has been inserted")
        return redirect(url_for('products.products'))
    return render_template('add_product.html', form=form, title='Add Product')


@product_blueprint.route('/edit_product/<string:product_id>', methods=['GET','POST'])
@login_required
def edit_product(product_id):
    form = ProductForm(request.form)
    my_product = Products.query.filter_by(product_id=product_id).first()
    if my_product and request.method=="POST":
        my_product.product_name = form.product.data
        my_product.quantity = form.quantity.data
        db.session.commit()
        flash("Record Updated Successfully","success")
        return redirect(url_for('products.products'))
    return render_template('edit_product.html',form=form ,product_id=my_product.product_id, title="Edit Product")


@product_blueprint.route('/delete_product/<int:product_id>',methods=['POST'])
@login_required
def delete_product(product_id):
    product = Products.query.filter_by(product_id=product_id).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        flash("Record has been deleted successfully","success")
        return redirect(url_for('products.products'))

