from utils import *
from datetime import datetime
import json

def matches(page):
    json_data = json.loads(page.find(id = "__NEXT_DATA__").string)
    competitions = json_data["props"]["pageProps"]["content"]["gamesets"]
    match_list = []
    for competition in competitions:
        match_list.extend(competition["matches"])
    
    return match_list

def date_time(match):
    return match["startDate"]

def home_team(match):
    return match["teamA"]

def away_team(match):
    return match["teamB"]

def teams_name(match):
    return home_team(match)["name"], away_team(match)["name"]

def teams_img(match):
    return home_team(match)["image"]["url"], away_team(match)["image"]["url"]

def teams_score(match):
    score = match["score"]
    return (home_team(score), away_team(score)) if score else (None, None)
    
def soccer_matches(league, base_id):
    return generate_matches(league, base_id, matches, teams_name, teams_img, teams_score, date_time)

# with open('output.txt', 'w', encoding='utf-8') as file:
#     page = get_page('https://lolesports.com/schedule?leagues=cblol-brazil')
#     file.write(str(page))