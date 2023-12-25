import json
from utils import *
from datetime import datetime

MONTHS = {
    'January': 1, 
    'February': 2, 
    'March': 3, 
    'April': 4, 
    'May': 5, 
    'June': 6, 
    'July': 7, 
    'August': 8, 
    'Setember': 9, 
    'October': 10, 
    'November': 11, 
    'December': 12
}

IMAGES = {
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

# page = get_page('https://liquipedia.net/valorant/VCT/2022/Brazil/Stage_2/Challengers/Group_Stage')
# for match in matches(page):
#     print(str(teams_name(match)))


# with open('output.txt', 'w', encoding='utf-8') as file:
#     page = get_page('https://liquipedia.net/valorant/VCT/2022/Brazil/Stage_2/Challengers/Group_Stage')
#     file.write(str(matches(page)[0]))
#     print('ok')