#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:36:30 2022

02AFibonacci.py

Develop a program to generate Fibonacci sequence of length (N). Read N from the console.

@author: Prabodh C P
"""

num = int(input("Enter the Fibonacci sequence length to be generated : "))

firstTerm = 0
secondTerm = 1
print("The Fibonacci series with", num, "terms is :")
print(firstTerm, secondTerm, end=" ")
for i in range(2,num):
    curTerm = firstTerm + secondTerm
    print(curTerm, end=" ")
    firstTerm = secondTerm
    secondTerm = curTerm
    
