import unittest
from lab1 import *
# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """tests max_list_iter"""
        #in order max test
        self.assertEqual(max_list_iter([1,2,3,4,5]),5)
        #out of order max test
        self.assertEqual(max_list_iter([1, 5, 3, 4, 1]), 5)
        #single element max test
        self.assertEqual(max_list_iter([1]), 1)
        tlist = None
        #none test - valueError test

        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        # empty list test
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter([])

    def test_reverse_rec(self):
        """test reverse list function"""
        #basic reverse
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1, 2, 3,4,5]), [5,4,3, 2, 1])
        #reverse with one element
        self.assertEqual(reverse_rec([1]),[1])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        """test bianry search funtion """
        list_val =[0,1,2,3,4,7,8,9,10]
        #basic bin search test
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        #search for first term
        self.assertEqual(bin_search(1,1,10,list_val),1)
        #search for term in second half of list
        self.assertEqual(bin_search(7, 1, 10, list_val), 5)
        #seacrh for term not in list
        self.assertEqual(bin_search(11,0,10,list_val),None)
        self.assertEqual(bin_search(6, 0, 10, list_val), None)
        #tests for none

        with self.assertRaises(ValueError):
            bin_search(0,0,0,None)

        # tests for empty list
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, [])

if __name__ == "__main__":
        unittest.main()

