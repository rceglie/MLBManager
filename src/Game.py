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
        self.firstBase = None
        self.secondBase = None
        self.thirdBase = None

        # debugging stats

        self.walks = 0
        self.totalStrikes = 0
        self.totalPitches = 0
        self.totalHits = 0
        self.games = 1

    def score(self):
        if self.battingTeam == self.home:
            self.hScore += 1
        else:
            self.aScore += 1

    def printBoxScore(self):
        print("\n%s: %d\n%s: %d\n\n" % (self.home.name, self.hScore, self.away.name, self.aScore))

    def printScore(self):
        print("\n********* %s: %d --- %s: %d *********\n" % (self.home.name, self.hScore, self.away.name, self.aScore))

    def detHitType(self):

        self.totalHits += 1

        val = .5 + ((self.pitcher.bbnine - 50) / 200)
        hr = .15 * (self.batter.power / 50)
        triple = .02 * (self.batter.power / 50)
        double = .20 * (self.batter.power / 50)
        single = 1 - (hr + triple + double)

        # print("1B: %.2f, 2B: %.2f, 3B: %.2f, HR: %.2f" % (single, double, triple, hr))
        rand = r.randint(0, 100)
        # print(rand)
        scored = 0

        if rand < (hr) * 100:

            # print(self.batter.lName + " homered.")

            if self.firstBase is not None:
                # print(self.firstBase.lName + " scored.")
                self.score()  # 1st base scores
            if self.secondBase is not None:
                # print(self.secondBase.lName + " scored.")
                self.score()  # 2nd base scores
            if self.thirdBase is not None:
                # print(self.thirdBase.lName + " scored.")
                self.score()  # 3rd base scores
            self.score()  # batter scores
            # empty bases
            self.firstBase = None
            self.secondBase = None
            self.thirdBase = None

            scored = 1
        elif rand < (hr + triple) * 100:

            # print("triple")

            if self.firstBase is not None:
                # print(self.firstBase.lName + " scored from 1st.")
                self.score()  # 1st base scores
                scored = 1
            if self.secondBase is not None:
                # print(self.secondBase.lName + " scored from 2nd.")
                self.score()  # 2nd base scores
                scored = 1
            if self.thirdBase is not None:
                # print(self.thirdBase.lName + " scored from 3rd.")
                self.score()  # 3rd base scores
                scored = 1

            self.firstBase = None
            self.secondBase = None
            self.thirdBase = self.batter

        elif rand < (hr + triple + double) * 100:

            # print(self.batter.lName + " doubled.")

            if self.thirdBase is not None:
                self.score()
                # print(self.thirdBase.lName + " scored from 3rd.")
                self.thirdBase = None
                scored = 1
            if self.secondBase is not None:
                self.score()
                # print(self.secondBase.lName + " scored from 2nd.")
                self.secondBase = None
                scored = 1
            if self.firstBase is not None:
                rand = r.randint(0, 100)
                if rand < self.firstBase.speed * 100:
                    self.score()
                    # print(self.firstBase.lName + " scored from 1st.")
                    self.firstBase = None
                    scored = 1
                else:
                    # advance to third
                    self.thirdBase = self.firstBase
                    # print(self.firstBase.lName + " to 3rd.")
                    self.firstBase = None

            self.secondBase = self.batter

        else:

            # print(self.batter.lName + " singled.")

            if self.thirdBase is not None:
                self.score()
                # print(self.thirdBase.lName + " scored from 3rd.")
                self.thirdBase = None
                scored = 1
            if self.secondBase is not None:
                rand = r.randint(0, 100)
                if rand < self.secondBase.speed * 100:
                    # advance to home
                    self.score()
                    # print(self.secondBase.lName + " scored from 2nd.")
                    self.secondBase = None
                    scored = 1
                else:
                    # advance to third
                    self.thirdBase = self.secondBase
                    # print(self.secondBase.lName + " to 3rd.")
                    self.secondBase = None
            if self.firstBase is not None:
                if self.firstBase.speed == 99:
                    self.score()
                    # print(self.firstBase.lName + " scored from 1st.")
                    self.firstBase = None
                    scored = 1
                else:
                    rand = r.randint(0, 100)
                    if (rand < self.firstBase.speed * 100) & (self.thirdBase is None):
                        # advance to 3rd
                        # print(self.firstBase.lName + " to 3rd.")
                        self.thirdBase = self.firstBase
                        self.firstBase = None
                    else:
                        # advance to 2nd
                        # print(self.firstBase.lName + " to 2nd.")
                        self.secondBase = self.secondBase
                        self.firstBase = None

            self.firstBase = self.batter
        # if scored == 1:
        # self.printScore()

    def pitch(self):

        self.totalPitches += 1

        # if (self.balls == 0) & (self.strikes == 0):
        # print("\t\tNow Batting: " + self.batter.lName)

        # ball or strike
        val = .53 + ((self.pitcher.bbnine - 50) / 400)
        val = .55
        rand = r.randint(0, 100)
        if rand < val * 100:
            ballorstrike = "strike"
            self.totalStrikes += 1
        else:
            ballorstrike = "ball"

        # swing?
        if ballorstrike == "strike":
            val = .66 + ((self.batter.eye - 50) / 150)
        else:
            val = .15 + ((self.pitcher.knine - self.batter.eye) / 750)
            val = .1
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
                val = .65 + (((1 * self.batter.contact) - self.pitcher.knine) / 200)
            else:
                val = .1 + ((self.batter.contact - self.pitcher.knine) / 1500)
            rand = r.randint(0, 100)
            if rand < val * 100:
                inplayornot = "in play"
            else:
                inplayornot = "swing and miss"
                self.strikes += 1

            # hit or out?
            if inplayornot == "in play":
                val = .23 + ((self.batter.hit - self.pitcher.hnine) / 400)
                rand = r.randint(0, 100)
                if rand < val * 100:
                    # print("\t\tBall in play, hit")
                    hitorout = "hit"
                    self.detHitType()
                else:
                    # print("\t\tBall in play, out")
                    # print(self.batter.lName + " got out (" + str(self.outs) + " out)")
                    hitorout = "out"
                    self.outs += 1
                self.resetCount()

        if swingornot == "no swing":
            # print("\t\t" + ballorstrike + "\t\t\t\t" + str(self.balls) + "-" + str(self.strikes))
            if self.balls == 4:

                # print(self.batter.lName + " walks")
                self.walks += 1
                scored = 0

                if self.firstBase is not None:
                    if self.secondBase is not None:
                        if self.thirdBase is not None:
                            # print(self.thirdBase.lName + " scored from 3rd.")
                            self.thirdBase = None
                            self.score()
                            scored = 1
                        # (self.secondBase.lName + " to 3rd.")
                        self.thirdBase = self.secondBase
                        self.secondBase = None
                    # print(self.firstBase.lName + " to 2nd.")
                    self.secondBase = self.firstBase
                    self.firstBase = None
                self.firstBase = self.batter
                self.resetCount()

                # if scored == 1:
                # self.printScore()

            elif self.strikes == 3:
                self.outs += 1
                # print(self.batter.lName + " strikes out looking (" + str(self.outs) + " out)")
                self.resetCount()
        elif swingornot == "swing":
            if inplayornot == "swing and miss":
                # print("\t\tswinging strike\t\t" + str(self.balls) + "-" + str(self.strikes))
                if self.strikes == 3:
                    self.outs += 1
                    # print(self.batter.lName + " strikes out swinging (" + str(self.outs) + " out)")
                    self.resetCount()

    def startGame(self):
        self.inning = 1
        self.half = 0
        self.outs = 0
        self.batter = self.battingTeam.batter
        while (self.inning < (self.games * 9) + 1) | (self.half == 1) | (self.aScore == self.hScore):
            toPrint = "\n--- "
            if (self.half == 0):
                toPrint += "Top"
            else:
                toPrint += "Bottom"
            # print("%s of %d\n--- Batting: %s\n--- Pitching: %s\n" % (toPrint, self.inning, self.battingTeam.name, self.pitchingTeam.name))
            while self.outs < 3:
                self.pitch()
            self.nextHalf()
        if self.hScore > self.aScore:
            self.winner = self.home
            self.loser = self.away
        else:
            self.winner = self.away
            self.loser = self.home

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
        self.pitcher = self.pitchingTeam.pitcher
        self.firstBase = None
        self.secondBase = None
        self.thirdBase = None

    def resetCount(self):
        self.strikes = 0
        self.balls = 0
        self.battingTeam.nextBatter()
        self.batter = self.battingTeam.batter
