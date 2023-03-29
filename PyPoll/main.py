import csv 
import os

#os for other systems
filepath = os.path.join("Resources", "election_data.csv")

#Read file
with open(filepath) as csv_file:
    csvreader=csv.reader(csv_file, delimiter=",")
    header=next(csvreader)

#List Variables
    ID = []
    Candidates = []
    
    #Find info
    for row in csvreader:

        ID.append((row[0]))
        Candidates.append((row[2]))

#List Candidates to find vote data
unique_candidates = []
for i in Candidates:
    if i not in unique_candidates:
        unique_candidates.append(i)

#print(unique_candidates)

charles = 0
diana = 0
raymon = 0

for name in Candidates:
    if name == "Charles Casper Stockham":
        charles =  charles + 1  

    elif name == "Diana DeGette":
        diana = diana + 1

    else: raymon = raymon + 1 

#print(charles)
#print(diana)
#print(raymon)

#Find % of popular votes
Total_Votes = (int)(charles) + (int)(diana) + (int)(raymon)
#print(Total_Votes)

charles_percentage = round((charles / Total_Votes) *100, 1)
diana_percentage = round((diana / Total_Votes) *100, 1)
raymon_percentage = round((raymon / Total_Votes) *100, 1)

#print(charles_percentage)
#print(diana_percentage)
#print(raymon_percentage)

#Find Winner
winner = max(charles, diana, raymon)
winnerpercentage = max(charles_percentage, diana_percentage, raymon_percentage)
#print (str(winner))

Vote = [charles, diana, raymon]
percentages = [charles_percentage, diana_percentage, raymon_percentage]

winning_candidate = (unique_candidates[Vote.index(winner)])
winningpercentage = (percentages[Vote.index(winner)])


#output
with open("output.txt", "w") as txt_file:

    text = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winner:,}\n"
        f"Winning Percentage: {winningpercentage:.1f}%\n"
        f"-------------------------\n")
    print(text)
    txt_file.write(text)

   # txt_file.write("Election Results")
    #txt_file.write("\n") 
    #txt_file.write("----------------")
    #txt_file.write("\n")
    #txt_file.write("Total Votes" ":")
    #txt_file.write(str(Total_Votes))
    #txt_file.write("\n")
    #txt_file.write("----------------")
    #txt_file.write("\n")
    #txt_file.write("Charles Casper Stackham" ":")
    #txt_file.write(str(charles))
    #txt_file.write(str(charles_percentage))
    #txt_file.write("\n")
    #txt_file.write(str(winner))
    #txt_file.write("\n")
    #txt_file.write("----------------")
    #txt_file.write("\n")
    