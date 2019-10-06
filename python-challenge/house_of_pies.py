# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:22:22 2019

@author: dbs2019

"""
#initial count for pie bought
pie_purchase = [0,0,0,0,0,0,0,0,0,0]

# start pie order intake

pie_n_order = "y"


#create list for pie 
pie_list = ["(1) Pecan", "(2) Apple Crisp", "(3) Bean", "(4) Banoffee",  "(5) Black Bun", "(6) Blueberry", "(7) Buko", "(8) Burek",  "(9) Tamale", "(10) Steak"]
 
print(pie_list)
 
while pie_n_order == "y":
    
    pie_order = input('which pie you would like to order?\n')
    
    customer_order = pie_list[int(pie_order)-1]
    
    pie_purchase[int(pie_order)-1] = pie_purchase[int(pie_order)-1] + 1
    
    print('Great! We will have that ' + customer_order + 'right out for you.')
    
    pie_n_order = input('Do you want to make another order: (y)es or (n)o?\n')

    # print(pie_purchase)

print(pie_purchase)

for pie_index in range(len(pie_list)):
    
    print(str(pie_purchase[pie_index]) + " " + str(pie_list[pie_index]))