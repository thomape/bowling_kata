def score(game):

    score = 0
    x = 0
    while x < len(game):

        if game[x] + game[x + 1] == 10:
            score += 10 + game[x+2]
            x += 2
        elif game[x] == 10:
            score += 10 + game[x+1] + game[x+2]
            if x == len(game) - 3:
                break
            else:
                x += 1
        else:
            score += game[x] + game[x+1]
            x += 2

    return score
