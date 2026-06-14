# -*- coding: utf-8 -*-
"""
In this practice code we will define the 'Operations' class to function as a contained set of the 
four basic numerical operations applied to an in input list or tuple as well as seeing if values are 
relatively prime, if input values are ordered, the gcf of input values, if input values of ordered 
pair form are factors of one another,
"""



class Operations:
    def __init__(self,num_set):
        # if type(num_set) is int:
        #     # Terminate instantiation if only a single input is passed
        #     raise TypeError("A single integer value cannot be used for the 'Operation' class.")
        values_types = [type(x) for x in num_set]
        if len(set(values_types)) > 1:
            # Terminate instantiation if input values have more than one type, unless...
            if len(set(values_types)) == 2:
                uniq_set_types = list(set(values_types))
                if uniq_set_types == [int,float]:
                    # Allows the instantiation to continue when the two sets are int and float type
                    pass
                else:
                    raise TypeError("The 'Operation' class only accepts 'int' or 'float' values.")
            else:
                raise TypeError("The 'Operation' class only accepts 'int' or 'float' values.")
        elif values_types[0] not in [int,float]:
            # Check if input values are all of the 'int' or 'float' type
            raise TypeError("The 'Operation' class only accepts 'int' or 'float' values.")
        else:
            pass
        self.num_set = num_set
    
    
    def name_type(self):
        """
        Displays the values of the object.
        """
        print("Input is '{}' of type '{}'".format(self.num_set,type(self.num_set)))
        
        
    def pair_check(self):
        """
        Determines if their are two values in the object.
        
        Returns
        -------
        Returns a boolean value as to whether or not the object forms a pair of values
        """
        values = self.num_set
        if len(values) == 2:
            return True
        else:
            return False
        
        
    
    def add(self):
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



    def sub(self):
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



    def mult(self):
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


    def div(self):
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
    
    
    
    def prime(self):
        """
        Calculates whether or not the values in self are relatively prime to one another and returns
        a boolean indicating whether or not they are ('True') or are not ('False') relatively prime

        Returns
        -------
        bool
            DESCRIPTION.
        """
        values = self.num_set
        values_types = [type(x) for x in values]
        if len(set(values_types)) > 1:
            raise TypeError((
                "Sets of values can only be relatively prime if all elements are integers."
                ))
        elif values_types[0] != int:
            raise TypeError((
                "Sets of values can only be relatively prime if all elements are integers."
                ))
        else:
            pass
        for pos in range(len(values)-1):
            x = values[pos]
            rest = values[pos+1:]
            for y in rest:
                if x>=y:
                    prime_comp = x % y
                    if prime_comp == 0:
                        pass
                    else:
                        print("The values in '{}' are not relatively prime.".format(values))
                        return False
                else:
                    prime_comp = y % x
                    if prime_comp == 0:
                        pass
                    else:
                        print("The values in '{}' are not relatively prime.".format(values))
                        return False
        print("Values in '{}' are relatively prime to one another.".format(values))
        return True
            
                   
            
    def order(self):
        pass
    
    
    
    def gcf(self):
        pass
            
    
    
    def divis(self):
        """
        If the object is an ordered pair of values, determines if one of those values is divisible
        by the other value; if so, the multiplication factor is determined.
        
        Returns
        -------
        Returns a boolean value as to whether or not the divis method is successfully implemented.
        If the boolean value returns 'True', the factor for the divisibility of the values is 
        returned as well
        """
        check = self.pair_check()
        if check is False:
            raise IndexError("Function 'divis' is only defined for pairs of numbers.")
        else:
            pass
        (x,y) = self.num_set
        if x >= y:
            rem = x % y
            if rem == 0:
                factor = int(x/y)
                print("{} is divisible by {} by the factor {}.".format(x,y,factor))
                return True, factor
            else:
                print("{} is NOT divisible by {}.".format(x,y))
                return False
        else:
            rem = y % x
            if rem == 0:
                factor = int(y/x)
                print("{} is divisible by {} by the factor {}.".format(y,x,factor))
                return True, factor
            else:
                print("{} is NOT divisible by {}.".format(y,x))
                return False
            
            