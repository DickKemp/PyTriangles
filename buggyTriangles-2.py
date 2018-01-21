# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

@author: jrr
"""

import unittest     # this makes Python unittest module available

def correctTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      
      BEWARE: there may be a bug or two in this code
        
    """
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput-1'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput-2'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput-3';
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'
    elif ((b ** 2) + (c ** 2)) == (a ** 2):
        return 'Right'
    elif ((c ** 2) + (a ** 2)) == (b ** 2):
        return 'Right'
    elif (a == b) or (b == c) or (a == c):
        return 'Isoceles'
    else:
        print('a',a,' b',b,' c',c)
        return 'Scalene'
        
def runCorrectTriangle(a, b, c):
    print('CorrectTriangle(',a, ',', b, ',', c, ')=',correctTriangle(a,b,c))

# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testRightTriangle(self): # test invalid inputs
        self.assertEqual(correctTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(correctTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testNotIsoTriangles(self): 
        self.assertNotEqual(correctTriangle(10,10,10),'Isoceles','Should be Equilateral')

    def testIsoTriangles(self): 
        self.assertEqual(correctTriangle(5,5,9),'Isoceles','Should be Isoceles')

if __name__ == '__main__':
    print('Running triangle app')
    runCorrectTriangle(3,4,5)

    
    
       
       
