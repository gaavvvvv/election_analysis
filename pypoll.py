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

# Open the election results and read the file
with open(file_to_load) as election_data:
# To do: read and analyze the data here
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row.
    headers = next(file_reader)
    print(headers)


