class GameTeam:
    def __init__(self, team):
        self.name = team.name
        self.team = team
        self.lineup = []
        self.bench = []
        self.starter = 0
        self.bullpen = []
        self.positions = []
        self.toBat = 0
        self.batter = None
        self.pitcher = None

    def bestLineup(self):
        self.positions.append(self.team.positions[0][0])
        for pos in self.team.positions:
            if pos[0].position != 1:
                bestHit = 0
                bestPlayer = ""
                for player in pos:
                    if player.hit > bestHit:
                        bestHit = player.hit
                        bestPlayer = player
                self.positions.append(bestPlayer)
        self.lineup = sorted(self.positions, key=lambda player: player.hit, reverse=True)
        temp = self.lineup[0]
        self.lineup[0] = self.lineup[1]
        self.lineup[1] = temp  # swaps 1 and 2
        temp = self.lineup[1]
        self.lineup[1] = self.lineup[2]
        self.lineup[2] = temp  # swaps 1 and 3
        self.batter = self.lineup[0]
        self.pitcher = self.lineup[8]

    def printLineup(self):
        print("\n\n" + self.team.name + " " + "Lineup\n\n")
        for player in self.lineup:
            player.printShort()

    def nextBatter(self):
        if self.toBat != 8:
            self.toBat += 1
        else:
            self.toBat = 0
        self.batter = self.lineup[self.toBat]