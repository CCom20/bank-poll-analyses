import os
import csv

# Set read and output paths
bankcsv_path = os.path.join("resources", "budget_data.csv")
analysis_path = os.path.join("analysis", "bank_analysis.txt")

# Set function for printing analysis
def print_analysis():
    print("Financial Analysis"),
    print("------------------------------"),
    print(f"Total Months: {total_months}"),
    print(f"Total: {total_profits}"),
    print(f"Average Change: {average}"),
    print(f"Greatest increase in profits: {increase_month} ${greatest_increase}"),
    print(f"Greatest decrease in profits: {decrease_month} ${greatest_decrease}"),
    print("------------------------------")

# Set and define variables for use when reading the document
total_months = 0
total_profits = 0
greatest_increase = 0
greatest_decrease = 0
increase_month = ""
decrease_month = ""
net_change = []

# Read the CSV and go through for-loop to calculate change
with open(bankcsv_path, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)

    # Set total_profits to the first_row since we skipped the first month, 
    # but we need that to calculate average between 1st and 2nd month:
    # increase total months to 1, and set previous month to first_row
    total_profits = int(first_row[1])
    total_months = 1
    previous_month = int(first_row[1]) 

    # Move through months/values in for-loop and calculate monthly change
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
    print_analysis()

with open(analysis_path, mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Average Change: {average}"])
    csvwriter.writerow([f"Greatest increase in profits: {increase_month} ${greatest_increase}"])
    csvwriter.writerow([f"Greatest decrease in profits: {decrease_month} ${greatest_decrease}"])