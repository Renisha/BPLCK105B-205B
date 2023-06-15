#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:50:46 2022

08AssertExceptDemo.py

Write a function named DivExp which takes TWO parameters a, b and returns a value c (c=a/b). Write
suitable assertion for a>0 in function DivExp and raise an exception for when b=0. Develop a suitable
program which reads two values from the console and calls a function DivExp.

@author: Prabodh C P
"""
import sys

def DivExp(a,b):
    assert a>0, "a should be greater than 0"
    try:
        c = a/b
    except ZeroDivisionError:
        print("Value of b cannot be zero")
        sys.exit(0)
    else:
        return c

val1 = int(input("Enter a value for a : "))
val2 = int(input("Enter a value for b : "))

val3 = DivExp(val1, val2)

print(val1, "/", val2, "=", val3)
