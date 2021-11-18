class GameTeam:
    def __init__(self, team):
        self.name = team.name
        self.team = team
        self.lineup = []
        self.bench = []
        self.bullpen = self.team.bullpen
        self.positions = []
        self.toBat = 0
        self.batter = None
        self.pitcher = None
        self.usedPitchers = []

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

        self.pitcher = self.team.getStarter()
        self.lineup[8] = self.pitcher
        self.usedPitchers.append(self.pitcher)

    def getReliever(self):
        self.team.bullpen = sorted(self.team.bullpen, key=lambda player: player.energy, reverse=True)
        #print("\nBullpen:\n")
        #for p in self.team.bullpen:
        #    p.printStam()
        self.pitcher = self.team.bullpen[0]
        #print("\nUsing:")
        #self.pitcher.printStam()
        #print("")
        self.usedPitchers.append(self.pitcher)
        return self.pitcher

    def endGame(self):
        energyGain = 33
        for p in self.team.rotation:
            if (p not in self.usedPitchers) & (p.energy < 100):
                p.energy += energyGain
        for p in self.team.bullpen:
            if (p not in self.usedPitchers) & (p.energy < 100):
                p.energy += energyGain

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
