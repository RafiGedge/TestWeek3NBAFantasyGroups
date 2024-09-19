from functools import reduce
from itertools import groupby

import requests
from Data.Models import Player
from Data.db import db
from app import app


def get_api():
    url22 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2022&&pageSize=1000'
    url23 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2023&&pageSize=1000'
    url24 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000'
    response22 = requests.get(url22).json()
    response23 = requests.get(url23).json()
    response24 = requests.get(url24).json()
    with app.app_context():
        for p in response22 + response23 + response24:
            db.session.add(Player(ATR=round(p['assists'] / p['turnovers'], 5) if p['turnovers'] != 0 else 0, **p))
        db.session.commit()
    calculate_ppg()
    with app.app_context():
        all_players = Player.query.all()
        for p in all_players:
            if '-' in p.position:
                continue  # deal with later
            p.PPGRatio = round(p.points / p.games / s22ppg.get(p.position), 5)
        db.session.commit()


s22ppg = {}
s23ppg = {}
s24ppg = {}


def calculate_ppg():
    def group_key(x):
        return x.season

    global s22ppg, s23ppg, s24ppg
    with app.app_context():
        players = Player.query.all()

    season22, season23, season24 = [list(group) for key, group in
                                    groupby(sorted(players, key=group_key), key=group_key)]
    s22ppg = group_by_position(season22)
    s23ppg = group_by_position(season23)
    s24ppg = group_by_position(season24)


def group_by_position(season: list) -> dict:
    def group_key(x):
        return x.position

    gb_season = {key: list(group) for key, group in groupby(sorted(season, key=group_key), key=group_key)}
    for i in gb_season.keys():
        if '-' in i:
            for p in i.split('-'):
                gb_season[p].extend(gb_season[i])
    result = dict()
    for i in gb_season.keys():
        if '-' not in i:
            result[i] = reduce(lambda x, y: x + y.points, gb_season[i], 0) / reduce(lambda x, y: x + y.games,
                                                                                    gb_season[i], 0)
    return result


get_api()
