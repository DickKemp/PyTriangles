# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest     # this makes Python unittest module available

def buggyTriangle(a,b,c):
    """
    
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
    if a > 200 and b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= b or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
        
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
        
        
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
        
        
    """
    # require that the input values be >= 0 and <= 200
    if a > 200 and b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= b or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
        
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'
        
        
def runBuggyTriangle(a, b, c):
    """ invoke buggyTriangle with the specified arguments and print the result """
    print('buggyTriangle(',a, ',', b, ',', c, ')=',buggyTriangle(a,b,b))


def runCorrectTriangle(a, b, c):
    """ invoke buggyTriangle with the specified arguments and print the result """
    print('CorrectTriangle(',a, ',', b, ',', c, ')=',correctTriangle(a,b,b))


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testBuggyTriangle(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(buggyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testCorrectTriangle(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(buggyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(correctTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(buggyTriangle(10,15,30),'Scalene','Should be Isoceles')

        

if __name__ == '__main__':
    print('Running triangle app')
    # examples of running the buggy code
    runBuggyTriangle(1,2,3)
    runBuggyTriangle(1,1,1)
    
    # examples of running the correct code
    runCorrectTriangle(3,4,5)
    
#    print('Begin UnitTest')
    # unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
#    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       
