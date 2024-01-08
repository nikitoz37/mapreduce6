
#import time

from flask import Flask
from flask import request, render_template, redirect, url_for, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
#from config import BaseConfig
from os import environ
#import os


'''
with open(os.environ['POSTGRES_USER_FILE']) as f:
    _db_user = f.read()

with open(os.environ['POSTGRES_PASSWORD_FILE']) as f:
    _db_pass = f.read()

class BaseConfig(object):
    DEBUG = os.environ['DEBUG']
    DB_NAME = os.environ['POSTGRES_DB']
    DB_USER = _db_user
    DB_PASS = _db_pass
    DB_PORT = os.environ['DATABASE_PORT']
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@db:{DB_PORT}/{DB_NAME}'
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

'''app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)'''

#from models import *

class Word(db.Model):
    __tablename__ = 'top_words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(30), unique=True, nullable=False)
    num = db.Column(db.Integer, nullable=False)

    def __init__(self, word, num):
        self.word = word
        self.num = num
    
    def json(self):
        return {'id': self.id,'word': self.word, 'email': self.num}


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'id': self.id,'username': self.username, 'email': self.email}




with app.app_context():
    db.create_all()



#create a test route
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)


# create a user
'''@app.route('/users', methods=['POST'])
def create_user():
  try:
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({'message': 'user created'}), 201)
  except e:
    return make_response(jsonify({'message': 'error creating user'}), 500)'''


'''@app.route('/', methods=['GET'])
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    post = Post(text)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))'''



'''@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)'''



@app.route('/', methods=['GET'])
def index():
    return 'Im master'






#if __name__ == '__main__':
#    app.run()
