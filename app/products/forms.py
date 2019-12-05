from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    product = StringField('Product', validators=[DataRequired()])
    quantity = IntegerField("Quantity",validators=[DataRequired()])
    submit = SubmitField('Submit')

