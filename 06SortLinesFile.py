#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:14:27 2022

06SortLinesFile.py

Develop a program to sort the contents of a text file and write the sorted contents into a separate text
file. [Hint: Use string methods strip(), len(), list methods sort(), append(), and file methods open(),
readlines(), and write()].

@author: Prabodh C P
"""

import os.path
import sys

fname = input("Enter the filename whose contents are to be sorted : ")      #sample file unsorted.txt also provided

if not os.path.isfile(fname):
    print("File", fname, "doesn't exists")
    sys.exit(0)

infile = open(fname, "r")

myList = infile.readlines()
# print(myList)

#Remove trailing \n characters
lineList = []
for line in myList:
    lineList.append(line.strip())

lineList.sort()

#Write sorted contents to new file sorted.txt

outfile = open("sorted.txt","w")


for line in lineList:
    outfile.write(line + "\n")

infile.close()  # Close the input file
outfile.close() # Close the output file

    
if os.path.isfile("sorted.txt"):
    print("\nFile containing sorted content sorted.txt created successfully")
    print("sorted.txt contains", len(lineList), "lines")
    print("Contents of sorted.txt")
    print("=================================================================")
    rdFile = open("sorted.txt","r")
    for line in rdFile:
        print(line, end="")
