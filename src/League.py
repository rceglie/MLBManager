from src.schedulecreation import *


class League:

    def __init__(self, tms):
        self.allTeams = tms
        self.name = "MLB"
        self.hitterFA = []
        self.pitcherFA = []
        self.year = 0
        self.ALTeams = []
        self.NLTeams = []
        self.ALEast = []
        self.ALCentral = []
        self.ALWest = []
        self.NLEast = []
        self.NLCentral = []
        self.NLWest = []
        self.schedule = createSchedule(self)

        for t in tms:
            if t.lg == "AL":
                self.ALTeams.append(t)
                if t.div == "east":
                    self.ALEast.append(t)
                elif t.div == "central":
                    self.ALCentral.append(t)
                elif t.div == "west":
                    self.ALWest.append(t)
            elif t.lg == "NL":
                self.NLTeams.append(t)
                if t.div == "east":
                    self.NLEast.append(t)
                elif t.div == "central":
                    self.NLCentral.append(t)
                elif t.div == "west":
                    self.NLWest.append(t)

    def printDivisions(self):
        for t in self.ALEast:
            print(t.name)
        for t in self.ALCentral:
            print(t.name)
        for t in self.ALWest:
            print(t.name)
        for t in self.NLEast:
            print(t.name)
        for t in self.NLCentral:
            print(t.name)
        for t in self.NLWest:
            print(t.name)

    def addFreeAgent(self, p):
        if p.position == 1:
            self.pitcherFA.append(p)
        else:
            self.hitterFA.append(p)
        p.team = "FA"

    def getTeam(self, i):
        return self.allTeams[i]

    def sort(self):
        self.ALEast.sort(key=lambda team: team.wins, reverse=True)
        self.ALCentral.sort(key=lambda team: team.wins, reverse=True)
        self.ALWest.sort(key=lambda team: team.wins, reverse=True)
        self.NLEast.sort(key=lambda team: team.wins, reverse=True)
        self.NLCentral.sort(key=lambda team: team.wins, reverse=True)
        self.NLWest.sort(key=lambda team: team.wins, reverse=True)

    def newSeason(self):
        self.year += 1
        self.schedule = createSchedule(self)
        for t in self.allTeams:
            t.newSeason()
