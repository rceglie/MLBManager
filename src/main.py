from Player import *
from helpers import *
from saveoperations import *
from GameTeam import *
from Game import *


def main():
    league = startup()
    game(league)


def game(le):
    # sets two teams to play
    t1 = le.allTeams[3]
    t2 = le.allTeams[18]
    # creates GameTeams for each
    gt1 = GameTeam(t1)
    gt2 = GameTeam(t2)
    # sets best lineup for each
    gt1.bestLineup()
    gt2.bestLineup()
    # print lineup for each

    game = Game(gt1, gt2)
    print(t1.name + " vs " + t2.name)

    game.pitcher = gt2.positions[0]
    game.batter = gt1.lineup[0]

    gt1.printLineup()
    gt2.printLineup()

    game.startGame()


if __name__ == "__main__":
    main()
