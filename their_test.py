import unittest
import game

class Tests(unittest.TestCase):

    def test_ones(self):
        self.assertEqual(game.score([1,1,1,1]),4)

    def test_strike(self):
        self.assertEqual(game.score([10,1,1,1,1]),16)

    def test_perfect(self):
        self.assertEqual(game.score([10,10,10,10,10,10,10,10,10,10,10,10]),300)

    def test_spare(self):
        self.assertEqual(game.score([5,5,1,1]),13)

    def test_custom(self):
        self.assertEqual(game.score([1,1,2,2,3,3,4,4,5,5,6,0,7,0,8,0,9,0,10,1,1]),78)


if __name__=='__main__':
    unittest.main()