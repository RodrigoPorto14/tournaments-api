from utils import generate_matches
import requests

def get_page(url):
    AUTH_KEY = 'f6ed666d4adb4ea99e2ca03abeb88943'
    headers = {
        "X-Auth-Token": AUTH_KEY,
        "Content-Type": "application/json",
    }
    return requests.get(url, headers=headers).json()

def matches(competiton):
    return competiton["matches"]

def home_team(match):
    return match["homeTeam"]

def away_team(match):
    return match["awayTeam"]

def teams_name(match):
    return home_team(match)["name"], away_team(match)["name"]

def teams_img(match):
    return home_team(match)["crest"], away_team(match)["crest"]

def teams_score(match):
    full_time_score = match["score"]["fullTime"]
    return full_time_score["home"], full_time_score["away"]

def date_time(match):
    return match["utcDate"]

def soccer_matches(league, base_id):
    return generate_matches(league, base_id, matches, teams_name, teams_img, teams_score, date_time, get_page)
