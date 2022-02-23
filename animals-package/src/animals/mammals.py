# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 22:38:42 2022

@author: niccr151
"""

class Mammals:
    def __init__(self):
        '''Constructor for this class'''
        self.members = ['Tiger', 'Elephant', 'Armadillo']

    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)
