class GameTeam:
    def __init__(self, team):
        self.team = team
        self.lineup = []
        self.bench = []
        self.starter = 0
        self.bullpen = []
        self.positions = []

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

    def printLineup(self):
        print("\n\nLineup\n\n")
        for player in self.lineup:
            player.printShort()
