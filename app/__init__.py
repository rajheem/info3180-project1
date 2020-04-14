from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://vjyvutwrdhdnwm:a14702fab93e4794b589e962bc3f4b5f2c19a11c0013bbc014adc3601ecb5929@ec2-52-200-119-0.compute-1.amazonaws.com:5432/dbnpb7luijjvs7"
#"postgresql://proj1:proj1@localhost/proj1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']= "./app/static/uploads"

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
