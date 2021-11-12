class Player:

    # game stats

    # current season

    # hitting
    hits = 0
    hr = 0
    ab = 0
    so = 0
    rbi = 0
    bb = 0

    # pitching
    inn = 0
    runs = 0
    k = 0
    bbp = 0
    hitsp = 0

    # career

    # hitting
    chits = 0
    chr = 0
    cab = 0
    cso = 0
    crbi = 0
    cbb = 0

    # pitching
    cinn = 0
    cruns = 0
    ck = 0
    cpbb = 0
    cphits = 0



    def __init__(self, f, l, a, p, h, pi, fi, tm, sal, yrs):
        self.fName = f
        self.lName=l
        self.age=a
        self.position=p
        self.hit=h
        self.pitch=pi
        self.field=fi
        self.team = tm
        self.salary = sal
        self.yearsLeft = yrs

    def printShort(self):
        print(self.position, self.fName, self.lName)
        print("Hit: \t\t", self.hit)
        print("Pitch: \t\t", self.pitch)
        print("Field: \t\t", self.field)
        print("\n")


    def print(self):
        print("FName: \t\t", self.fName)
        print("LName: \t\t", self.lName)
        print("Age: \t\t", self.age)
        print("Position: \t", self.position)
        print("Hit: \t\t", self.hit)
        print("Pitch: \t\t", self.pitch)
        print("Field: \t\t", self.field)
        print("Team: \t\t", self.team)
        print("Salary: \t", self.salary)
        print("Years Left: ", self.yearsLeft)
        self.printStats()

    def printStats(self):
        print("Hits: \t\t", self.hits)
        print("HR: \t\t", self.hits)
        print("AB: \t\t", self.hits)
        print("SO: \t\t", self.hits)
        print("RBI: \t\t", self.hits)
        print("BB: \t\t", self.hits)
        print("cHits: \t\t", self.hits)
        print("cHR: \t\t", self.hits)
        print("cAB: \t\t", self.hits)
        print("cSO: \t\t", self.hits)
        print("cRBI: \t\t", self.hits)
        print("cBB: \t\t", self.hits)
        print("Innings: \t", self.hits)
        print("Runs: \t\t", self.hits)
        print("K: \t\t\t", self.hits)
        print("PBB: \t\t", self.hits)
        print("PHits: \t\t", self.hits)
        print("cInnings: \t", self.hits)
        print("cRuns: \t\t", self.hits)
        print("cK: \t\t", self.hits)
        print("cPBB: \t\t", self.hits)
        print("cPHits: \t", self.hits)

    def toString(self):
        ret = self.fName + "," + self.lName + "," + str(self.age) + "," + str(self.position) + "," +str(self.hit)
        ret = ret + "," +str(self.pitch) + "," +str(self.field) + "," + self.team + "," +str(self.salary) + "," + str(self.yearsLeft)
        ret = ret + "\n"
        return ret