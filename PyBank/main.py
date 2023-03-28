import csv
import os

#os for other systems
file_path = os.path.join("Resources", "budget_data.csv")

#open and format file
with open (file_path) as csv_file:
    csvreader=csv.reader(csv_file, delimiter=",")
    header=next(csvreader)


#list variables 
    totalmonths = 0
    PnL = []
    PnLsum = 0
    Avgchanges = []
    Avgchangessum = 0
    greatestchange = ""
    lowestchange = ""
    Dates = []
    greatestchangeindex = 0
    lowestchangeindex = 0

#find total months 
    for row in csvreader:
        totalmonths += 1 
        Dates.append(row[0])

#find profit and losses
        PnL.append(int((row[1])))

    for number in PnL:
        PnLsum += number

 #greatest and lowest changes   
    for i in range(len(PnL)-1):
        Avgchanges.append(PnL[i+1]-PnL[i])   

    greatestchange = max(Avgchanges)
    lowestchange = min(Avgchanges)

    for i in range(len(Avgchanges)):
        Avgchangessum += Avgchanges[i]
        if Avgchanges[i] >= greatestchange:
            greatestchangeindex = i
            
        else:
            greatestchangeindex = 2
    
    print(Avgchanges[i])

 #print results
print(PnLsum)
print(totalmonths)
print(round(Avgchangessum/len(Avgchanges),2))
print(greatestchange)
print(lowestchange)
print(Dates[greatestchangeindex])
print(Dates[lowestchangeindex])

