import os
import csv

bankcsv_path = os.path.join("Resources", "budget_data.csv")

with open(bankcsv_path, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader: 
        print(row)
