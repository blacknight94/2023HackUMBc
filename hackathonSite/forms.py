from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired()])
    submit = SubmitField('ButtonClicked')