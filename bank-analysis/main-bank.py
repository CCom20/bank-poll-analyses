import os
import csv

bankcsv_path = os.path.join("Resources", "budget_data.csv")

def fiscal_months(): 
    total_months = [row for row in csvreader]
    print(len(total_months))

def months_profitable():
    profit = [row[1] for rows[1] in csvreader if rows[1] > 0]
    losses = [row[1] for rows[1] in csvreader if rows[1] < 0]
    print(profit)
    print(losses)
    
with open(bankcsv_path, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    fiscal_months()
    months_profitable()