from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
# app.config['DB_NAME'] = 'data.db'

@app.route('/')
def index():
    title='Welcome'
    return render_template('./index.html', title=title)

@app.route('/accounts')
def accounts():
    title='Accounts'
    return render_template('./accounts.html', title=title)

@app.route('/create-account')
def create_accounts():
    title='Create Account'
    return render_template('./create-account.html', title=title)

app.run()