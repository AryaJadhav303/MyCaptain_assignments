# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:58:39 2023

@author: Arya
"""
def most_frequent():
    print('Enter word as string:',end='')
    str1=input()
    freq={}
    for i in str1:
        freq[i]=freq.get(i,0)+1
    ordered=sorted(freq,key=freq.get,reverse=True)
    print('Frequency of letters entered as string in decending order is:')
    for i in ordered:
        print(i,'=',freq[i])
            
most_frequent()

