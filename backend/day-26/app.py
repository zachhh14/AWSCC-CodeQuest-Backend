from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_books.db'
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    published_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}-{self.author}>'

if __name__ == '__main__':
    app.app_context().push()  # Manually push the application context

    db.create_all()

    new_book = Books(title="Harry Potter", author="J.K. Rowling", published_year=1960)
    db.session.add(new_book)
    db.session.commit()

    books = Books.query.all()

    for book in books:
        print(book)
