#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:21:12 2022

05WordFreq.py

Develop a program to print 10 most frequently appearing words in a text file. [Hint: Use dictionary
with distinct words and their frequency of occurrences. Sort the dictionary in the reverse order of
frequency and display dictionary slice of first 10 items]

@author: Prabodh C P
"""
import sys
import string
import os.path


fname = input("Enter the filename : ")      #sample file text.txt also provided


if not os.path.isfile(fname):
    print("File", fname, "doesn't exists")
    sys.exit(0)

infile = open(fname, "r")

filecontents = ""

for line in infile:
    for ch in line:
        if ch not in string.punctuation:
            filecontents = filecontents + ch
        else:
            filecontents = filecontents + ' '   #replace punctuations and newline with a space
            
wordFreq = {}

wordList = filecontents.split()

#Calculate word Frequency

for word in wordList:
    if word not in wordFreq.keys():
        wordFreq[word] = 1
    else:
        wordFreq[word] += 1
        
# print(wordFreq)
        
# for word, frequency in wordFreq.items():
#     print(word, "occurs", frequency, "times")

#Sort Dictionary based on values in descending order
sortedWordFreq = sorted(wordFreq.items(), key=lambda x:x[1], reverse=True )

# print(type(sortedWordFreq))

# print(sortedWordFreq)

#Display 10 most frequently appearing words with their count

print("\n===================================================")
print("10 most frequently appearing words with their count")
print("===================================================")
for i in range(10):
    print(sortedWordFreq[i][0], "occurs", sortedWordFreq[i][1], "times")
