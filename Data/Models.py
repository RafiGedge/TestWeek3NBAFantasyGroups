from Data.db import db


def view(player):
    return {'playerName': player.playerName,
            'team': player.team,
            'position': player.position,
            'season': player.season,
            'points': player.points,
            'games': player.games,
            'twoPercent': player.twoPercent,
            'threePercent': player.threePercent,
            'ATR': player.ATR,
            'PPG Ratio': player.PPGRatio}


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    playerName = db.Column(db.String(80))
    position = db.Column(db.String(80))
    age = db.Column(db.Integer)
    games = db.Column(db.Integer)
    gamesStarted = db.Column(db.Integer)
    minutesPg = db.Column(db.Integer)
    fieldGoals = db.Column(db.Integer)
    fieldAttempts = db.Column(db.Integer)
    fieldPercent = db.Column(db.Float)
    threeFg = db.Column(db.Integer)
    threeAttempts = db.Column(db.Integer)
    threePercent = db.Column(db.Float)
    twoFg = db.Column(db.Integer)
    twoAttempts = db.Column(db.Integer)
    twoPercent = db.Column(db.Float)
    effectFgPercent = db.Column(db.Float)
    ft = db.Column(db.Integer)
    ftAttempts = db.Column(db.Integer)
    ftPercent = db.Column(db.Float)
    offensiveRb = db.Column(db.Integer)
    defensiveRb = db.Column(db.Integer)
    totalRb = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    steals = db.Column(db.Integer)
    blocks = db.Column(db.Integer)
    turnovers = db.Column(db.Integer)
    personalFouls = db.Column(db.Integer)
    points = db.Column(db.Integer)
    team = db.Column(db.String(80))
    season = db.Column(db.Integer)
    playerId = db.Column(db.String(80))
    ATR = db.Column(db.Integer)
    PPGRatio = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'Player(id: {self.id}, name: {self.playerName}, position: {self.position} games: {self.games}, points: {self.points}, assists: {self.assists}, turnovers: {self.turnovers}, season: {self.season}, ATR: {self.ATR}, PPGRatio: {self.PPGRatio})'
