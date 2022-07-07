class Bowling:

    def __init__(self):
        self.score = [[0 for x in range(2)] for y in range(10)]
        self.score[9].append(0) # adds a third roll to 10th frame
        self.frame = 0
        self.roll_count = 0

    # Will fill in lists as a roll with amount of pins
    def roll(self, pins):

        if self.roll_count == 2 and self.frame != 9: # reset counts after second roll
            self.roll_count = 0
            self.frame += 1

        if self.roll_count == 0 and pins == 10 and self.frame != 9:  # checking for a strike here reset counts
            self.score[self.frame][self.roll_count] = pins
            self.roll_count = 2
        else:
            self.score[self.frame][self.roll_count] = pins # normal adding
            self.roll_count += 1


    # Will generate the score after all rolls are completed
    def calculate_score(self):
        score = 0
        frame = 0
        for x in range(10):

            if frame == 8:
                score += sum(self.score[9])
            else:  
                if self.is_strike(frame): # need to look at this section. Strike rules don't make alot of sense
                    if self.score[frame][0] == 10 and self.score[frame + 1][0] == 10:
                        score += 10 + self.score[frame + 1][0] + self.score[frame + 2][0]
                    else:
                        score += 10 + self.score[frame + 1][0] + self.score[frame + 1][1]
                elif self.is_spare(frame):  # spare calculation
                    score += 10 + self.score[frame + 1][0]
                else: # normal calculation
                    score += self.score[frame][0] + self.score[frame][1]
                frame += 1

        return score

    # Helper to test if roll is a strike
    def is_strike(self,frame):
        return self.score[frame][0] == 10
    

    # Helper to test if roll is a spare
    def is_spare(self, frame):
        return self.score[frame][0] + self.score[frame][1] == 10


if __name__ == "__main__":

    # Test game
    game = Bowling()

    for x in range(21):
        game.roll(5)

    print(game.score)
    print(game.calculate_score())
