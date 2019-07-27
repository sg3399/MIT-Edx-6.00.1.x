# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:51:18 2016

@author: ericgrimson
"""

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                    + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
                   - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    def convert(self):
        return self.getNumer() / self.getDenom()
    
oneHalf= fraction(1,2)
twoThirds=fraction(2,3)
print(oneHalf)
print(twoThirds)
#can mutate .numer
oneHalf.numer
#cannot mutate getNumer
oneHalf.getNumer()
twoThirds.denom
twoThirds.getDenom()

new= oneHalf + twoThirds
print(new)
new.convert()