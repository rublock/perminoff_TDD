import unittest

from square import Square


class TestSquare(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Running setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("Running tearDownClass")

    def test_area(self):
        square1 = Square(5)
        self.assertEqual(square1.area(), 25)

        square2 = Square(0)
        self.assertEqual(square2.area(), 0)

        square3 = Square(-4)
        self.assertEqual(square3.area(), 16)


if __name__ == "__main__":
    unittest.main(verbosity=2)
