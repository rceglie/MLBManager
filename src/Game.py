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

    def pitch(self):

        # ball or strike
        val = .5 + ((self.pitcher.bbnine - 50) / 200)
        rand = r.randint(0, 100)
        if rand < val * 100:
            ballorstrike = "strike"
        else:
            ballorstrike = "ball"
        print(ballorstrike)

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
        print(swingornot)

        if swingornot == "swing":
            if ballorstrike == "strike":
                val = .25 + ((self.batter.contact - self.pitcher.knine) / 500)
            else:
                val = .1 + ((self.batter.contact - self.pitcher.knine) / 1500)
            rand = r.randint(0, 100)
            if rand < val * 100:
                inplayornot = "in play"
            else:
                inplayornot = "swing and miss"
            print(inplayornot)