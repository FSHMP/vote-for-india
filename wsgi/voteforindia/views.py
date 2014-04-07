import os
from voteforindia.variables import *
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


def comparing_ranks(user, party):
    result_dict = {}
    for key, value in user.iteritems():
        if abs(value - party.get(key) == 0):
            result_dict[key] = H
        elif abs(value - party.get(key) == 1):
            result_dict[key] = N
        else:
            result_dict[key] = L
    return result_dict


def calculate_percentage(user_party_dict):
    '''returns percentage by calculating the total values of dictionary'''
    total = 0
    for value in user_party_dict.values():
        total += value
    percentage = float("%.2f" % round((total/20.0) * 100, 2))
    return percentage


def process(data_dict):
    # convert data_dict to user_dict with ranks
    user_dict = {}
    for key, value in data_dict.iteritems():
        for v in metrics.values():
            if value in v.get('range'):
                user_dict[key] = v.get('rank')

    # compare user_dict with each parties dict ranks
    # and create a new dictionary with distances
    user_bjp_dict = comparing_ranks(user_dict, bjp_dict)
    user_cong_dict = comparing_ranks(user_dict, cong_dict)
    user_aap_dict = comparing_ranks(user_dict, aap_dict)
    user_left_dict = comparing_ranks(user_dict, left_dict)

    user_bjp_percent = calculate_percentage(user_bjp_dict)
    user_cong_percent = calculate_percentage(user_cong_dict)
    user_aap_percent = calculate_percentage(user_aap_dict)
    user_left_percent = calculate_percentage(user_left_dict)

    return {'BJP': user_bjp_percent, 'INC': user_cong_percent, 'AAP': user_aap_percent, 'LEFT PARTIES': user_left_percent}


@app.route('/respond', methods=['POST'])
def respond():
    result = process(request.json)
    return jsonify(result), 200


@app.route('/methodology', methods=['GET'])
def show_methodology():
    return render_template('methodology.html')
