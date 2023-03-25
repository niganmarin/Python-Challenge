import csv
import os

file_path = "C:\Users\nigan\python-challenge\PyBank\Resources\budget_data.csv"

with open(file_path) as csv_file:
    csvreader=csv.reader(csv_file, delimiter=",")
    header=next(csvreader)
    print(file_path)

#list variables 
    totalmonths = 0
    

    for row in csvreader:
        totalmonths += 1 
        #totalmonths.count((row[0]))
print(totalmonths)


    #PnL = []
    #for row in csvreader:
     #   PnLtotal = (int)((row[1])).sum()

       

#    for row in csvreader:
 #       totalmonths.append((row[1]))

#unique_months = [totalmonths]
#for i in totalmonths:
 #   if i not in unique_months:
  #      totalmonths.append(i)

   #     print(unique_months)
