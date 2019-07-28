# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 00:54:14 2019

@author: HP
"""
#Write a procedure called oddTuples, which takes a tuple as input, and returns
# a new tuple as output, where every other element of the input tuple is copied,
# starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 
#then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    ret=() 
    index=1
    for t in aTup:
        if index%2==1:
            ret += (t,)
        index += 1
    return ret