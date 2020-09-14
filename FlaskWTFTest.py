from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(Form):
    user = StringField('Username', validators=[DataRequired()])

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = '1234567'

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = MyForm()
    if form.validate_on_submit():
        # if form.user.data == 'admin':
        if form.user.data == 'admin':
            return 'Admin login successfully'
        else:
            return 'Wrong user!'
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run()