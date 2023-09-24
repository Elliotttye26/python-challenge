import pandas as pd
from pathlib import Path
import os

#Pull in dataset
election_data = r"C:\Users\ellio\Documents\github\python-challenge\PyPoll\Resources\election_data.csv"

#read the dataset
df = pd.read_csv(election_data)

#The total number of votes cast
df["Ballot ID"].unique

len(df.columns)

#total votes cast
total_votes =len(df)
total_votes

#votes cast per candidate
candidates_count =df["Candidate"].value_counts()
candidates_count

#The percentage of votes each candidate won
percentage_votes = (candidates_count/total_votes)*100
percentage_votes

#The winner of the election based on popular vote
candidate_winner = candidates_count.idxmax()
candidate_winner

#analysis
print("Election Results:")
print("------------------------")
print("Total Votes:", total_votes)
print("------------------------")
print(percentage_votes)
print("------------------------")
print("Winner:", candidate_winner)


#create a text file with results
output_file = r"C:\Users\ellio\Documents\github\python-challenge\PyPoll\analysis\Results.txt"

with open(output_file, "w") as results:
    results.write("Election Results:  \n")
    results.write("------------------------ \n")
    results.write("Total Votes: " + str(total_votes) + "\n")
    results.write("------------------------ \n")
    results.write(str(percentage_votes) + "\n")
    results.write("------------------------ \n")
    results.write("Winner: " + str(candidate_winner) + "\n")