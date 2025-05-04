from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)
app.secret_key = 'test'

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField([InputRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

    ## AUTHENTICATION OF WHETHER OR NOT THIS YAHOO ACCOUNT EVEN EXISTS GOES HERE

@app.route('/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)