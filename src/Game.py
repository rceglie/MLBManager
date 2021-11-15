import random as r


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
        self.batter = None
        self.pitcher = None
        self.battingTeam = self.away
        self.pitchingTeam = self.home
        self.outs = 0
        self.strikes = 0
        self.balls = 0
        self.first = 0
        self.second = 0
        self.third = 0

    def detHitType(self):
        # what kind of hit
        val = .5 + ((self.pitcher.bbnine - 50) / 200)
        hr = .16 * (self.batter.power / 50)
        triple = .02 * (self.batter.power / 50)
        double = .20 * (self.batter.power / 50)
        single = 1 - (hr + triple + double)
        print("1B: %.2f, 2B: %.2f, 3B: %.2f, HR: %.2f" % (single, double, triple, hr))
        rand = r.randint(0, 100)
        print(rand)
        if rand < (hr) * 100:
            print("hr")
        elif rand < (hr + triple) * 100:
            print("triple")
        elif rand < (hr + triple + double) * 100:
            print("double")
        else:
            print("single")

    def pitch(self):

        if (self.balls == 0) & (self.strikes == 0):
            print("\t\tNow Batting: " + self.batter.lName)

        # ball or strike
        val = .5 + ((self.pitcher.bbnine - 50) / 200)
        rand = r.randint(0, 100)
        if rand < val * 100:
            ballorstrike = "strike"
        else:
            ballorstrike = "ball"

        # swing?
        if ballorstrike == "strike":
            val = .66 + ((self.batter.eye - 50) / 150)
        else:
            val = .13 + ((50 + self.pitcher.knine - self.batter.eye) / 400)
        rand = r.randint(0, 100)
        if rand < val * 100:
            swingornot = "swing"
        else:
            swingornot = "no swing"
            if ballorstrike == "strike":
                self.strikes += 1
            else:
                self.balls += 1

        # in play or swing and miss?
        if swingornot == "swing":
            if ballorstrike == "strike":
                val = .25 + (((1 * self.batter.contact) - self.pitcher.knine) / 200)
            else:
                val = .1 + ((self.batter.contact - self.pitcher.knine) / 1500)
            rand = r.randint(0, 100)
            if rand < val * 100:
                inplayornot = "in play"
                self.detHitType()
            else:
                inplayornot = "swing and miss"
                self.strikes += 1

            # hit or out?
            if inplayornot == "in play":
                val = .25 + ((self.batter.hit - self.pitcher.hnine) / 400)
                rand = r.randint(0, 100)
                if rand < val * 100:
                    hitorout = "hit"
                else:
                    hitorout = "out"
                    self.outs += 1

        if swingornot == "no swing":
            print("\t\t" + ballorstrike + "\t\t\t\t" + str(self.balls) + "-" + str(self.strikes))
            if self.balls == 4:
                print(self.batter.lName + " walks")
                self.resetCount()
            elif self.strikes == 3:
                self.outs += 1
                print(self.batter.lName + " strikes out looking (" + str(self.outs) + " out)")
                self.resetCount()
        elif swingornot == "swing":
            if inplayornot == "swing and miss":
                print("\t\tswinging strike\t\t" + str(self.balls) + "-" + str(self.strikes))
                if self.strikes == 3:
                    self.outs += 1
                    print(self.batter.lName + " strikes out swinging (" + str(self.outs) + " out)")
                    self.resetCount()
            else:
                print("\t\tBall in play")
                if hitorout == "hit":
                    print(self.batter.lName + " got a hit")
                    self.resetCount()
                else:
                    print(self.batter.lName + " got out (" + str(self.outs) + " out)")
                    self.resetCount()

        #print(ballorstrike + ", " + swingornot + ", " + inplayornot + ", " + hitorout + ", (" + self.balls + "-" + self.strikes + ")")



    def startGame(self):
        self.inning = 1
        self.half = 0
        self.outs = 0
        self.batter = self.battingTeam.batter
        while (self.inning < 3) | (self.half == 0):
            print("--- %d - %d --- Batting: %s --- Pitching: %s" % (self.inning, self.half, self.battingTeam.name, self.pitchingTeam.name))
            while self.outs < 3:
                self.pitch()
            self.nextHalf()
        # bottom of the 9th
        print("--- %d - %d --- Batting: %s --- Pitching: %s" % (self.inning, self.half, self.battingTeam.name, self.pitchingTeam.name))
        while self.outs < 3:
            self.pitch()
        print("game over")

    def nextHalf(self):
        self.outs = 0
        if self.half == 0:
            self.half = 1
            self.battingTeam = self.home
            self.pitchingTeam = self.away
        else:
            self.half = 0
            self.inning = self.inning + 1
            self.battingTeam = self.away
            self.pitchingTeam = self.home
        self.batter = self.battingTeam.batter

    def resetCount(self):
        self.strikes = 0
        self.balls = 0
        self.battingTeam.nextBatter()
        self.batter = self.battingTeam.batter