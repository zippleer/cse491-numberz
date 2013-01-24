# -*- coding: iso-8859-1 -*-
import sieve


def test1():
    s = sieve.sieve()
    i = s.__iter__()
    print i.next() 
    
def test2():
    s = sieve.sieve()
    i = s.__iter__()
    i.next()
    print i.next() 

def test3():
    s = sieve.sieve()
    i = s.__iter__()
    i.next()
    i.next()
    print i.next() 

test1()
test2()
test3()

#With the iterator functionality i.next() must be called x amount of times
#within each test to reach the x-th item in the sieve function