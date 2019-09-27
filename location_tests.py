import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("MSP", 39.3, -20.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")
        # equal test
        self.assertEqual(loc.__eq__(loc), True)
        self.assertEqual(loc.__eq__(loc1), False)

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("MSP", 39.3, -20.7)
        # equal test -true
        self.assertEqual(loc.__eq__(loc), True)
        # equal test -False
        self.assertEqual(loc.__eq__(loc1), False)
        # different variable type tess
        self.assertEqual(loc.__eq__(3), False)
        # none test
        self.assertEqual(loc.__eq__(None), False)

    # Add more tests!


if __name__ == "__main__":
    unittest.main()
