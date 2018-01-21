# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testRightTriangle(self): # test invalid inputs
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')
        self.assertEqual(classifyTriangle(4,3,5),'Right','4,3,5 is a Right triangle')
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,4,5 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testNotIsoTriangles(self): 
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')

    def testNotATriangles(self): 
        self.assertEqual(classifyTriangle(100,10,10),'NotATriangle','not a triangle')
        self.assertEqual(classifyTriangle(10,100,10),'NotATriangle','not a triangle')
        self.assertEqual(classifyTriangle(10,10,100),'NotATriangle','not a triangle')

    def testIsoTriangles(self): 
        self.assertEqual(classifyTriangle(5,5,9),'Isoceles','Should be Isoceles')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(3,4,6),'Scalene','Should be Scalene')

    def testInvalidTriangles(self): 
        self.assertEqual(classifyTriangle(199,10,205),'InvalidInput','Should be invalid')
        self.assertEqual(classifyTriangle(-1,2,1),'InvalidInput','Should be invalid')
        self.assertEqual(classifyTriangle(3.2,4,6),'InvalidInput','Should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

