import os
import csv

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
    print(f"{names[0]}: {percent_votes_khan}% (Total Votes: {len(votes['Khan'])})")
    print(f"{names[1]}: {percent_votes_correy}% (Total Votes: {len(votes['Correy'])})")
    print(f"{names[2]}: {percent_votes_li}% (Total Votes: {len(votes['Li'])})")
    print(f"{names[3]}: {percent_votes_tooley}% (Total Votes: {len(votes['Tooley'])})")
    print("-------------------")
    print(f"Winner: {winner}")
    print("-------------------")

# Set Variables, Dictionaries, and Lists that we will be usings / appending to
total_votes = 0
winner_votes = 0
candidate_votes = []
names = []
votes = {"Khan": [], 
    "Correy": [], 
    "Li": [], 
    "Tooley": []}
winner = ""

# Read CSV and start For-Loop to go through, read and append as appropriate
with open(polldata_path, mode='r', newline='') as polldata:
    csvreader = csv.reader(polldata, delimiter=',')
    polldata_header = next(csvreader)

    for row in csvreader: 
        total_votes += 1

        # Add name to names.list - Not necessary for this, but larger datasets will require a way to check all unique values, so I included this
        if row[2] not in names:
            names.append(row[2])

        #Go through for-loop and append voter id to key-value in dictionary, then read the length of the list for an integer and calculate percentage of votes
        if row[2] == "Khan":
            votes["Khan"].append(row[0])
            percent_votes_khan = round(100 * (len(votes["Khan"]) / total_votes), 3)
        elif row[2] == "Correy":
            votes["Correy"].append(row[0])
            percent_votes_correy = round(100 * (len(votes["Correy"]) / total_votes), 3)
        elif row[2] == "Li":
            votes["Li"].append(row[0])
            percent_votes_li = round(100 * (len(votes["Li"]) / total_votes), 3)
        elif row[2] == "O'Tooley":
            votes["Tooley"].append(row[0])
            percent_votes_tooley = round(100 * (len(votes["Tooley"]) / total_votes), 3)

    #Check for winner by updating winner_votes and winner = ""
    if len(votes["Khan"]) > winner_votes:
        winner_votes = len(votes["Khan"])
        winner = "Khan"
    elif len(votes["Correy"]) > winner_votes:
        winner_votes = len(votes["Correy"])
        winner = "Correy"
    elif len(votes["Li"]) > winner_votes:
        winner_votes = len(votes["Li"])
        winner = "Li"       
    elif len(votes["Tooley"]) > winner_votes:
        winner_votes = len(votes["Tooley"])
        winner = "O'Tooley"

    print_results()

# Export results as txt file
with open(pollout_path, mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["-------------------"])
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow([f"Candidates Running: {names[0]}, {names[1]}, {names[2]}, {names[3]}"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow([f"{names[0]}: {percent_votes_khan}% (Total Votes: {len(votes['Khan'])})"])
    csvwriter.writerow([f"{names[1]}: {percent_votes_correy}% (Total Votes: {len(votes['Correy'])})"])
    csvwriter.writerow([f"{names[2]}: {percent_votes_li}% (Total Votes: {len(votes['Li'])})"])
    csvwriter.writerow([f"{names[3]}: {percent_votes_tooley}% (Total Votes: {len(votes['Tooley'])})"])
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------"])
