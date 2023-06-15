#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:59:36 2022

03MeanVarSD.py

Read N numbers from the console and create a list. Develop a program to print mean, variance and
standard deviation with suitable messages.

@author: Prabodh C P
"""

from math import sqrt

myList = []

num = int(input("Enter the number of elements in your list : "))

for i in range(num):
    val = int(input("Enter the element : "))
    myList.append(val)
    
print('The length of list1 is', len(myList))

print('List Contents', myList)


total = 0
for elem in myList:
    total += elem

mean = total / num

total = 0
for elem in myList:
    total += (elem - mean) * (elem - mean)

variance = total / num

stdDev = sqrt(variance)

print("Mean =", mean)
print("Variance =", variance)
print("Standard Deviation =", "%.2f"%stdDev)

    
