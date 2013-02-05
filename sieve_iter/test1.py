# -*- coding: iso-8859-1 -*-
import sieve


def test1():
    s = sieve.sieve()
    i = s.__iter__()
    assert i.next() == 3
    
def test2():
    s = sieve.sieve()
    i = s.__iter__()
    i.next()
    assert i.next() == 5

def test3():
    s = sieve.sieve()
    i = s.__iter__()
    i.next()
    i.next()
    assert i.next() == 7

test1()
test2()
test3()

#With the iterator functionality i.next() must be called x amount of times
#within each test to reach the x-th item in the sieve function