from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired,Email,DataRequired


class ProfileForm(FlaskForm):
    first_name=StringField('fname',validators=[InputRequired()])
    last_name=StringField('lname',validators=[InputRequired()])
    gender=SelectField('gender',choices=[('Male','Male'),('Female','Female')],validators=[InputRequired()])
    email=StringField('email',validators=[Email(),InputRequired()])
    location=StringField('location',validators=[InputRequired()])
    biography=TextAreaField('biography',validators=[DataRequired()])
    profile_pic=FileField('photo',
    validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
