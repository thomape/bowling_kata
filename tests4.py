import unittest
from bowling4 import Bowling

class Tests(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Bowling()

    # helper section
    def roller(self,pins):
        for x in range(20):
            self.game.roll(pins)
    
    def strike_roller(self,pins):
        for x in range(12):
            self.game.roll(pins)

    def spare_roller(self,pins):
        for x in range(21):
            self.game.roll(pins)

    # test section
    def test_score_card(self):
        self.assertEqual(len(self.game.score_card),10)

    def test_all_zeros(self):
        self.roller(0)
        self.assertEqual(self.game.calculate_score(),0)

    def test_all_ones(self):
        self.roller(1)
        self.assertEqual(self.game.calculate_score(),20)

    def test_all_strikes(self):
        self.strike_roller(10)
        self.assertEqual(self.game.calculate_score(),300)

    def test_all_spares(self):
        self.spare_roller(5)
        self.assertEqual(self.game.calculate_score(),150)

    def test_single_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(5)
        self.assertEqual(self.game.calculate_score(),20)

    def test_single_strike(self):
        self.game.roll(10)
        self.game.roll(1)
        self.game.roll(1)
        self.assertEqual(self.game.calculate_score(),14)

    def test_custom_game(self):
        self.game.roll(1)
        self.game.roll(1) # 2

        self.game.roll(2)
        self.game.roll(2) # 6

        self.game.roll(3)
        self.game.roll(3) # 12

        self.game.roll(4)
        self.game.roll(4) # 20
        
        self.game.roll(5)
        self.game.roll(5) # 36

        self.game.roll(6) # 42
        self.game.roll(0)

        self.game.roll(7) # 49
        self.game.roll(0)
 
        self.game.roll(8) # 57
        self.game.roll(0)

        self.game.roll(9) # 66
        self.game.roll(0)

        self.game.roll(10) # 78
        self.game.roll(1)
        self.game.roll(1)
        self.assertEqual(self.game.calculate_score(),78)

if __name__ == '__main__':
    unittest.main()