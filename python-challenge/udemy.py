import os
import csv

udemy_csv = os.path.join("..","Resources","web_starter.csv")

title = []
price = []
subscribers = []
reviews = []
percent = []
length = []

with open(udemy_csv, encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # loop through
    for row in csvreader:
        
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        #length.append(row[9])
        percent_cacu = (int(row[6])/int(row[5]))
        percent.append(round(percent_cacu,2))
        length_r = row[9].split(" ")
        length.append(length_r[0])

zipped_data = zip(title, price, subscribers, reviews, percent, length) 

output_file = os.path.join("Peter_web_final.csv")

with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)
        
        writer.writerow(["Title","Price","Subscribers","Reviews", "Percent", "Length"])
        writer.writerows(zipped_data)