from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DB_NAME'] = 'accounts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ZACH'

db = SQLAlchemy(app)

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    website = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Accounts {self.email}-{self.password}>'

@app.route('/')
def index():
    title = 'Welcome'

    return render_template('./index.html', title=title)

@app.route('/accounts')
def accounts():
    title = 'Accounts'
    accounts = Account.query.all()

    return render_template('./accounts.html', title=title, accounts=accounts)

@app.route('/create-account')
def create_accounts():
    title = 'Create Account'

    return render_template('./create-account.html', title=title)

@app.route('/edit-account/<int:id>')
def edit_account(id):
    title = 'Edit Account'
    account = Account.query.get(id)

    return render_template('./edit-account.html', title=title, account=account)

@app.route('/add-account', methods=['POST'])
def add_accounts():
    website = request.form.get('website')
    email = request.form.get('email')
    password = request.form.get('password')

    new_account = Account(website=website, email=email, password=password)
    db.session.add(new_account)
    db.session.commit()
    flash("Account added succesfully!")  
    
    return redirect(url_for('accounts'))

@app.route('/update-account/<int:id>', methods=['GET','POSt'])
def update_account(id):
    account = Account.query.get_or_404(id)

    if request.method == 'POST':
        account.website = request.form.get('website')
        account.email = request.form.get('email')
        account.password = request.form.get('password')
        db.session.commit()
        flash("Account updated succesfully!")  

        return redirect(url_for('accounts'))
    
    return render_template('edit-account.html', account=account)

@app.route('/delete-account/<int:id>', methods=['GET', 'POST'])
def delete_account(id):
    account = Account.query.get_or_404(id)

    db.session.delete(account)
    db.session.commit()
    flash("Account deleted succesfully!")  

    return redirect(url_for('accounts'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
