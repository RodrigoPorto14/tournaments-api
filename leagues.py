from object.rule import Rule

SOCCER_RULE = Rule(25,18,15,13,10)
LOL_MD1_RULE = Rule(1,0,0,0,0);
LOL_MD3_RULE = Rule(2,1,0,0,0);
LOL_MD5_RULE = Rule(3,2,0,0,0);

def football_data_stage(league_id, season):
    stage = {
        "url" : f'https://api.football-data.org/v4/competitions/{league_id}/matches?season={season}',
        "rule" : SOCCER_RULE,
        "type" : "PLACAR"
    }
    return stage


cblol = {
    "2024-1" : [
        {
            "url" : "https://lol.fandom.com/wiki/CBLOL/2024_Season/Split_1",
            "rule" : LOL_MD1_RULE,
            "type" : "MD1"
        },
        # {
        #     "url" : "https://lol.fandom.com/wiki/CBLOL/2023_Season/Split_2_Playoffs",
        #     "rule" : LOL_PLAYOFFS_RULE,
        #     "type" : "MD5"
        # }
    ]
}

lck = {
    "2024-1" : [
        {
            "url" : "https://lol.fandom.com/wiki/LCK/2024_Season/Spring_Season",
            "rule" : LOL_MD3_RULE,
            "type" : "MD3"
        },
        # {
        #     "url" : "https://lol.fandom.com/wiki/LCK/2023_Season/Summer_Playoffs",
        #     "rule" : LOL_MD5_RULE,
        #     "type" : "MD5"
        # }
    ]   
}

ucl = {
    "2023" : [ football_data_stage(2001, 2023) ],
}

la_liga = {
    "2023" : [ football_data_stage(2014, 2023) ],
}

premier_league = {
    "2023" : [ football_data_stage(2021, 2023) ],
}

serie_a = {
    "2023" : [ football_data_stage(2019, 2023) ],
}

bundesliga = {
    "2023" : [ football_data_stage(2002, 2023) ],
}

ligue_1 = {
    "2023" : [ football_data_stage(2015, 2023) ],
}

brasileiro_a = {
    "2023" : [ football_data_stage(2013, 2023) ],
}

# eredivise_2023 = [
#     {
#         "url" : "https://api.football-data.org/v4/competitions/2003/matches",
#         "rule" : SOCCER_RULE,
#         "type" : "PLACAR"
#     },
# ]

# liga_portugal_2023 = [
#     {
#         "url" : "https://api.football-data.org/v4/competitions/2017/matches",
#         "rule" : SOCCER_RULE,
#         "type" : "PLACAR"
#     },
# ]

# eurocopa_2024 = [
#     {
#         "url" : "https://api.football-data.org/v4/competitions/2018/matches",
#         "rule" : SOCCER_RULE,
#         "type" : "PLACAR"
#     },
# ]

