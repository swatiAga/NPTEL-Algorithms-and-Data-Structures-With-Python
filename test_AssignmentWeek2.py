from inspect import Parameter
from unittest import result
from parameterized import parameterized
import unittest
from AssignmentWeek2 import AssignmentWeek2 

class test_AssignmentWeek2(unittest.TestCase):

    @parameterized.expand([
        [6,True],
        [143,False],
        [1024,True]
        ])
    def test_threesquares(self, number, expectedresult):
        result=AssignmentWeek2.threesquares(number)
        self.assertEqual(result,expectedresult,'6 can be written as a sum of three squares.')

    @parameterized.expand([
        ["qwerty!@#2",True],
        ["(x+6)(y-5)",False],
        ["94templars",True],
        ["siruseri",False]
        ])
    def test_repfree(self,samplestring,expectedresult):
        result=AssignmentWeek2.repfree(samplestring)
        self.assertEqual(result,expectedresult,'')

    @parameterized.expand([
        [[1,2,3,5,4,3,2,1],True],
        [[1,2,3,2,4,1,2],False],
        [[1,2,3,4,5,3,2,4,5,3,2,1],False],
        [[9,5,4,-1,-2,3,7],True],
        [[5,4,3,2,1,0,-1,-2,-3],False],
        [[2,3,4,3,1],True]
    ])
    def test_hillvalley(self,data, expectedresult):
       result= AssignmentWeek2.hillvalley(data)
       self.assertEqual(result,expectedresult,"This list is a Hill")
    

if __name__ == '__main__':
    unittest.main()



