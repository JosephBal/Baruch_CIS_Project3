# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:27:12 2023

@author: Admin
"""

# sample python program
from math import sqrt # this imports the sqrt function from math

K = 6 + 5 + 8 + 7 + 5  #31
test1 = int((( 1 + sqrt(5) )/2) ** K)
test2 = int((( 1 - sqrt(5) )/2) ** K)

print(int((test1 - test2)/ sqrt(5)))
