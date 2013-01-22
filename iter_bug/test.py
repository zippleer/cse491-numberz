# -*- coding: iso-8859-1 -*-
import fib



def test1():
    f = fib.fib(1)
    i = f.__iter__()
    assert i.next() == 2
    
def test2():
    g = fib.fib(2)
    h = g.__iter__()
    assert h.next() == 3

def test3():
    j = fib.fib(3)
    k = j.__iter__()
    assert k.next() == 5

test1()
test2()
test3()

