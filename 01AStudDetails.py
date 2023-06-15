#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:01:34 2022

01AStudDetails.py
Develop a program to read the student details like Name, USN, and Marks in three subjects. 
Display the student details, total marks and percentage with suitable messages.

@author: Prabodh C P
"""

stName = input("Enter the name of the student : ")
stUSN = input("Enter the USN of the student : ")
stMarks1 = int(input("Enter marks in Subject 1 : "))
stMarks2 = int(input("Enter marks in Subject 2 : "))
stMarks3 = int(input("Enter marks in Subject 3 : "))


print("Student Details\n=========================")
print("%12s"%("Name :"), stName)
print("%12s"%("USN :"), stUSN)
print("%12s"%("Marks 1 :"), stMarks1)
print("%12s"%("Marks 2 :"), stMarks2)
print("%12s"%("Marks 3 :"), stMarks3)
print("%12s"%("Total :"), stMarks1+stMarks2+stMarks3)
print("%12s"%("Percent :"), "%.2f"%((stMarks1+stMarks2+stMarks3)/3))
print("=========================")
