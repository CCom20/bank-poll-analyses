import os
import csv

# Set read and output paths
polldata_path = os.path.join("Resources", "election_data.csv")
pollout_path = os.path.join("analysis", "election_summary.txt")

# Define the print function for Election Results 
def print_results():
    print("-------------------")
    print("Election Results")
    print("-------------------")
    print(f"Total Votes: {total_votes}")
    print(f"Candidates Running: {names[0]}, {names[1]}, {names[2]}, {names[3]}")
    print("-------------------")
    print(f"{names[0]}: {percent_votes_khan}% (Total Votes: {khan_votes})")
    print(f"{names[1]}: {percent_votes_correy}% (Total Votes: {correy_votes})")
    print(f"{names[2]}: {percent_votes_li}% (Total Votes: {li_votes})")
    print(f"{names[3]}: {percent_votes_tooley}% (Total Votes: {tooley_votes})")
    print("-------------------")
    print(f"Winner: {winner}")
    print("-------------------")

# Set Variables, Dictionaries, and Lists that we will be usings / appending to
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0
total_votes = 0
winner_votes = 0
candidate_votes = []
names = []
winner = ""

# Read CSV and start For-Loop to go through and calculate votes
with open(polldata_path, mode='r', newline='') as polldata:
    csvreader = csv.reader(polldata, delimiter=',')
    polldata_header = next(csvreader)

    for row in csvreader: 
        total_votes += 1

        # Add name to names.list - Not necessary for this, but larger datasets will require a way to check all unique values, so I included this
        if row[2] not in names:
            names.append(row[2])

        #Go through for-loop and add to each candidates' total vote count
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            tooley_votes += 1

    #Calculate percentages for each candidate
    percent_votes_khan = round(100 * (khan_votes/ total_votes), 3)
    percent_votes_correy = round(100 * (correy_votes / total_votes), 3)
    percent_votes_li = round(100 * (li_votes / total_votes), 3)
    percent_votes_tooley = round(100 * (tooley_votes / total_votes), 3)

    #Check for winner by updating winner_votes and winner = ""
    if khan_votes > winner_votes:
        winner_votes = khan_votes
        winner = "Khan"
    elif correy_votes > winner_votes:
        winner_votes = correy_votes
        winner = "Correy"
    elif li_votes> winner_votes:
        winner_votes = li_votes
        winner = "Li"       
    elif tooley_votes > winner_votes:
        winner_votes = tooley_votes
        winner = "O'Tooley"

# Export results as txt file
with open(pollout_path, mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["-------------------"])
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow([f"Candidates Running: {names[0]}, {names[1]}, {names[2]}, {names[3]}"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow([f"{names[0]}: {percent_votes_khan}% (Total Votes: {khan_votes})"])
    csvwriter.writerow([f"{names[1]}: {percent_votes_correy}% (Total Votes: {correy_votes})"])
    csvwriter.writerow([f"{names[2]}: {percent_votes_li}% (Total Votes: {li_votes})"])
    csvwriter.writerow([f"{names[3]}: {percent_votes_tooley}% (Total Votes: {tooley_votes})"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------"])

    print_results()