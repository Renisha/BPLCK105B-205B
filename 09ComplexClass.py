#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:11:47 2022

09ComplexClass.py

Define a function which takes TWO objects representing complex numbers and returns new complex
number with a addition of two complex numbers. Define a suitable class ‘Complex’ to represent the
complex number. Develop a program to read N (N >=2) complex numbers and to compute the addition
of N complex numbers.

@author: Prabodh C P
"""

class Complex:
    def __init__(self, realp = 0, imagp=0):
        self.realp = realp
        self.imagp = imagp
        
    def setComplex(self, realp, imagp):
        self.realp = realp
        self.imagp = imagp

    def readComplex(self):
        self.realp = int(input("Enter the real part : "))
        self.imagp = int(input("Enter the real part : "))
        
    def showComplex(self):
        print('(',self.realp,')','+i','(',self.imagp,')',sep="")

    def addComplex(self, c2):
        c3 = Complex()
        c3.realp = self.realp + c2.realp
        c3.imagp = self.imagp + c2.imagp
        return c3
        
def add2Complex(a,b):
    c = a.addComplex(b)
    return c

def main():
    c1 = Complex(3,5)
    c2 = Complex(6,4)
    
    print("Complex Number 1")
    c1.showComplex()
    print("Complex Number 2")
    c2.showComplex()
    
    c3 = add2Complex(c1, c2)

    print("Sum of two Complex Numbers")    
    c3.showComplex()

#Addition of N (N >=2) complex numbers

    compList = []
    
    num = int(input("\nEnter the value for N : "))
    
    for i in range(num):
        print("Object", i+1)
        obj = Complex()
        obj.readComplex()
        compList.append(obj)
    
    print("\nEntered Complex numbers are : ")
    for obj in compList:
        obj.showComplex()
        
    sumObj = Complex()
    for obj in compList:
        sumObj = add2Complex(sumObj, obj)    
    
    
    print("\nSum of N complex numbers is", end = " ")
    sumObj.showComplex()
    
main()
