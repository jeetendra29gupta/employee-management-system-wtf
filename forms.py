from datetime import date

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, BooleanField
from wtforms.validators import DataRequired


class EmployeeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    salary = FloatField('Salary', validators=[DataRequired()])

    date_of_joining = DateField('Date of Joining', format='%Y-%m-%d', validators=[DataRequired()], default=date.today)
    birthday = DateField('Birthday', format='%Y-%m-%d', validators=[])
    is_active = BooleanField('Is Active', default=True)
