"""
This program makes a data frame for the initial test of activity based on research paper located here:
https://arxiv.org/pdf/1809.04041.pdf
This project will have to train an ML model to create a data set for predictive analysis
"""
import csv
import json
from github import Github, StatsContributor

# Connect to the GitHub api with Username and Password specified in github_api_info.json
with open("github_api_info.json") as read_file:
    user_pass = json.load(read_file)


gh_api = Github(user_pass['Username'], user_pass['Password'])

repo = gh_api.get_repo('itsabot/itsabot')
# Read in the ESEM - Dataset which is the name of 1002 repos and their activity status (archived/FSE are inactive) and
# and active is active
checklist = []
with open('ESEM - Dataset.csv', newline='')as esemdata:
    labeled_data = csv.DictReader(esemdata, delimiter=',')
    for row in labeled_data:
        try:
            repo = gh_api.get_repo(row['Repository'])
            name_of = repo.name
        except:
            name_of = 'n/a'
            checklist.append(row['Repository'])

with open('checklist.txt', 'w') as check_file:
        for item in checklist:
            check_file.write("%s\n" % item)
