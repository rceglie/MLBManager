class Player:
    fName = ""
    lName = ""
    age = 0
    position = ""
    hit=0
    pitch=0
    field=0

    def __init__(self, f, l, a, p, h, pi, fi):
        self.fName = f
        self.lName=l
        self.age=a
        self.position=p
        self.hit=h
        self.pitch=pi
        self.field=fi

    def print(self):
        print("FName: \t\t", self.fName)
        print("LName: \t\t", self.lName)
        print("Age: \t\t", self.age)
        print("Position: \t", self.position)
        print("Hit: \t\t", self.hit)
        print("Pitch: \t\t", self.pitch)
        print("Field: \t\t", self.field)

