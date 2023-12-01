from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from model import Account
import logging
import sqlite3

app = Flask(__name__)
app.config['DB_NAME'] = 'accounts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    website = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Accounts {self.email}-{self.password}>'

def get_db():
    db = sqlite3.connect(app.config["DB_NAME"])
    db.row_factory = sqlite3.Row
    return db

@app.route('/')
def index():
    title='Welcome'
    return render_template('./index.html', title=title)

@app.route('/accounts')
def accounts():
    title='Accounts'
    conn = get_db()
    accounts = conn.execute("SELECT * FROM accounts").fetchall()
    return render_template('./accounts.html', title=title, accounts=accounts)

@app.route('/create-account')
def create_accounts():
    title='Create Account'
    return render_template('./create-account.html', title=title)


@app.route('/add-account', methods=['POST'])
def add_accounts():
    try:
        website = request.form.get('website')
        email = request.form.get('email')
        password = request.form.get('password')

        new_account = Account(website=website, email=email, password=password)
        db.session.add(new_account)
        db.session.commit()
    except Exception as e:
        app.logger.error('Error during data insertion: %s', str(e))
        return 'Error during data insertion'
    return redirect(url_for('accounts'))

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True)