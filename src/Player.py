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

    # def __init__(self, f, l, a, p, h, bbnine, eye, fi, tm, sal, yrs):
    #    self.fName = f
    #    self.lName=l
    #    self.age=a
    #    self.position=int(p)
    #    self.hit=int(h)
    #    self.bbnine=int(bbnine)
    #    self.eye = int(eye)
    #    self.field=fi
    #    self.team = tm
    #    self.salary = sal
    #    self.yearsLeft = yrs

    def __init__(self, list):
        self.fName = list[0]
        self.lName = list[1]
        self.age = list[2]
        self.position = int(list[3])
        self.hit = int(list[4])
        self.power = int(list[5])
        self.contact = int(list[6])
        self.eye = int(list[7])
        self.speed = int(list[8])
        self.hnine = int(list[9])
        self.bbnine = int(list[10])
        self.knine = int(list[11])
        self.stamina = int(list[12])
        self.energy = int(list[13])
        self.battery = float(list[14])
        self.team = list[15]
        self.salary = list[16]
        self.yearsLeft = list[17]

    def getBattery(self):
        self.battery = self.stamina * self.energy * self.energy
        return self.battery

    def printShort(self):
        print(self.position, self.fName, self.lName)
        print("Hit: \t\t", self.hit)
        print("Power: \t\t", self.power)
        print("Contact: \t", self.contact)
        print("Eye: \t\t", self.eye)
        print("Speed: \t\t", self.speed)
        print("H/9: \t\t", self.hnine)
        print("BB/9: \t\t", self.bbnine)
        print("K/9: \t\t", self.knine)
        print("Stamina: \t\t", self.stamina)
        print("Energy: \t\t", self.energy)
        print("Battery: \t\t", self.battery)
        print("\n")

    def printFull(self):  # not updated
        print("FName: \t\t", self.fName)
        print("LName: \t\t", self.lName)
        print("Age: \t\t", self.age)
        print("Position: \t", self.position)
        print("Hit: \t\t", self.hit)
        print("BB/9: \t\t", self.bbnine)
        print("Eye: \t\t", self.eye)
        print("Team: \t\t", self.team)
        print("Salary: \t", self.salary)
        print("Years Left: ", self.yearsLeft)
        self.printStats()

    def printStats(self):  # not updated
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
        ret = self.fName + "," + self.lName + "," + str(self.age) + "," + str(self.position) + "," + str(self.hit)
        ret = ret + "," + str(self.power) + "," + str(self.contact) + "," + str(self.eye) + "," + str(
            self.speed) + "," + str(self.hnine) + ","
        ret += str(self.bbnine) + "," + str(self.knine) + ","
        ret = ret + str(self.stamina) + "," + str(self.energy) + "," + str(self.getBattery()) + ","
        ret = ret + self.team + "," + str(self.salary) + "," + str(self.yearsLeft)
        ret = ret + "\n"
        return ret
