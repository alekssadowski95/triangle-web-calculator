from flask import render_template, session
from flaskpackage import app, db
from flaskpackage.models import Calculation
from flaskpackage.forms import CalculateTrangleForm
from calculation import calculate


@app.route('/', methods=['GET', 'POST'])
def home():
    form = CalculateTrangleForm()
    if form.validate_on_submit():
        calculation = Calculation(height=form.height.data, angle=form.angle.data)
        db.session.add(calculation)
        db.session.commit()
        session['RESULT'] = calculate(form.height.data, form.angle.data)
    return render_template('home.html', form=form, result=session['RESULT'])
