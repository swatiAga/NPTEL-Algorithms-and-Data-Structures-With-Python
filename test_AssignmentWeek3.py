from inspect import Parameter
from typing import ItemsView
from unittest import result
from parameterized import parameterized
import unittest
from AssignmentWeek2 import AssignmentWeek3 
class test_AssignmentWeek3(unittest.TestCase):
    @parameterized.expand([
        [[3,1,3,5],[3, 1, 5]],
        [[7,3,-1,-5],[7, 3, -1, -5]],
        [[3,5,7,5,3,7,10],[3, 5, 7, 10]]
    ])
    def test_redmup(self,test_list, expected_length):
        result=AssignmentWeek3.remdup(test_list)
        self.assertEqual(result,expected_length,'message.')
        
    @parameterized.expand([
        [[1,3,5],[35, 0]],
        [[2,4,6],[0, 56]],
        [[-1,-2,3,7],[59, 4]],
        [[],[]],
        [None,None]
    ])
    def test_sumsquare(self, list, expected_value):
        result=AssignmentWeek3.sumsquare(list)
        self.assertEqual(result,expected_value)

    @parameterized.expand([
        [[[1,2,3],[4,5,6]],[[1, 4], [2, 5], [3, 6]]],
        [[[1],[2],[3]],[[1, 2, 3]]],
        [[[3]],[[3]]],
        [[[1,2,3]],[[1], [2], [3]]]
    ])
    def test_transpose(self, input_list, expected_transpose):
        result=AssignmentWeek3.transpose(input_list)
        self.assertEqual(result,expected_transpose)
if __name__ == '__main__':
    unittest.main()
