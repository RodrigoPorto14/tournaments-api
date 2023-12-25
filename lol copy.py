import json
from utils import *
from datetime import datetime

images = {
    "paiN Gaming": "https://upload.wikimedia.org/wikipedia/pt/thumb/5/5d/PainGaming.png/225px-PainGaming.png",
    "LOUD": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/LOUD_logo.svg/225px-LOUD_logo.svg.png",
    "Liberty" : "https://images.squarespace-cdn.com/content/v1/61afb10ae1f7cf52bfb3dd13/1a627bac-be78-47d3-917f-72b4d880beba/%23557q1m_presskit_logo_cyan_transparent_RGB.png",
    "INTZ" : "https://upload.wikimedia.org/wikipedia/pt/thumb/c/c3/Logo_INTZ.png/263px-Logo_INTZ.png",
    "KaBuM! Esports" : "https://cdn.escharts.com/uploads/public/63b/d6e/6ea/63bd6e6ea6631174338548.png",
    "Los Grandes" : "https://upload.wikimedia.org/wikipedia/pt/a/af/Los_Grandes_logo.png",
    "Fluxo" : "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Fluxo_escudo.png/225px-Fluxo_escudo.png",
    "Vivo Keyd Stars" : "https://api.draft5.gg/teams/1050/logo",
    "RED Canids" : "https://upload.wikimedia.org/wikipedia/pt/d/df/RED_Canids_Kalunga.png",
    "FURIA" : "https://upload.wikimedia.org/wikipedia/pt/thumb/f/f9/Furia_Esports_logo.png/218px-Furia_Esports_logo.png"
}

def matches(page):
    return page.find_all("tr", attrs = {"data-date" : True})

def date_time(match):
    time = match.find("span", class_ = "TimeInLocal").string
    ano, mes, dia, hora, minuto = time.split(',')
    return datetime(int(ano), int(mes), int(dia), int(hora), int(minuto))    

def name(team):
    return team.parent.attrs["data-teamhighlight"]

def teams_name(match):
    home, away = match.find_all("span", class_ = "team")
    return name(home), name(away)

def img(team_name):
    return images[team_name]

def teams_img(match):
    home, away = teams_name(match)
    return img(home), img(away)

def score(match, team_name):
    score = match.find("td", attrs = {"class" : "matchlist-score", "data-teamhighlight" : team_name})
    return score.string if score else None

def teams_score(match):
    home, away = teams_name(match)
    return score(match, home), score(match, away)

def lol_matches(league, base_id):
    return generate_matches(league, base_id, matches, teams_name, teams_img, teams_score, date_time)
