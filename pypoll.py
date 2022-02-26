# total number of votes cast
# a complete list of candidates who received votes
# total number of votes each candidate received
# percentage of votes each candidate won
# the winner of the eletion based on popular vote
# Import the datetime class from the datetime module.
import datetime as dt
from os import listdir
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter to 0
total_votes = 0 

# candidate options
candidate_options = []
# candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row.
    headers = next(file_reader)
# Print each row in the CSV file.
    for row in file_reader:
    # Add to the total vote count.
        total_votes += 1
    # print the candidate name from each row
        candidate_name = row[2]
    # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        # Add it to the list of candidates.
            candidate_options.append(candidate_name)
        # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # add a vote to the candidate's count
        candidate_votes[candidate_name] +=1
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name 
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
