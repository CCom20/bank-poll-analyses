import os
import csv

polldata_path = os.path.join("Resources", "election_data.csv")

total_votes = []
candidate_votes = []
unique_candidates = []
votes = {"Khan": [], 
    "Correy": [], 
    "Li": [], 
    "O'Tooley": []}
votes_khan = []
votes_correy = []
votes_li = []
votes_otooley = []

with open(polldata_path, mode='r', newline='') as polldata:
    csvreader = csv.reader(polldata, delimiter=',')
    polldata_header = next(csvreader)

    percent_vote = 0

    for row in csvreader: 
        total_votes.append(row[0])
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
        if row[2] == "Khan":
            votes.append[0]
            # votes_khan.append(row[0])
            percent_votes_khan = round(100 * (len(votes_khan) / len(total_votes)), 2)
        elif row[2] == "Correy":
            votes_correy.append(row[0])
        elif row[2] == "Li":
            votes_li.append(row[0])
        elif row[2] == "O'Tooley":
            votes_otooley.append(row[0]) 
        
print(f"Candidates Running: {unique_candidates[0]}, {unique_candidates[1]}, {unique_candidates[2]}, {unique_candidates[3]}")
print(f"Total Votes Cast: {len(total_votes)}")
print(len(votes_khan))
print(percent_votes_khan)
print(len(votes_correy))
print(len(votes_li))
print(len(votes_otooley))