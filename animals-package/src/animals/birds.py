# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:28:47 2022

@author: niccr151
"""

class Birds:
    def __init__(self):
        '''Constructor for this class'''
        self.members = ['Blue Jay', 'Eagle', 'Cardinal']

    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)

