# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 09:35:30 2017

@author: sven.langer
"""

import sys

def foo():
    """
    My numpydoc description of a kind of very exhautive numpydoc format docstring.

    Parameters
    ----------
    first : array_like
        the 1st param name `first`
    second :
        the 2nd param
    third : {'value', 'other'}, optional
        the 3rd param, by default 'value'
    
    Returns
    -------
    string
        a value in a string
    
    Raises
    ------
    KeyError
        when a key error
    OtherError
    when an other error
    """
    print("bar")
                
def main(argv):
    print(argv[0])
    foo()
    

if __name__ == "__main__":
    main(sys.argv[1:])
    
