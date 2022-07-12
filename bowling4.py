# Bowling Game
# Rules
# 10 frames per game
# 2 rolls per frame
# scoring is sum of pins
# strike is all pins first rolls
# spare is all pins both rolls
# special scoring for strike
# special scoring for spares
# 10th frame extra roll if strike or spare

class Bowling:

    def __init__(self) -> None:
        self.score_card = [[0 for x in range(2)] for y in range(10)]
        self.score_card[9].append(0)
        self.frame = 0
        self.roll_count = 0

    def is_strike(self,frame):
        return self.score_card[frame][0] == 10
    
    def is_spare(self,frame):
        return sum(self.score_card[frame]) == 10

    def calculate_score(self):
        score = 0

        for frame in range(len(self.score_card)):

            if self.is_strike(frame):
                if frame < 8 and self.is_strike(frame + 1):
                    score += self.score_card[frame + 1][0] + self.score_card[frame + 2][0] + 10
                elif  frame == 9:
                    score += self.score_card[frame][1] + self.score_card[frame][2] + 10
                else:
                    score += self.score_card[frame + 1][0] + self.score_card[frame + 1][1] + 10
            elif self.is_spare(frame):
                score += self.score_card[frame + 1][0] + 10
            else:
                score += sum(self.score_card[frame])

        return score

    def roll(self,pins):

        if self.roll_count == 2 and self.frame != 9:
            self.roll_count = 0
            self.frame += 1

        if self.roll_count == 0 and pins == 10 and self.frame != 9:
            self.score_card[self.frame][0] = pins
            self.roll_count = 2
        else:        
            self.score_card[self.frame][self.roll_count] = pins
            self.roll_count += 1



if __name__ == '__main__':
    
    game = Bowling()



    for x in range(21):
        game.roll(5)

    print(game.calculate_score())
    print(game.score_card)
