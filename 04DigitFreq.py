#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:12:31 2022

04DigitFreq.py

Read a multi-digit number (as chars) from the console. 
Develop a program to print the frequency of each digit with suitable message.

@author: Prabodh C P
"""

num = input("Enter a number : ")
print("The number entered is :", num)

uniqDig = set(num)
#print(uniqDig)

for elem in uniqDig:
    print(elem, "occurs", num.count(elem), "times")
