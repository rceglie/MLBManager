class Game:
    def __init__(self, t1, t2):
        self.home = t1
        self.away = t2
        self.inning = 0
        self.half = 0
        self.hScore = 0
        self.aScore = 0
        self.winner = ""
        self.loser = ""
