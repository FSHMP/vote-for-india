from voteforindia import app
from flask import render_template, request, jsonify


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')


@app.route('/respond', methods=['POST'])
def respond():
    print request.json
    return jsonify(), 200
