# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:36:37 2019

@author: dbs2019
"""


import os
import csv

# Variables
total_vote = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0

# Set Path For File
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:

    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvfile)

    # Read Each Row Of Data After The Header
    for row in csvreader:
        
        # Calculate Total Number Of Votes Cast
        total_vote += 1
        
        # Calculate Total Number Of Votes Each Candidate Won
        if (row[2] == "Khan"):
            khan_vote += 1
        elif (row[2] == "Correy"):
            correy_vote += 1
        elif (row[2] == "Li"):
            li_vote += 1
        else:
            otooley_vote += 1
            
    # Calculate Percentage Of Votes Each Candidate Won
    kahn_percent = khan_vote / total_vote
    correy_percent = correy_vote / total_vote
    li_percent = li_vote / total_vote
    otooley_percent = otooley_vote / total_vote
    
    winner = max(khan_vote, correy_vote, li_vote, otooley_vote)

    if winner == khan_vote:
        winner_name = "Khan"
    elif winner == correy_vote:
        winner_name = "Correy"
    elif winner == li_vote:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_vote}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%}({khan_vote})")
print(f"Correy: {correy_percent:.3%}({correy_vote})")
print(f"Li: {li_percent:.3%}({li_vote})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_vote})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Specify File To Write To
output_file = os.path.join('.', 'Resources', 'election_data_revised.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Election Result\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Vote: {total_vote}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_vote})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_vote})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_vote})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_vote})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")