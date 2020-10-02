# Bank and Poll Analyses

This respository houses two analyses: a **bank financial analysis**, and a **poll analysis**. The files are labled accordingly.

## About the Bank Analysis

The bank analysis looks at 86 months and the change between months which is used to find the average monthly change over those 86 months. 

**Folders and Files**
1. bank-analysis 
    + analysis 
        + bank_analysis.txt
    + resources (contains csv reference)
        + budget_data.csv 
2. main.py 

### About the Code
To find the average change between the 1st month and the 2nd month, it was necessary to skip not only the first row (i.e., the "header row") but also the second row (i.e., the first month in the series). This was achieved by employing the `next()` function for both the header and the first row. 

    csv_header = next(csvreader)
    first_row = next(csvreader)

Using `first_row = next(csvreader)` allows the calculation between the 3rd row and 2nd row in the start of the series to find the change between months.

    total_profits = int(first_row[1])
    total_months = 1
    previous_month = int(first_row[1]) 

The rest of the calculations take place within the for-loop. The loop simply adds 1 for every month, totals the profits, calculates the change, resets the `previous_month` variable, and then appends the change to a list. 

    for row in csvreader:
        total_months += 1
        total_profits += int(row[1])
        change = int(row[1]) - previous_month
        previous_month = int(row[1])
        net_change.append(change)

Still inside the for-loop, we go through `if` statements to check for months of greatest increase (`greatest_increase`) and greatest decrease (`greatest_decrease`). Then, stepping out of the loop, we calculate the average change. 

        if change > greatest_increase:
            greatest_increase = change
            increase_month = row[0]
        elif change < greatest_decrease:
            greatest_decrease = change
            decrease_month = row[0]

    # Find the average of the changes
    average = round( sum(net_change) / len(net_change), 2)

After this, the CSV writer simply exports a `.txt` file and runs a function to print the analysis. 

## About the Poll Analysis

The poll analysis looks at a small-town election and determines the total votes, votes for each candidate, as well as the percentage of votes for each candidate. Some code is added to automate more of the process, but it isn't necessary for this dataset. I included to practice writing for scalability. 

**Folders and Files**

1. poll-analysis 
    + analysis 
        + election_summary.txt
    + Resources
        + election_data.csv 
2. main.py 

### About the Code

Starting simply, I employed the use of skipping the first row with `next(csvreader)`. Using the `total_votes` variable, the for-loop adds 1 for every row, yeilding the total number of votes for the election. 

Within the for-loop, the first `if` statement is part of the optional code. I used this to find all the names of every candidate running in the election, and appended all unique names to the `names = []` list. 

        if row[2] not in names:
            names.append(row[2])

Again, the above code isn't necessary since the names of the candidates are already known. However, I figured this allows code to be reused in following elections, as it allows the list of names to be printed out or referenced based on index number. 

After this, the rest of the `if` statements look matching names. While I could have calculated the percentage of votes within each `if`, I figured calculations outside the for-loop would run a bit faster by simply storing the matching name to a numeric variable. 

        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            tooley_votes += 1

Once the votes are counted, the rest of the code simply calculates the percentages and checks for the winner: 

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

Instead of `winner = ""`, the `name[0]` or relative index could be referenced. However, the index number might not always been known. I had this prior to the string-matching, but decided for ease of knowing what the code is doing to switch it.

As with the bank analysis, the csv writer exports this as a `.txt` file. 