# -*- coding: utf-8 -*-
"""
Created on Tue May 30 20:20:48 2023

@author: Arya
"""

print('Enter number of integers:')
n=int(input())
integers=[]
for i in range(0,n):
    print('Enter integer:')
    x=int(input())
    integers.append(x)
print('Numbers entered:',integers)
print('Positive integers are:',end='')
    
for x in integers:
    if x>0:
        print(x,end=' ')
    

        