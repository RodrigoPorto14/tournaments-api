from object.match import Match
from object.team import Team

def get_matches(get_page, matches, teams_name, teams_img, teams_score, date_time, get_id, base_id, url, match_rule, match_type):
    page = get_page(url)
    match_list = []
    for i, match in enumerate(matches(page)):
        home_name, away_name = teams_name(match)
        home_img, away_img = teams_img(match)
        home_score, away_score = teams_score(match)

        home_team = vars(Team(home_name, home_img))
        away_team = vars(Team(away_name, away_img))

        start_moment = date_time(match)
        id = get_id(match) if get_id else base_id + i

        match_list.append(vars(Match(id, match_type, start_moment, vars(match_rule), home_team, away_team, home_score, away_score)))
    
    return match_list
        
def generate_matches(league, get_page, matches, teams_name, teams_img, teams_score, date_time, get_id):
    match_list = []
    base_id = league.base_id
    for stage in league.stages:
        match_list += get_matches(
            get_page, 
            matches, 
            teams_name, 
            teams_img, 
            teams_score, 
            date_time,
            get_id,
            base_id,
            stage.url, 
            stage.rule, 
            stage.type, 
        )
        if(base_id != None):
             base_id += len(match_list)

    return match_list
