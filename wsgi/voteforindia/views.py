from voteforindia import app
from flask import render_template


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')
