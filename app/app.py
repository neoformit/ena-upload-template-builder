"""Basic Flask app."""

import csv
import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from pathlib import Path
from wtforms import StringField, SubmitField, IntegerField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
OUTFILE = Path(os.environ['FLASK_OUTPUT_FILE'])


class MyForm(FlaskForm):
    name = StringField('Name')
    age = IntegerField('Age')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.form)
        if form.validate_on_submit():
            name = form.name.data
            age = form.age.data
            with open(OUTFILE, mode="w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Age"])
                writer.writerow([name, age])
            return render_template('success.html')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
