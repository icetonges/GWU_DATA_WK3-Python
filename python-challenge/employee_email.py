#GWU_DATA_WK3-Python/python-challenge/employee_email.py /
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:31:25 2019

@author: dbs2019
"""

import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []
first_name = []
last_name = []
ssn = []
data_dict = {}

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # YOUR CODE HERE
        first_name = (row['first_name'])
        last_name = (row['last_name'])
        ssn = (row['ssn'])
        email = first_name + "." + last_name + '@example.com'
        
        #print(row['first_name'])
        #print(email)
        data_dict = {'first_name':first_name,'last_name':last_name, 'ssn':ssn, 'email':email}
        
        new_employee_data.append(data_dict)
        
        #print(data_dict)
#print(new_employee_data)

        #print(first_name)

f = open("employees.csv", "w")
writer = csv.DictWriter(f, fieldnames = ["first_name", "last_name", "ssn","email"], lineterminator='\n')
writer.writeheader()
writer.writerows(new_employee_data)
f.close()
