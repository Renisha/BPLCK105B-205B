#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:23:54 2022

01BChkSnrCitzn.py

Develop a program to read the name and year of birth of a person. Display whether the person is a senior citizen or not.

@author: Prabodh C P
"""
from datetime import date


perName = input("Enter the name of the person : ")
perDOB = int(input("Enter his year of birth : "))

curYear = date.today().year
perAge = curYear - perDOB 

if (perAge > 60):
    print(perName, "aged", perAge, "years is a Senior Citizen.")
else:
    print(perName, "aged", perAge, "years is not a Senior Citizen.")


