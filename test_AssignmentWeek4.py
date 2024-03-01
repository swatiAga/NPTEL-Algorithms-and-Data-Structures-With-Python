import unittest
from unittest import result
from parameterized import parameterized
from AssignmentWeek2 import AssignmentWeek4

class test_AssignmentWeek4(unittest.TestCase):
    @parameterized.expand([
        [{'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}, ('player3', 100)],
        [{'test1':{'Pant':84, 'Kohli':120}, 'test2':{'Pant':59, 'Gill':42}},('Pant', 143)],        
        [{'test1':{'Pant':84, 'Kohli':120}, 'test2':{'Gill':42}},('Kohli', 120)],
        [{'test1':{'Kohli':120}, 'test2':{'Gill':42}},('Kohli', 120)],
        [{'test1':{'Kohli':120}, 'test2':{}},('Kohli', 120)],
        [{'test1':{}, 'test2':{}},('',0)],
        [{'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}, 'match4':{'player2':31, 'player4':73, 'player3':88}},('player3', 188)],
        [{'match1':{'player1':38, 'player2':49}, 'match2':{'player3':99, 'player1':32}, 'match3':{'player2':56, 'player4':99, 'player3':89}, 'match4':{'player2':11, 'player4':123, 'player3':48}},('player3', 236)],
        [{'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'Ashwin':59, 'Pujara':42},'test3':{'Rahul':48, 'Shreyas':120}, 'test4':{'Rahul':59, 'Pujara':42}},('Ashwin', 143)],
        [{'test1':{'Ashwin':48, 'Kohli':20}, 'test2':{'Ashwin':39, 'Pujara':24},'test3':{'Rahul':84, 'Shreyas':95}, 'test4':{'Rahul':39, 'Pujara':94}},('Rahul', 123)]
        ])
    def test_orangecap(self,d, expected_value):
        result=AssignmentWeek4.orangecap(d)
        self.assertEqual(result,expected_value,'message.')
    
    @parameterized.expand([
    [[(4,3),(3,0)],[(-4,3),(2,1)],[(2, 1),(3, 0)]],
    [[(2,1)],[(-2,1)],[]],
    [[(3,0)],[(4,0)],[(7,0)]],
    [[(2,1),(3,0)],[(-3,0),(-2,1)],[]],
    [[(2,1),(3,0),(2,2),(3,3),(2,4),(3,5)],[(2,2),(3,3),(2,4),(3,5),(2,1),(3,0)],[(6,5), (4,4),(6,3),(4,2),(4,1),(6,0)]],
    [[(5,3),(3,1)],[(-4,3),(-2,1)],[(1, 3), (1, 1)]],
    [[],[(1,1)],[(1, 1)]],
    [[(5,4),(3,2)],[(-4,1),(-2,0)],[(5, 4), (3, 2), (-4, 1), (-2, 0)]]
        ])
    def test_addpoly(self, polynomial1, polynomial2, expected_value):
        obj=AssignmentWeek4()
        result=obj.addpoly(polynomial1,polynomial2)
        self.assertEqual(result,expected_value,'message.')
    
    @parameterized.expand([
      [[(1,1),(-1,0)],[(1,2),(1,1),(1,0)],[(1, 3),(-1, 0)]],
      [[(3,1),(-2,0)],[(4,2),(7,1),(11,0)],[(12, 3), (13, 2), (19, 1), (-22, 0)]],
      [[(1,1),(1,0)],[(1,1),(-1,0)], [(1, 2), (-1, 0)]],
      [[(3,1),(-2,0)],[],[]]
        ])
    def test_multpoly(self,polynomial1, polynomial2,expected_value):
        obj=AssignmentWeek4()
        result = obj.multpoly(polynomial1,polynomial2)
        self.assertEqual(result,expected_value,'some message')
if __name__ == '__main__':
    unittest.main()
