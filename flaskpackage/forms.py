from flask_wtf import FlaskForm
from wtforms import SubmitField 
from wtforms.fields import DecimalField
from wtforms.validators import DataRequired

class CalculateTrangleForm(FlaskForm):
    height = DecimalField('Height', validators=[DataRequired()])
    angle = DecimalField('Angle', validators=[DataRequired()])
    submit = SubmitField('Calculate')