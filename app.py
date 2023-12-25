from flask import Flask, jsonify
from soccer import soccer_matches
from lol import lol_matches
from leagues import *

app = Flask(__name__)

@app.route('/api/cblol', methods=['GET'])
def cblol():
    matches = lol_matches(lck_2023_summer, 0)
    return jsonify(matches)

@app.route('/api/ucl', methods=['GET'])
def ucl():
    matches = soccer_matches(ucl_2023, 1000)
    return jsonify(matches)

@app.route('/api/la-liga', methods=['GET'])
def la_liga():
    matches = soccer_matches(la_liga_2023, 2000)
    return jsonify(matches)

@app.route('/api/premier-league', methods=['GET'])
def premier_league():
    matches = soccer_matches(premier_league_2023, 3000)
    return jsonify(matches)

@app.route('/api/serie-a', methods=['GET'])
def serie_a():
    matches = soccer_matches(serie_a_2023, 4000)
    return jsonify(matches)

@app.route('/api/bundesliga', methods=['GET'])
def bundesliga():
    matches = soccer_matches(bundesliga_2023, 5000)
    return jsonify(matches)

@app.route('/api/ligue-1', methods=['GET'])
def ligue_1():
    matches = soccer_matches(ligue_1_2023, 6000)
    return jsonify(matches)

@app.route('/api/brasileiro-a', methods=['GET'])
def brasileiro_a():
    matches = soccer_matches(brasileiro_a_2023, 7000)
    return jsonify(matches)

if __name__ == '__main__':
    app.run()
