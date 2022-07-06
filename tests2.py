import unittest
from bowling2 import Game

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Game()

    def roll_many(self, rolls, pins):
        for roll in range(0, rolls):
            self.g.roll(pins)

    def roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)

    def roll_strike(self):
        self.g.roll(10)

    def test_gutter_game(self):
        rolls = 20
        pins = 0
        self.roll_many(rolls, pins)
        self.assertEqual(self.g.score(),0)

    def test_all_ones(self):
        rolls = 20
        pins = 1
        self.roll_many(rolls, pins)
        self.assertEqual(self.g.score(), 20)

    def test_one_spare(self):
        self.roll_spare()
        self.g.roll(3)
        self.roll_many(17,0)
        self.assertEqual(self.g.score(),16)

    def test_one_strike(self):
        self.roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self.roll_many(16,0)
        self.assertEqual(self.g.score(), 24)

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.g.score(), 300)


    if __name__ == "__main__":
        unittest.main()


