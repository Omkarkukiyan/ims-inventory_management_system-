from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired


class MovementForm(FlaskForm):
    product = StringField('Product', validators=[DataRequired()])
    from_location = StringField('From Location', validators=[DataRequired()])
    to_location =  StringField('To Location', validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    submit = SubmitField('Submit')
