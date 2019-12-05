from flask import Blueprint
from app import db
from flask import render_template, flash, redirect, url_for, request
from app.product_movements.forms import MovementForm
from app.models import Movements
from flask_login import login_required

movement_blueprint = Blueprint('movement_blueprint',__name__)


@movement_blueprint.route('/product_movements', methods=['POST','GET'])
@login_required
def product_movements():
    movements = Movements.query.all()
    if len(movements)>0:
        return render_template('product_movements.html', title='Product Movements', movements=movements)
    else:
        msg="No Product Movements found"
        return render_template('product_movements.html', msg=msg, tilte='Product Movements')


@movement_blueprint.route('/add_product_movements', methods=['GET','POST'])
@login_required
def add_movements():
    form = MovementForm()
    if request.method == "POST":
        movement = Movements(product_name=form.product.data, from_warehouse=form.from_location.data,
                             to_warehouse = form.to_location.data, quantity =form.quantity.data)
        db.session.add(movement)
        db.session.commit()
        flash("Your Product Movement has been inserted","success")
        return redirect(url_for('product_movements.product_movements'))
    return render_template('add_movements.html', form=form, title='Add Product Movements')


@movement_blueprint.route('/edit_product_movement/<int:transaction_id>', methods=['GET','POST'])
@login_required
def edit_movement(transaction_id):
    form = MovementForm(request.form)
    my_movement = Movements.query.filter_by(transaction_id=transaction_id).first()
    if my_movement and request.method == 'POST':
        my_movement.product_name = form.product.data
        my_movement.from_warehouse = form.from_location.data
        my_movement.to_warehouse = form.to_location.data
        my_movement.quantity = form.quantity.data
        db.session.commit()
        flash("Record Updated Successfully","success")
        return redirect(url_for('product_movements.product_movements'))
    return render_template('edit_movements.html',form=form ,location_id=my_movement.transaction_id, title="Edit Product Movement")


@movement_blueprint.route('/delete_movement/<int:transaction_id>',methods=['POST'])
@login_required
def delete_movement(transaction_id):
    movement = Movements.query.filter_by(transaction_id=transaction_id).first()
    if movement:
        db.session.delete(movement)
        db.session.commit()
        flash("Record has been deleted successfully","success")
        return redirect(url_for('product_movements.product_movements'))
