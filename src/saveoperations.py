import os
from createplayers import *
from League import *
from Team import *
from main import *
import timeit


def startup():
    # checks if there is already a save

    if os.stat("C:\\Users\\Robert\\IdeaProjects\\MLBManager\\save\\save.txt").st_size == 0:
        return firstload()
    else:
        return load()


def firstload():
    # writes 0 in save file to write something

    file = open("C:\\Users\\Robert\\IdeaProjects\\MLBManager\\save\\save.txt", "w")
    file.write("0")
    file.close()

    # create teams and league

    masterPlayerList = []

    teams = []

    teams.append(Team("Arizona", "Diamondbacks", "ARI", "NL", "west"))
    teams.append(Team("Atlanta", "Braves", "ATL", "NL", "east"))
    teams.append(Team("Baltimore", "Orioles", "BAL", "AL", "east"))
    teams.append(Team("Boston", "Red Sox", "BOS", "AL", "east"))
    teams.append(Team("Chicago", "Cubs", "CHC", "NL", "central"))
    teams.append(Team("Chicago", "White Sox", "CWS", "AL", "central"))
    teams.append(Team("Cincinnati", "Reds", "CIN", "NL", "central"))
    teams.append(Team("Cleveland", "Indians", "CLE", "AL", "central"))
    teams.append(Team("Colorado", "Rockies", "COL", "NL", "west"))
    teams.append(Team("Detroit", "Tigers", "DET", "AL", "central"))
    teams.append(Team("Houston", "Astros", "HOU", "AL", "west"))
    teams.append(Team("Kansas City", "Royals", "KC", "AL", "central"))
    teams.append(Team("Los Angeles", "Angels", "LAA", "AL", "west"))
    teams.append(Team("Los Angeles", "Dodgers", "LAD", "NL", "west"))
    teams.append(Team("Miami", "Marlins", "MIA", "NL", "east"))
    teams.append(Team("Milwaukee", "Brewers", "MIL", "NL", "central"))
    teams.append(Team("Minnesota", "Twins", "MIN", "AL", "central"))
    teams.append(Team("New York", "Mets", "NYM", "NL", "east"))
    teams.append(Team("New York", "Yankees", "NYY", "AL", "east"))
    teams.append(Team("Oakland", "Athletics", "OAK", "AL", "west"))
    teams.append(Team("Philadelphia", "Phillies", "PHI", "NL", "east"))
    teams.append(Team("Pittsburgh", "Pirates", "PIT", "NL", "central"))
    teams.append(Team("San Diego", "Padres", "SD", "NL", "west"))
    teams.append(Team("Seattle", "Mariners", "SEA", "AL", "west"))
    teams.append(Team("San Francisco", "Giants", "SF", "NL", "west"))
    teams.append(Team("St. Louis", "Cardinals", "STL", "NL", "central"))
    teams.append(Team("Tampa Bay", "Rays", "TB", "AL", "east"))
    teams.append(Team("Texas", "Rangers", "TEX", "AL", "west"))
    teams.append(Team("Toronto", "Blue Jays", "TOR", "AL", "east"))
    teams.append(Team("Washington", "Nationals", "WSH", "NL", "east"))

    file = open("C:\\Users\\Robert\\IdeaProjects\\MLBManager\\save\\teams.txt", "w")
    for team in teams:
        file.write(team.toString())
    file.close()

    league = League(teams)

    # creates players

    temp = []
    for i in range(30):
        temp.clear()
        temp.extend(createPosition(1, 2))
        temp.extend(createPosition(1, 3))
        temp.extend(createPosition(1, 4))
        temp.extend(createPosition(1, 5))
        temp.extend(createPosition(1, 6))
        temp.extend(createPosition(1, 7))
        temp.extend(createPosition(1, 8))
        temp.extend(createPosition(1, 9))  # 1 of each position (8)
        temp.extend(createHitters(5))  # 5 bench hitters
        temp.extend(createPosition(13, 1))  # 13 pitchers

        league.allTeams[i].addPlayers(temp)
        masterPlayerList.extend(temp)

    temp.clear()
    for i in range(8):
        temp.extend(createPosition(5, i + 2))  # 5 per position as free agents
    temp.extend(createPosition(50, 1))
    masterPlayerList.extend(temp)
    for t in temp:
        league.addFreeAgent(t)

    # write masterPlayerList to text file


    file = open("C:\\Users\\Robert\\IdeaProjects\\MLBManager\\save\\players.txt", "w")
    for player in masterPlayerList:
        file.write(player.toString())
    file.close()

    return league


def load():
    playerString = []
    teamsString = []
    teams = []

    with open("C:\\Users\\Robert\\IdeaProjects\\MLBManager\\save\\players.txt", "r") as file:
        for line in file:  # parse every player
            playerString.append(line)
        file.close()
    with open("C:\\Users\\Robert\\IdeaProjects\\MLBManager\\save\\teams.txt", "r") as file:
        for line in file:  # parse every team
            teamsString.append(line)
    file.close()

    # parses teams into league
    for string in teamsString:
        ps = string.split(",")
        ps[-1] = ps[-1].rstrip(ps[-1][-1])
        teams.append(Team(ps[0], ps[1], ps[2], ps[3], ps[4]))

    league = League(teams)

    teamNames = []
    for t in teams:
        teamNames.append(t.name)

    for string in playerString:
        ps = string.split(",")
        ps[-1] = ps[-1].rstrip(ps[-1][-1])
        player = Player(ps)
        if player.team != "FA":
            teams[teamNames.index(player.team)].addPlayer(player)
            #league.allTeams[teamNames.index(player.team)].addPlayer(player)
        else:
            league.addFreeAgent(player)


    return league
