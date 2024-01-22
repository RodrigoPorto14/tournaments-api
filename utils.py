from object.match import Match
from object.team import Team

def get_matches(get_page, matches, teams_name, teams_img, teams_score, date_time, url, match_rule, match_type, base_id):
    page = get_page(url)
    match_list = []
    for i, match in enumerate(matches(page)):
        home_name, away_name = teams_name(match)
        home_img, away_img = teams_img(match)
        home_score, away_score = teams_score(match)

        home_team = vars(Team(home_name, home_img))
        away_team = vars(Team(away_name, away_img))

        start_moment = date_time(match)

        match_list.append(vars(Match(base_id + i, match_type, start_moment, vars(match_rule), home_team, away_team, home_score, away_score)))
    
    return match_list
        
def generate_matches(league, base_id, matches, teams_name, teams_img, teams_score, date_time, get_page):
    match_list = []
    for stage in league:
        match_list += get_matches(get_page, matches, teams_name, teams_img, teams_score, date_time, stage['url'], stage['rule'], stage['type'], base_id)
        base_id += len(match_list)

    return match_list
