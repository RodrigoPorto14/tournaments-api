from utils import *
from datetime import datetime
from constants import MONTHS

def matches(page):
    return page.find_all(class_= ["brkts-matchlist-match", 'match-row'])

def to_month(month):
    return MONTHS[month]

def date_time(match):
    date = match.find("span", class_ = "timer-object").text
    month, day, year, none, time, brt = date.split()
    hour, minute = time.split(':')
    return datetime(int(year), to_month(month), int(day[:-1]), int(hour), int(minute)).isoformat()+'Z'    

def teams(match):
    return match.find_all('span', class_ = ["team-template-image-icon team-template-lightmode", "team-template-image-icon lightmode"])[:2]

def name(team):
    return team.find('img').get('alt')

def teams_name(match):
    home, away = teams(match)
    return name(home), name(away)

def img(team):
    return 'https://liquipedia.net' + team.find('img').get('src')

def teams_img(match):
    home, away = teams(match)
    return img(home), img(away)

def teams_score(match):
    home, away = match.find_all('div', class_ = "brkts-matchlist-cell-content")[1:3]
    return home.string, away.string

def lol_matches(league, base_id):
    return generate_matches(league, base_id, matches, teams_name, teams_img, teams_score, date_time)
