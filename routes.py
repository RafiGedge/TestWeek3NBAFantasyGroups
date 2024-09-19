from flask import Blueprint
from Data.Models import Player, db, view

players_bp = Blueprint('players', __name__, url_prefix='/players')


@players_bp.route('/', methods=['GET'])
def get_players():
    players = Player.query.all()
    return [view(player) for player in players]
