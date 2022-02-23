# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 23:54:56 2022

@author: niccr151
"""

class Fish:
    def __init__(self):
        self.members = ['Shark', 'Puffer', 'Eel']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s ' % member)