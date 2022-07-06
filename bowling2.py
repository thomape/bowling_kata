# Rules
# 10 frames with max 2 rolls per frame
# Strikes will only use one roll if done first roll
# All 10 pins by second frame is a spare
# Can't get negative amount of pins


class Game:

    _rolls = [0] * 21
    _current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1

    def _is_strike(self, frame_index):
        return self._rolls[frame_index] == 10
    
    def _is_spare(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index + 1] == 10

    def _strike_bonus(self, frame_index):
        return self._rolls[frame_index + 1] + self._rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        return self._rolls[frame_index + 2]

    def _sum_of_balls_in_frame(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index + 1]

    def score(self):
        score = 0 
        frame_index = 0
        for frame in range(0,10):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self._rolls[frame_index] + self._rolls[frame_index + 1]
                frame_index += 2
        return score


if __name__ == '__main__':
    game = Game()

    game.roll(10)
    game.roll(10)
    game.roll(10)
    game.roll(10)
    print(game.score())
    print(game._rolls)


