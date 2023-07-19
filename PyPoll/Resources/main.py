import csv
import os

#import and export file
file_to_load = "C:/Users/shaji/OneDrive/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv"
File_to_output = "C:/Users/shaji/OneDrive/Documents/GitHub/python-challenge/PyPoll/Analysis/election_results.csv"

#variables
total_votes= 0
candidates_votes = {}
winner_candidates = ""
winner_votes = 0

#open file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    next(reader)

# Calculations
    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name in candidates_votes:
            candidates_votes[candidate_name] += 1
        else:
            candidates_votes[candidate_name] = 1

        if candidates_votes[candidate_name] > winner_votes:
                winner_candidate = candidate_name
                winner_votes = candidates_votes[candidate_name]

# Results
output = (
     f"\nElection Results\n"
     f"------------------\n"
     f"Total Votes: {total_votes}\n"
     f"----------\n"
)

for candidate, votes in candidates_votes.items():
    vote_percentage = (votes / total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

output += (
     f"------------------\n"
     f"Winner: {winner_candidate}\n"
     f"-----------------\n"

)

print(output)

with open(File_to_output, "w") as txt_file:
     txt_file.write(output)
