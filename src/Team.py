class Team:

    def __init__(self, lo, n, ab, l, d):
        self.name = n
        self.location = lo
        self.abb = ab
        self.lg = l
        self.div = d
        self.roster = []
        self.hitters = []
        self.wins = 0
        self.losses = 0
        self.positions = []
        for i in range(9):
            blank = []
            self.positions.append(blank)
        self.rotation = []
        self.spotInRotation = 0
        self.bullpen = []


    def addPlayer(self, p):
        if p.position == 1:
            self.roster.append(p)
            if p.type == "starter":
                self.rotation.append(p)
            else:
                self.bullpen.append(p)
        else:
            self.hitters.append(p)
            self.roster.append(p)
        self.positions[int(p.position) - 1].append(p)
        p.team = self.name
        self.updatePitchers()

    def addPlayers(self, p):
        for player in p:
            self.addPlayer(player)

    def toString(self):
        ret = ""
        ret = ret + self.location + "," + self.name + "," + self.abb + "," + self.lg + "," + self.div
        ret = ret + "\n"
        return ret

    def printDepthChart(self):
        for pos in self.positions:
            for p in pos:
                p.printShort()

    def newSeason(self):
        self.wins = 0
        self.losses = 0

    def updatePitchers(self):
        self.rotation = sorted(self.rotation, key=lambda player: player.hnine, reverse=True)
        self.bullpen = sorted(self.bullpen, key=lambda player: player.hnine, reverse=True)

    def getStarter(self):

        ret = self.rotation[self.spotInRotation]
        if self.spotInRotation == 4:
            self.spotInRotation = 0
        else:
            self.spotInRotation += 1
        return ret
