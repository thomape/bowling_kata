import unittest
from bowling import Bowling

class Tests(unittest.TestCase):

    # Instantiate Game for all tests
    def setUp(self):
        self.game = Bowling()

    # Helper function to do 20 rolls
    def roller(self, pins):
        for x in range(20):
            self.game.roll(pins)
    
    # Helper to roll all strikes
    def strike_roller(self, pins):
        for x in range(12):
            self.game.roll(pins)

    # Helper to roll all spares
    def spare_roller(self,pins):
        for x in range(21):
            self.game.roll(5)

    # No pins knocked down
    def test_all_zeros(self):
        self.roller(0)
        self.assertEqual(self.game.calculate_score(), 0)

    # One pin per roll knocked down
    def test_all_ones(self):
        self.roller(1)
        self.assertEqual(self.game.calculate_score(), 20)

    # Game of all spares
    def test_all_spares(self):
        self.spare_roller(5)
        self.assertEqual(self.game.calculate_score(), 150)

    # Game of all strikes
    def test_all_strikes(self):
        self.strike_roller(10)
        self.assertEqual(self.game.calculate_score(), 300)

    # Just a single spare
    def test_single_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        for x in range(1,10):
            self.game.roll(0)
        self.assertEqual(self.game.calculate_score(), 10)

    # Just a single strike
    def test_single_strike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(1)
        for x in range(2,10):
            self.game.roll(0)
        self.assertEqual(self.game.calculate_score(), 20)

    # Random game I hand calculate the total
    def test_random_game(self):
        self.game.roll(2)
        self.game.roll(3)
        self.game.roll(10)
        self.game.roll(8)
        self.game.roll(1)
        self.game.roll(4)
        self.game.roll(6)
        self.game.roll(4)
        self.game.roll(4)
        self.game.roll(4)
        self.game.roll(5)
        self.game.roll(9)
        self.game.roll(0)
        self.game.roll(2)
        self.game.roll(2)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.assertEqual(self.game.calculate_score(), 137)


if __name__ == '__main__':
    unittest.main()