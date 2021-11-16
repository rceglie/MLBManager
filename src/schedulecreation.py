import random as r


def createSchedule(lg):
    schedule = []
    full = lg.allTeams.copy()

    massSchedule = []
    for tm in full:
        for t in full:
            massSchedule.append([tm, t])

    for g in massSchedule:
        if g[0] == g[1]:
            massSchedule.remove(g)

    for i in range(54):
        game = makeSeries(massSchedule)
        schedule.append(game)
        schedule.append(game)
        schedule.append(game)

    return schedule


def makeSeries(mass):
    game = []
    teamsCycled = []
    for i in range(15):
        valid = 0
        while valid == 0:
            matchup = mass[r.randint(0, len(mass) - 1)]
            if (matchup[0] not in teamsCycled) & (matchup[1] not in teamsCycled):
                if (matchup[0].div == matchup[1].div) & (matchup[0].lg == matchup[1].lg):
                    valid = 1
                    game.append(matchup)
                    teamsCycled.append(matchup[0])
                    teamsCycled.append(matchup[1])
                    # print(str(i) + " " + matchup[0].name + " vs " + matchup[1].name)
                else:
                    if (r.randint(0, 100) > 50):
                        valid = 1
                        game.append(matchup)
                        teamsCycled.append(matchup[0])
                        teamsCycled.append(matchup[1])
                        # print(str(i) + " " + matchup[0].name + " vs " + matchup[1].name)
    return game
