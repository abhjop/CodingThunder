from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from datetime import datetime
import json
import sqlite3


with open("config.json", "r") as config:
    params = json.load(config)["params"]

local_server= True

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_server"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_server"]

class Contacts(db.Model):
    contact_sr_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contact_name = db.Column(db.String(80), nullable=False)
    contact_phone_num = db.Column(db.String(12), nullable=False)
    contact_message = db.Column(db.String(120), nullable=False)
    contact_date = db.Column(db.String(12), nullable=False)
    contact_email = db.Column(db.String(20), nullable=True, unique=True)

class Post(db.Model):
    post_sr_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_title = db.Column(db.String(1000), nullable=False)
    post_content = db.Column(db.String(5000), nullable=False)
    post_date = db.Column(db.String(20), nullable=True)
    
    
class SignupDetails(db.Model):
    reg_srno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reg_frist_name = db.Column(db.String(30), nullable=False)
    reg_last_name = db.Column(db.String(30), nullable=False)
    reg_gender = db.Column(db.String(12), nullable=False)
    reg_phone_no = db.Column(db.Integer, nullable=False)
    reg_birth_date = db.Column(db.String(12), nullable=False)
    reg_date = db.Column(db.String(12), nullable=False)
    reg_email = db.Column(db.String(20), nullable=True, unique=True)
    reg_subject = db.Column(db.String(30), nullable=False)
    reg_password = db.Column(db.String(256), nullable=False)
    
#create first app
@app.route('/')
def home():
    return render_template('index.html', params = params)


@app.route('/about')
def aboout():
    return render_template('about.html', params = params)


@app.route('/posts')
def post():
    return render_template('posts.html', params = params)


@app.route('/contact', methods = ['GET', 'POST'])
def Contact():
    if(request.method == 'POST'):
        
        name = request.form.get('name')
        phone_num = request.form.get('phone_num')
        message = request.form.get('message')
        email = request.form.get('email')

        entry_contact = Contacts(contact_name=name, contact_phone_num=phone_num, contact_date=datetime.now(), contact_message=message, contact_email=email)
        db.session.add(entry_contact)
        db.session.commit()

    
    return render_template('contact.html', params = params)

@app.route('/set-post', methods = ['GET', 'POST'])
def setPost():
    if(request.method == 'POST'):        
        title = request.form.get('title')
        content = request.form.get('content')

        entry_post = Post(post_title=title, post_date=datetime.now(), post_content=content)
        db.session.add(entry_post)
        db.session.commit()    
    return render_template('set-post.html', params = params)


@app.route('/signup', methods = ['GET', 'POST'])
def signUp():
    msg = ''
    if (request.method == 'POST' and 'email' in request.form and 'password' in request.form):
        password = sha256_crypt.encrypt(request.form['password'])
        email = request.form['email']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        gender = request.form['inlineRadio']
        phoneNo = request.form['phoneNumber']
        birthDate = request.form['birthdayDate']
        subject = request.form['chooseSubject']
        if SignupDetails.query.filter_by(reg_email=email.data).first():
            raise ValidationError("Email already registered!")
        else:
            entry_post = SignupDetails(reg_email=email, reg_password=password, reg_frist_name=firstName, reg_last_name=lastName, 
                                    reg_gender=gender, reg_phone_no=phoneNo, reg_birth_date=birthDate, reg_subject=subject, 
                                    reg_date=datetime.now())
            db.session.add(entry_post)
            db.session.commit()
        if request.method == 'POST':
            msg = 'You have successfully registered !'
            return render_template('login.html', params = params, msg = msg)
    return render_template('signup.html', params = params)


@app.route('/login')
def login():
    return render_template('login.html', params = params)


with app.app_context():
    db.create_all()
#---------run the main file--------- 

if __name__ == '__main__':
    app.run(debug = True)