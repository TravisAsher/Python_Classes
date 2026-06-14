# -*- coding: utf-8 -*-
"""
Testing space for object-oriented programming. We will create a class of basic numeric manipulation
over the reals. We will deal with addition, subtraction, multiplication, and division.
"""



class Operations:
    def __init__(self,num_set):
        self.num_set = num_set
    
    
    def name_type(self):
        print("Input is '{}' of type '{}'".format(self.num_set,type(self.num_set)))
    
    def num_add(self):
        """
        Takes the sum of all of the values in self. 

        Returns
        -------
        Returns the sum of values in self.
        """
        values = self.num_set
        result = 0
        for x in values:
            result += x
        return result



    def num_sub(self):
        """
        Takes the difference of all of the non-initial self values from the intial self value.
    
        Returns
        -------
        Returns the difference of all values after the intial value from the initial value of self.
        """   
        values = self.num_set
        result = 2*values[0]    #We double the initial value because it will be subtracted off from 
                                # itself
        for x in values:
            result -= x
        return result



    def num_mult(self):
        """
        Takes the product of all of the values in self.
    
        Returns
        -------
        Returns the product of values in self.
        """
        values = self.num_set
        result = 1
        for x in values:
            result *= x
        return result


    def num_div(self):
        """
        Performs successive division operations starting with the initial value of self as the
        dividend with the next value as the divisor and continously iterates this process with the
        result of this operation as the dividend with the next value as the divisor.
    
        Returns
        -------
        Returns the operation of successive division from the initial value in self by the
        succeeding values sequentially.
        """
        values = self.num_set
        result = values[0] ** 2 #We square the initial value because it will divided off from itself
        for x in values:
            result /= x
        return result