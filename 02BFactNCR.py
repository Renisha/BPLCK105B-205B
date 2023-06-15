#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:36:52 2022

02BFactNCR.py

Write a function to calculate factorial of a number. 
Develop a program to compute binomial coefficient (Given N and R).

@author: Prabodh C P
"""

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)
    
    
n = int(input("Enter the value of N : "))
r = int(input("Enter the value of R (R cannot be negative or greater than N): "))
nCr = fact(n)/(fact(r)*fact(n-r))

print(n,'C',r," = ","%d"%nCr,sep="")
