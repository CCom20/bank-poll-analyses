import os
import csv

polldata_path = os.path.join("Resources", "election_data.csv")

with open(polldata_path, mode='r', newline='') as polldata:
    csvreader = csv.reader(polldata, delimiter=',')
    csv_header = next(csvreader)

    #for row in polldata:
       #print(row)