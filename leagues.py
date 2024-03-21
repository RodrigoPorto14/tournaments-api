from object.rule import Rule
from object.league import League
from object.stage import Stage

SOCCER_RULE = Rule(10,7,5,3,2);
LOL_MD1_RULE = Rule(1,0,0,0,0);
LOL_MD3_RULE = Rule(2,1,0,0,0);
LOL_MD5_RULE = Rule(3,1,0,0,0);

def football_data_league(league_id, season):
    return League(
        [
            Stage(
                f'https://api.football-data.org/v4/competitions/{league_id}/matches?season={season}',
                SOCCER_RULE,
                "PLACAR",
            )
        ],
        None
    )


cblol = {
    "2024-1" : League(
        [
            Stage(
                "https://lol.fandom.com/wiki/CBLOL/2024_Season/Split_1",
                LOL_MD1_RULE,
                "MD1",
            ),
            Stage(
                "https://lol.fandom.com/wiki/CBLOL/2024_Season/Split_1_Playoffs",
                LOL_MD5_RULE,
                "MD5",
            )
        ],
        0
    )
}


lck = {
    "2024-1" : League(
        [
            Stage(
                "https://lol.fandom.com/wiki/LCK/2024_Season/Spring_Season",
                LOL_MD3_RULE,
                "MD3",
            ),
            # Stage(
            #     "https://lol.fandom.com/wiki/LCK/2024_Season/Spring_Playoffs",
            #     LOL_MD5_RULE,
            #     "MD5",
            # )
        ],
        1000
    ) 
}

cblol_academy = {
    "2024-1" : League(
        [
            Stage(
                "https://lol.fandom.com/wiki/CBLOL_Academy/2024_Season/Split_1",
                LOL_MD1_RULE,
                "MD1",
            ),
            # Stage(
            #     "https://lol.fandom.com/wiki/CBLOL/2024_Season/Split_1_Playoffs",
            #     LOL_MD3_RULE,
            #     "MD3",
            # )
        ],
        2000
    )
}

ucl = {
    "2023" : football_data_league(2001, 2023),
}

la_liga = {
    "2023" : football_data_league(2014, 2023),
}

premier_league = {
    "2023" : football_data_league(2021, 2023),
}

serie_a = {
    "2023" : football_data_league(2019, 2023),
}

bundesliga = {
    "2023" : football_data_league(2002, 2023),
}

ligue_1 = {
    "2023" : football_data_league(2015, 2023),
}

brasileiro_a = {
    "2023" : football_data_league(2013, 2023),
    "2024" : football_data_league(2013, 2024)
}

eredivise = {
    "2023" : football_data_league(2003, 2023),
}

liga_portugal = {
    "2023" : football_data_league(2017, 2023),
}

eurocopa = {
    "2024" : football_data_league(2018, 2024),
}

world_cup = {
    "2022" : football_data_league(2000, 2022),
}

libertadores = {
    "2024" : football_data_league(2152, 2024),
}
