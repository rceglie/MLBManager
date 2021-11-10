from Player import *
import random as r
import names


def createAnyPlayers(num):
    players = []
    for i in range(num):
        players.append(Player(names.get_first_name('male'), names.get_last_name(), r.randint(20,39), r.randint(1,9), r.randint(1,99), r.randint(1,99), r.randint(1,99)))
    return players

def createPitchers(num):
    players = []
    for i in range(num):
        tempArr = createHPStat(1)
        players.append(Player(names.get_first_name('male'), names.get_last_name(), r.randint(20,39), 1, tempArr[0], tempArr[1], r.randint(1,99)))
    return players

def createHitters(num):
    players = []
    for i in range(num):
        pos = r.randint(2,8)
        tempArr = createHPStat(pos)
        players.append(Player(names.get_first_name('male'), names.get_last_name(), r.randint(20,39), pos, tempArr[0], tempArr[1], r.randint(1,99)))
    return players

def createPosition(num, pos):
    players = []
    for i in range(num):
        tempArr = createHPStat(pos)
        players.append(Player(names.get_first_name('male'), names.get_last_name(), r.randint(20,39), pos, tempArr[0], tempArr[1], r.randint(1,99)))
    return players

def createHPStat(pos):
    hp = []
    if pos == 1:
        goodHitter = r.randint(0,19)
        if goodHitter == 0:
            hp.append(r.randint(1,45))
        elif goodHitter < 3:
            hp.append(r.randint(1,19))
        else:
            hp.append(r.randint(1,9))
        hp.append(r.randint(30,99))
    else:
        hp.append(r.randint(30, 99))
        hp.append(r.randint(1,9))
    return hp