#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import doctest
from checkfiles import Check_directory

def mul(x, y):
    '''
    >>> mul(100, 200)
    20000


    >>> mul(1, 2)
    2

    >>> mul(2, 4)
    6
    '''
    return x * y

    '''
    

    
    

    '''

if __name__ == '__main__':
    doctest.testmod()