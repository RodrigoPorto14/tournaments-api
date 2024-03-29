from utils import generate_matches
from bs4 import BeautifulSoup
from datetime import datetime
from constants import CBLOL_LOGOS
import requests

def get_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def matches(page):
    return page.find_all("tr", attrs = {"data-date" : True})

def date_time(match):
    time = match.find("span", class_ = "TimeInLocal").string
    ano, mes, dia, hora, minuto = time.split(',')
    return datetime(int(ano), int(mes), int(dia), int(hora), int(minuto)).isoformat()+'Z'    

def name(team):
    tr_attributes = team.parent.attrs
    name_attribute = "data-teamhighlight"
    return tr_attributes[name_attribute] if name_attribute in tr_attributes else "A ser definido"
    

def teams_name(match):
    home, away = match.find_all("span", class_ = "team")
    return name(home), name(away)

def img(team_name):
    return CBLOL_LOGOS[team_name] if team_name in CBLOL_LOGOS else ''

def teams_img(match):
    home, away = teams_name(match)
    return img(home), img(away)

def score(match, team_name):
    score = match.find("td", attrs = {"class" : "matchlist-score", "data-teamhighlight" : team_name})
    return score.string if score else None

def teams_score(match):
    home, away = teams_name(match)
    return score(match, home), score(match, away)

def lol_matches(league):
    return generate_matches(league, get_page, matches, teams_name, teams_img, teams_score, date_time, None)
