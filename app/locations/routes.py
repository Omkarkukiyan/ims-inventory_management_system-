from flask import Blueprint
from app import db
from flask import render_template, flash, redirect, url_for, request
from app.locations.forms import LocationForm
from app.models import Locations
from flask_login import login_required

location_blueprint = Blueprint('location_blueprint',__name__)


@location_blueprint.route('/locations')
@login_required
def locations():
    locations = Locations.query.all()
    if len(locations)>0:
        return render_template('location.html', title='Locations', locations=locations)
    else:
        msg="No Locations found"
        return render_template('location.html', msg=msg, tilte='Products')


@location_blueprint.route('/add_location', methods=['GET','POST'])
@login_required
def add_location():
    form = LocationForm()
    if request.method == "POST":
        location = Locations(location_name=form.location.data)
        db.session.add(location)
        db.session.commit()
        flash("Your Location has been created","success")
        return redirect(url_for('locations.locations'))
    return render_template('add_location.html', form=form, title='Add Location')


@location_blueprint.route('/edit_location/<string:location_id>', methods=['GET','POST'])
@login_required
def edit_location(location_id):
    form = LocationForm(request.form)
    my_location = Locations.query.filter_by(location_id=location_id).first()
    if my_location and request.method=="POST":
        my_location.location_name = form.location.data
        db.session.commit()
        flash("Record Updated Successfully","success")
        return redirect(url_for('locations.locations'))
    return render_template('edit_location.html',form=form ,location_id=my_location.location_id, title="Edit Location")


@location_blueprint.route('/delete_location/<int:location_id>',methods=['POST'])
@login_required
def delete_location(location_id):
    location = Locations.query.filter_by(location_id=location_id).first()
    if location:
        db.session.delete(location)
        db.session.commit()
        flash("Record has been deleted successfully","success")
        return redirect(url_for('locations.locations'))
