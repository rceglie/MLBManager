from Player import *
from helpers import *
from saveoperations import *
from GameTeam import *

def main():
    league = startup()
    game(league)

def game(le):
    t1 = le.allTeams[3]
    t2 = le.allTeams[18]
    t1.printDepthChart()
    gt1 = GameTeam(t1)

    #game1 = Game
    print(t1.name + " vs " + t2.name)

if __name__ == "__main__":
    main()

