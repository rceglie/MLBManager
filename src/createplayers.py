from Player import *
import random as r
import names


def createHitters(num):
    players = []
    for i in range(num):
        pos = r.randint(2, 8)
        tempArr = createHPStat(pos)
        construct = []
        construct.append(names.get_first_name('male'))  # fName
        construct.append(names.get_last_name())  # lName
        construct.append(r.randint(20, 39))  # age
        construct.append(pos)  # position
        construct.append(tempArr[0])  # hit stat
        construct.append(r.randint(1, 99))  # power stat
        construct.append(r.randint(1, 99))  # contact stat
        construct.append(r.randint(1, 99))  # eye stat
        construct.append(r.randint(1, 99))  # speed stat
        construct.append(r.randint(1, 99))  # h/9 stat
        construct.append(r.randint(1, 99))  # bb/9 stat
        construct.append(r.randint(1, 99))  # k/9 stat
        construct.append(r.randint(1, 99))  # stamina stat
        construct.append(r.randint(1, 99))  # energy stat
        construct.append(r.randint(1, 99))  # battery stat
        construct.append("FA")  # team
        construct.append(0)  # salary
        construct.append(0)  # yearsleft
        players.append(Player(construct))
    return players


def createPosition(num, pos):
    players = []
    for i in range(num):
        tempArr = createHPStat(pos)
        construct = []
        construct.append(names.get_first_name('male'))  # fName
        construct.append(names.get_last_name())  # lName
        construct.append(r.randint(20, 39))  # age
        construct.append(pos)  # position
        construct.append(tempArr[0])  # hit stat
        construct.append(r.randint(1, 99))  # power stat
        construct.append(r.randint(1, 99))  # contact stat
        construct.append(r.randint(1, 99))  # eye stat
        construct.append(r.randint(1, 99))  # speed stat
        construct.append(r.randint(1, 99))  # h/9 stat
        construct.append(r.randint(1, 99))  # bb/9 stat
        construct.append(r.randint(1, 99))  # k/9 stat
        construct.append(r.randint(1, 99))  # stamina stat
        construct.append(r.randint(1, 99))  # energy stat
        construct.append(r.randint(1, 99))  # battery stat
        construct.append("FA")  # team
        construct.append(0)  # salary
        construct.append(0)  # yearsleft
        players.append(Player(construct))
    return players


def createHPStat(pos):
    hp = []
    if pos == 1:
        goodHitter = r.randint(0, 19)
        if goodHitter == 0:
            hp.append(r.randint(1, 45))
        elif goodHitter < 3:
            hp.append(r.randint(1, 19))
        else:
            hp.append(r.randint(1, 9))
        hp.append(r.randint(30, 99))
    else:
        hp.append(r.randint(30, 99))
        hp.append(r.randint(1, 9))
    return hp
