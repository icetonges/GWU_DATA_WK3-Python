# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 18:08:12 2019

@author: dbs2019
"""

import os
import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
dataFileList = ["employee_data.csv"]

for file in dataFileList:
    csvpath = os.path.join("Resources",file)
    formattedCsvpath = os.path.join("Resources","new_"+file)
    with open(formattedCsvpath,'w',newline='') as formattedCsvfile:
        csvwriter = csv.writer(formattedCsvfile)
        csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
        with open(csvpath, newline='') as csvfile:
            csvfile.readline()
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                empID = row[0]
                empName = row[1]
                empDOB = row[2]
                empSSN = row[3]
                empState = row[4]

            
                splitName = empName.split()
                empFirstName = splitName[0]
                empLastName = splitName[1]

                splitDOB =  empDOB.split("-")
                year = splitDOB[0]
                month = splitDOB[1]
                day = splitDOB[2]
                formattedDOB = month + "/" + day + "/" + year
                formattedSSN = "***-**-" + empSSN.split("-")[2]
                abbrState = us_state_abbrev.get(empState)            
                csvwriter.writerow([empID,empFirstName,empLastName,formattedDOB,formattedSSN,abbrState])
                print(str([empID,empFirstName,empLastName,formattedDOB,formattedSSN,abbrState]))
    formattedCsvfile.close()