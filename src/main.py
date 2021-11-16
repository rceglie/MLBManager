from Player import *
from createplayers import *
from saveoperations import *
from GameTeam import *
from Game import *
from schedulecreation import *
import time


def main():
    league = startup()

    seasons = 1
    for i in range(seasons):
        league.newSeason()
        simulateSeason(league)
        league.sort()
    printSeasonStandings(league)
    total = 0
    #for i in range(seasons):
    #    total += simulateGame(league, league.allTeams[i%30], league.allTeams[(i*2)%30])
    #print(total/(2*seasons))



def printSeasonStandings(league):
    avg = 0
    print("\tAL East\n\t\tW\tL\t%")
    for t in league.ALEast:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
        avg += t.wins
    print("\t\t\t\t.%d" % (avg/5/.162))
    avg = 0
    print("\tAL Central")
    for t in league.ALCentral:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
        avg += t.wins
    print("\t\t\t\t.%d" % (avg/5/.162))
    avg = 0
    print("\tAL West")
    for t in league.ALWest:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
        avg += t.wins
    print("\t\t\t\t.%d" % (avg/5/.162))
    avg = 0
    print("\tNL East")
    for t in league.NLEast:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
        avg += t.wins
    print("\t\t\t\t.%d" % (avg/5/.162))
    avg = 0
    print("\tNL Central")
    for t in league.NLCentral:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
        avg += t.wins
    print("\t\t\t\t.%d" % (avg/5/.162))
    avg = 0
    print("\tNL West")
    for t in league.NLWest:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
        avg += t.wins
    print("\t\t\t\t.%d" % (avg/5/.162))


def simulateSeason(league):
    j = 0
    for day in league.schedule:
        i = 0
        j += 1
        for matchup in day:
            # print("Day #%d, Game #%d" %(j, i))
            # print("%s vs %s" % (matchup[0].name, matchup[1].name))
            i += 1
            result = simulateGame(league, matchup[0], matchup[1])
            result[0].team.wins += 1
            result[1].team.losses += 1


def simulateGame(le, a, b):
    # creates GameTeams for each
    gt1 = GameTeam(a)
    gt2 = GameTeam(b)

    # sets "best" lineup for each
    gt1.bestLineup()
    gt2.bestLineup()

    # creates and simulates game
    game = Game(gt1, gt2)
    # print(gt1.name + " vs " + gt2.name)
    game.pitcher = gt2.positions[0]
    game.batter = gt1.lineup[0]
    game.startGame()
    #return game.hScore + game.aScore
    #return game.hPC + game.aPC
    return [game.winner, game.loser]


if __name__ == "__main__":
    main()
