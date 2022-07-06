import rlcompleter


class Game:

    def __init__(self):
        self.score = []

    def roll(self,pins):
        self.score.append(pins)
    
    def calc_score(self):
        roll = 0
        my_score = 0

        for x in self.score:
            if self.is_spare(roll):
                my_score += self.score[x] + self.score[x+1]
                roll += 2
            elif self.is_strike(roll):
                my_score += self.score[x] + self.score[x+1] + self.score[x+2]
                roll += 2
            else:
                my_score += self.score[x]
                roll += 1

        return my_score


    def is_spare(self, roll):
        return self.score[roll] + self.score[roll + 1] == 10

    def is_strike(self, roll):
        return self.score[roll] == 10 and roll % 2 == 0




    
if __name__ == '__main__':

    game = Game()

    for x in range(10):
        game.roll(5)

    the_score = game.calc_score()
    print(the_score)
    print(game.score)
