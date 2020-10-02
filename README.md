# Bank and Poll Analyses

This respository houses two analyses: a **bank financial analysis**, and a **poll analysis**. The files are labled accordingly.

## About the Bank Analysis

The bank analysis looks at 86 months and the change between months which is used to find the average monthly change over those 86 months. 

#### Some note about the CSV Reader
To find the average change between the 1st month and the 2nd month, it was necessary to skip not only the first row (i.e., the "header row") but also the second row (i.e., the first month in the series). This was achieved by employing the `next()` function for both the header and the first row. 

    `csv_header = next(csvreader)`
    `first_row = next(csvreader)`

## About the Poll Analysis