from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'You can contact us at contact@example.com.'

@app.route('/username/<username>')
def user_profile(username):
    return f'Welcome, {username}'

if __name__ == '__main__':
    app.run()