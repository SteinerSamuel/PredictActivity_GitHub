"""
This program makes a data frame for the initial test of activity based on research paper located here:
https://arxiv.org/pdf/1809.04041.pdf
This project will have to train an ML model to create a data set for predictive analysis
"""
import csv
from github import Github


# Read in the ESEM - Dataset which is the name of 1002 repos and their activity status (archived/FSE are inactive) and
# and active is active
with open('ESEM - Dataset.csv', newline='')as esemdata :
    labeled_data = csv.reader(esemdata, delimiter=',')
    count = 0
    for row in labeled_data:
        if row[1] == 'FSE' or row[1] == 'Archived':
            count += 1
            row[1] = 'inactive'
            print(row)
    print(count)
