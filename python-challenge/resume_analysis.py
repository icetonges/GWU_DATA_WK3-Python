# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:32:10 2019

@author: dbs2019
"""

# -*- coding: UTF-8 -*-

import os
import string

# Counter is used later in the program
from collections import Counter

# Paths
resume_path = os.path.join(".", "Resources", 'resume.md')

# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}

# function to load a file
def load_file(filepath):
    """Helper function to read a file and return the data."""
    with open(filepath, "r") as resume_file_handler:
        return resume_file_handler.read().lower().split()

# Grab the text for a Resume
word_list = load_file(resume_path)

# Create a set of unique words from the resume
resume = set()

# Remove trailing punctuation from words
for token in word_list:
    resume.add(token.split(',')[0].split('.')[0])

# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
resume = resume - punctuation
print(resume)

# Calculate the Required Skills Match using Set Intersection
print("REQUIRED SKILLS")
print("=============")
print(resume & REQUIRED_SKILLS)


# Calculate the Desired Skills Match using Set Intersection
print("DESIRED SKILLS")
print("=============")
print(resume & DESIRED_SKILLS)

# Clean Stop Words

from nltk.corpus import stopwords
filtered_word_list = word_list[:] #make a copy of the word_list
for word in word_list: # iterate over word_list
  if word in stopwords.words('english'): 
    filtered_word_list.remove(word) # remove word from filtered_word_list if it is a stopword

# Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(filtered_word_list, 0)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# Loop through the word list and count each word.
for word in filtered_word_list:
    word_count[word] += 1
print(word_count)
print("***********************************")
# Using collections.Counter
word_counter = Counter(filtered_word_list)
print(word_counter)

# Comparing both word count solutions
print(word_count == word_counter)

# Top 10 Words
print("Top 10 Words")
print("=============")

# Don't worry about the underscore in front of _word_count
# It is just convention for internal use only
# More info here: https://dbader.org/blog/meaning-of-underscores-in-python
_word_count = dict()
for line in filtered_word_list:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in _word_count:
            _word_count[word] =1
        else:
            _word_count[word] += 1

_word_counter = Counter(_word_count)
sorted_words = _word_counter.most_common()[:10]
print(sorted_words) 