from flask import Flask, jsonify
from football_data import soccer_matches
from lol_leaguepedia import lol_matches
from leagues import *

app = Flask(__name__)

@app.route('/api/cblol', methods=['GET'])
def _cblol():
    matches = lol_matches(cblol["2024-1"])
    return jsonify(matches)

@app.route('/api/ucl', methods=['GET'])
def _ucl():
    matches = soccer_matches(ucl["2023"])
    return jsonify(matches)

@app.route('/api/la-liga', methods=['GET'])
def _la_liga():
    matches = soccer_matches(la_liga["2023"])
    return jsonify(matches)

@app.route('/api/premier-league', methods=['GET'])
def _premier_league():
    matches = soccer_matches(premier_league["2023"])
    return jsonify(matches)

@app.route('/api/serie-a', methods=['GET'])
def _serie_a():
    matches = soccer_matches(serie_a["2023"])
    return jsonify(matches)

@app.route('/api/bundesliga', methods=['GET'])
def _bundesliga():
    matches = soccer_matches(bundesliga["2023"])
    return jsonify(matches)

@app.route('/api/ligue-1', methods=['GET'])
def _ligue_1():
    matches = soccer_matches(ligue_1["2023"])
    return jsonify(matches)

@app.route('/api/brasileiro-a', methods=['GET'])
def _brasileiro_a():
    matches = soccer_matches(brasileiro_a["2023"])
    return jsonify(matches)

@app.route('/api/eredivise', methods=['GET'])
def _eredivise():
    matches = soccer_matches(eredivise["2023"])
    return jsonify(matches)

@app.route('/api/liga-portugal', methods=['GET'])
def _liga_portugal():
    matches = soccer_matches(liga_portugal["2023"])
    return jsonify(matches)

@app.route('/api/eurocopa', methods=['GET'])
def _eurocopa():
    matches = soccer_matches(eurocopa["2024"])
    return jsonify(matches)

@app.route('/api/world-cup', methods=['GET'])
def _world_cup():
    matches = soccer_matches(world_cup["2022"])
    return jsonify(matches)


if __name__ == '__main__':
    app.run()