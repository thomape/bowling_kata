class Bowling:

    def __init__(self):
        self.score = [[0 for x in range(2)] for y in range(10)]
        self.frame = 0
        self.roll_count = 0

    def roll(self, pins):

        if self.roll_count == 2: # reset counts after second roll
            self.roll_count = 0
            self.frame += 1

        if self.roll_count == 0 and pins == 10:  # checking for a strike here reset counts
            self.score[self.frame][self.roll_count] = pins
            self.roll_count = 2
        else:
            self.score[self.frame][self.roll_count] = pins
            self.roll_count += 1


    def calculate_score(self):
        score = 0
        frame = 0
        for x in range(10):
            if self.is_strike(frame):
                score += 10 + self.score[frame + 1][0] + self.score[frame + 1][1]
            elif self.is_spare(frame):
                score += 10 + self.score[frame + 1][0]
            else:
                score += self.score[frame][0] + self.score[frame][1]
                frame += 1

        return score

    def is_strike(self,frame):
        return self.score[frame][0] == 10
    
    def is_spare(self, frame):
        return self.score[frame][0] + self.score[frame][1] == 10


if __name__ == "__main__":

    game = Bowling()

    for x in range(20):
        game.roll(5)

    print(game.score)
    print(game.calculate_score())
