class Team:

    def __init__(self, lo, n, ab, l, d):
        self.name = n
        self.location = lo
        self.abb = ab
        self.lg = l
        self.div = d
        self.roster = []
        self.hitters = []
        self.pitchers = []
        self.wins = 0
        self.losses = 0

    def addPlayer(self, p):
        if p.position == 1:
            self.pitchers.append(p)
            self.roster.append(p)
        else:
            self.hitters.append(p)
            self.roster.append(p)
        p.team = self.name

    def addPlayers(self, p):
        for player in p:
            self.addPlayer(player)

    def toString(self):
        ret = ""
        ret = ret + self.location + "," + self.name +"," + self.abb +"," + self.lg +"," + self.div
        ret = ret + "\n"
        return ret

    def printDepthChart(self):
        for pos in range(9):
            for p in self.roster:
                if p.position == str(pos):
                    p.printShort()