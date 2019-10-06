# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:29:35 2019

@author: dbs2019
"""

import re
import os
fileList = ["paragraph_1.txt","paragraph_2.txt"]
for file in fileList:
    txtpath = os.path.join("raw_data",file)
    with open(txtpath, 'r') as text:   
        lines = text.read()
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', lines)
        words = re.split(r' ', lines)                    
        letterCount = 0
        for word in words:
            letterCount = letterCount + len(word)
        outputpath = os.path.join("raw_data",file.split(".")[0] + "_result.txt")

        filelines = []
    
        newfile = open(outputpath, "w")
    
        filelines.append("Paragraph Analysis")
        filelines.append("-----------------")
        filelines.append("Approximate Word Count:: "+str(len(words)))
        filelines.append("Approximate Sentence Count: "+str(len(sentences)))
        filelines.append("Average letter count: "+ str(round(letterCount/len(words),2)))
        filelines.append("Average Sentence Length: "+ str(round(len(words)/len(sentences),2)))
        for line in filelines:
            print(line)
            print(line,file=newfile)
        print()
        newfile.close()
