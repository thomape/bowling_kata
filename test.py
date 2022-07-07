import unittest
from bowling import Bowling

class Tests(unittest.TestCase):

    def setUp(self):
        self.game = Bowling()

    def roller(self, pins):
        for x in range(20):
            self.game.roll(pins)
    
    def strike_roller(self, pins):
        for x in range(10):
            self.game.roll(pins)

    def test_all_zeros(self):
        self.roller(0)
        self.assertEqual(self.game.calculate_score(), 0)

    def test_all_ones(self):
        self.roller(1)
        self.assertEqual(self.game.calculate_score(), 20)

    def test_all_spares_no_bonus(self):
        self.roller(5)
        self.assertEqual(self.game.calculate_score(), 100)

    def test_all_strikes_no_bonus(self):
        self.strike_roller(10)
        self.assertEqual(self.game.calculate_score(), 100)

    def test_all_spares(self):
        self.roller(5)
        self.assertEqual(self.game.calculate_score(), 150)

    def test_all_strikes(self):
        self.strike_roller(10)
        self.assertEqual(self.game.calculate_score(), 300)

    def test_ace_tenth(self):
        return 1




if __name__ == '__main__':
    unittest.main()