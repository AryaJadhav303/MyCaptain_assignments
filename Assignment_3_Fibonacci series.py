# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:23:30 2023

@author: Arya
"""

print('Enter number of terms to be printed in the fibonacci series:')
t=int(input())
a=0
b=1
if t<=0:
    print('Range not valid.')
elif t==1:
    print('Fibonacci series is')
    print(a)
elif t==2:
    print('Fibonacci series is')
    print(a)
    print(b)
else:
    print('Fibonacci series is')
    print(a)
    print(b)
    for i in range(1,t-1):
        fib=a+b
        a=b
        b=fib
        print(fib)

    
    