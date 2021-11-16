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
    totalWins = 0
    bestWins = 0
    worstWins = 10000
    for i in range(seasons):
        league.newSeason()
        simulateSeason(league)
        league.sort()
        print(league.allTeams[3].wins)
        totalWins += league.allTeams[3].wins
        if bestWins < league.allTeams[3].wins:
            bestWins = league.allTeams[3].wins
        if worstWins > league.allTeams[3].wins:
            worstWins = league.allTeams[3].wins
    print("Average: %.1f wins/season" % (totalWins / seasons))
    print("Best: %d wins" % (bestWins))
    print("Worst: %d wins" % (worstWins))
    print("Variance: %.1f wins" % (.5 * ((bestWins - (totalWins / seasons)) + ((totalWins / seasons) - worstWins))))

    printSeasonStandings(league)


def printSeasonStandings(league):
    print("\tAL East\n\t\tW\tL\t%")
    for t in league.ALEast:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
    print("\tAL Central")
    for t in league.ALCentral:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
    print("\tAL West")
    for t in league.ALWest:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
    print("\tNL East")
    for t in league.NLEast:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
    print("\tNL Central")
    for t in league.NLCentral:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))
    print("\tNL West")
    for t in league.NLWest:
        print("%s\t\t%d\t%d\t.%0.3d" % (t.abb, t.wins, t.losses, t.wins / .162))


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

    return [game.winner, game.loser]


if __name__ == "__main__":
    main()
