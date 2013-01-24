# -*- coding: iso-8859-1 -*-
import sieve


def test1():
    s = sieve.sieve()
    i = s.__iter__()
    print i.next() 
    
def test2():
    s = sieve.sieve()
    i = s.__iter__()
    print i.next() 

def test3():
    s = sieve.sieve()
    i = s.__iter__()
    print i.next() 

test1()
test2()
test3()

#With the generator functionality, the value of i.next() is preserved
#so the next time i.next() is called, it will be the next item generated
#despite being contained within seperate tests