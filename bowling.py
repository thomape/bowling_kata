class Bowling:

    def __init__(self):
        self.score = [[0 for x in range(2)] for y in range(10)]
        self.frame = 0
        self.roll_count = 0

    def roll(self, pins):

        good_pins = False
        if self.roll_count == 0 and pins > 10:
            good_pins = False
        elif ((self.roll_count == 1 and pins > 10) or (pins + self.score[self.frame][0] > 10)):
            good_pins = False
        elif pins < 0:
            good_pins = False
        elif self.roll_count == 0 and pins == 10:
            good_pins = True
        else:
            good_pins = True

        if self.frame < 9 and good_pins:
            self.score[self.frame][self.roll_count] = pins
            self.roll_count += 1
            if self.roll_count == 2 or pins == 10:
                self.frame += 1
                self.roll_count = 0
            print(self.score)
        


    def running_score(self):
        running_score = 0

        for i in range(11):
            for j in range(2):
                if self.score[i][j] == 10 and i < 11:
                    running_score += self.score[i][j] + self.score[i + 1][j + 1] + self.score[i + 2][j + 2]
                    print(f'IF j = {j} and i = {i}')
                    print("if")
                elif self.score[i][j] + self.score[i][j + 1] == 10 and i < 3:
                    running_score += self.score[i][j] + self.score[i + 1][j + 1]
                #     print("hi2")
                else:
                    running_score += self.score[i][j] 
                    print(f'ELSE j = {j} and i = {i}')

        print(running_score)

if __name__ == "__main__":

    def test_game():
        for i in range(11):
            bowl.roll(10)

    bowl = Bowling()
    test_game()
    bowl.running_score()

    # bowl.roll(0)
    # bowl.roll(10)
    # bowl.roll(1)
    # bowl.roll(1)
    # bowl.roll(5)
    # bowl.roll(5)


