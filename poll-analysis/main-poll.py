import os
import csv

polldata_path = os.path.join("Resources", "election_data.csv")

total_votes = []
candiate_votes = {
    ""
}
unique_candidates = []


with open(polldata_path, mode='r', newline='') as polldata:
    csvreader = csv.reader(polldata, delimiter=',')
    csv_header = next(csvreader)

    for row in polldata: 
        total_votes.append(row)
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
    
    print(len(total_votes))
    print(unique_candidates)

    #for row in polldata:
       #print(row)