from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
# app.config['DB_NAME'] = 'data.db'

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/accounts')
def accounts():
    return render_template('./accounts.html')

app.run()