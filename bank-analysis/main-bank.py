import os
import csv

bankcsv_path = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_profits = 0
greatest_increase = 0
greatest_decrease = 0
increase_month = ""
decrease_month = ""
net_change = []


# def months_profitable():
#     profit_list = []
#     profit = [row[1] for row in csvreader if int(row[1]) > 0]
#     profit_list.append(profit)
#     #losses = [row for row[1] in csvfile if row[1] < 0]
#     print(profit_list)
#     #print(losses)
    
with open(bankcsv_path, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)

    total_profits = int(first_row[1])
    total_months = 1
    previous_month = int(first_row[1]) 

    for row in csvreader:
        total_months += 1
        total_profits += int(row[1])
        change = int(row[1]) - previous_month
        previous_month = int(row[1])
        net_change.append(change)
        if change > greatest_increase:
            greatest_increase = change
            increase_month = row[0]
        elif change < greatest_decrease:
            greatest_decrease = change
            decrease_month = row[0]

    average = sum(net_change) / len(net_change)

print(total_months,
    total_profits,
    greatest_increase,
    greatest_decrease,
    increase_month,
    decrease_month,
    net_change,
    average)
