import os
import csv

bankcsv_path = os.path.join("Resources", "budget_data.csv")

def fiscal_months(): 
    total_months = [row for row in csvreader]
    print(len(total_months))

def months_profitable():
    
    
with open(bankcsv_path, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    fiscal_months()