# -*- coding: iso-8859-1 -*-
# this is an implementation of the Fibonacci series using
# Python's iterator functionality.  Here, 'fib' is a class that
# obeys the iterator protocol.

class fib(object):
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        self.last_1 = 1
        self.last_2 = 1
        return self
        
    def next(self):
        count = 0
        while count < self.number:
            next_fib = self.last_1 + self.last_2
            self.last_1 = self.last_2
            self.last_2 = next_fib
            count += 1
            
        print next_fib
        return next_fib
