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
    return home_team(match)["shortName"], away_team(match)["shortName"]

def teams_img(match):
    return home_team(match)["crest"], away_team(match)["crest"]

def teams_score(match):
    score = match["score"]
    duration = score["duration"]
    final_score = score["fullTime"] if duration == "REGULAR" else score["regularTime"]
    return final_score["home"], final_score["away"]

def date_time(match):
    return match["utcDate"]

def get_id(match):
    return match["id"]

def soccer_matches(league):
    return generate_matches(league, get_page, matches, teams_name, teams_img, teams_score, date_time, get_id)
