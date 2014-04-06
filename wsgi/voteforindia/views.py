import os
from voteforindia import app
from flask import render_template, request, jsonify

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')


@app.route('/respond', methods=['POST'])
def respond():
    print request.json
    return jsonify(), 200
