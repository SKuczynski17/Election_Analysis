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
total_votes = 0
#print the candidate name from each row
candidate_options = []
candidate_votes = {}
# winning candidate and winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read and print the header row.
    headers = next(file_reader)
    #print each row in the csv file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        #print the cnadidate name from each row
        candidate_name = row[2]
        #If the cnadidate name does not match any existing candidate....
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #add it to the dictionary as a key
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    #iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrive vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # to do print out each candidates name,vote count and percantage of votes to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #deteming winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidates name
            winning_candidate = candidate_name    
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)  
#print the total votes
print(total_votes)
#print the candidate list.
print(candidate_options)
#print the candidate vote dictionary
print(candidate_votes)





