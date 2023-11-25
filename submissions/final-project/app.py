from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
app.config['DB_NAME'] = 'accounts.db'

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

app.run()