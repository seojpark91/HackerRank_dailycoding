def howManyGames(p, d, m, s):
    games = 0
    while s >= 0:
        s -= p
        p = max(p-d, m)
        games +=1
    return games-1

howManyGames(20, 3, 6, 80), howManyGames(20, 3, 6, 85), howManyGames(100, 19, 1, 180)