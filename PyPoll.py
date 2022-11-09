#Open the Dataset
#Sum the total number of votes cast
 #Print the names of each candidate who received a vote
#Sum the total votes casted for each candidate 
#Divide the total number of votes for each candidate by the total number of votes for the election
#Rank the highest percentages of number of votes divided bt total number of votes in order from highest to lowest to show the winner
#Print the list of winners ranked and their respective percentages & total votes

import csv
import os

#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable to save the file path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read and print the header row.
    headers = next(file_reader)
    print(headers)





