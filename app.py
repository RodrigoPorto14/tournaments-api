from flask import Flask, jsonify
from football_data import soccer_matches
from lol_leaguepedia import lol_matches
from leagues import *

app = Flask(__name__)

@app.route('/api/cblol/<season>', methods=['GET'])
def _cblol(season):
    matches = lol_matches(cblol[season])
    return jsonify(matches)

@app.route('/api/ucl/<season>', methods=['GET'])
def _ucl(season):
    matches = soccer_matches(ucl[season])
    return jsonify(matches)

@app.route('/api/la-liga/<season>', methods=['GET'])
def _la_liga(season):
    matches = soccer_matches(la_liga[season])
    return jsonify(matches)

@app.route('/api/premier-league/<season>', methods=['GET'])
def _premier_league(season):
    matches = soccer_matches(premier_league[season])
    return jsonify(matches)

@app.route('/api/serie-a/<season>', methods=['GET'])
def _serie_a(season):
    matches = soccer_matches(serie_a[season])
    return jsonify(matches)

@app.route('/api/bundesliga/<season>', methods=['GET'])
def _bundesliga(season):
    matches = soccer_matches(bundesliga[season])
    return jsonify(matches)

@app.route('/api/ligue-1/<season>', methods=['GET'])
def _ligue_1(season):
    matches = soccer_matches(ligue_1[season])
    return jsonify(matches)

@app.route('/api/brasileiro-a/<season>', methods=['GET'])
def _brasileiro_a(season):
    matches = soccer_matches(brasileiro_a[season])
    return jsonify(matches)

@app.route('/api/eredivise/<season>', methods=['GET'])
def _eredivise(season):
    matches = soccer_matches(eredivise[season])
    return jsonify(matches)

@app.route('/api/liga-portugal/<season>', methods=['GET'])
def _liga_portugal(season):
    matches = soccer_matches(liga_portugal[season])
    return jsonify(matches)

@app.route('/api/eurocopa/<season>', methods=['GET'])
def _eurocopa(season):
    matches = soccer_matches(eurocopa[season])
    return jsonify(matches)

@app.route('/api/world-cup/<season>', methods=['GET'])
def _world_cup(season):
    matches = soccer_matches(world_cup[season])
    return jsonify(matches)

@app.route('/api/libertadores/<season>', methods=['GET'])
def _libertadores(season):
    matches = soccer_matches(libertadores[season])
    return jsonify(matches)


if __name__ == '__main__':
    app.run()