from Player import *
from createplayers import *
from saveoperations import *
from GameTeam import *
from Game import *


def main():
    league = startup()
    game(league)


def game(le):

    # 3 (red sox) vs 18 (yankees)

    # sets two teams to play
    t1 = le.allTeams[11]
    t2 = le.allTeams[0]
    # creates GameTeams for each
    gt1 = GameTeam(t1)
    gt2 = GameTeam(t2)
    # sets best lineup for each
    gt1.bestLineup()
    gt2.bestLineup()
    # print lineup for each

    games = 1000
    wins = 0
    for i in range(games):
        game = Game(gt1, gt2)
        print(t1.name + " vs " + t2.name)
        game.pitcher = gt2.positions[0]
        game.batter = gt1.lineup[0]
        game.startGame()
        if game.winner.name == t1.name:
            wins += 1
    gt1.printLineup()
    gt2.printLineup()
    print("%s won %.1f%% of the time" % (t1.name, wins * 100 / games))


if __name__ == "__main__":
    main()
