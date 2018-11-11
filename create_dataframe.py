"""
This program makes a data frame for the initial test of activity based on research paper located here:
https://arxiv.org/pdf/1809.04041.pdf
This project will have to train an ML model to create a data set for predictive analysis
"""
import csv
import json

import requests

# Connect to the GitHub api with Username and Password specified in github_api_info.json
with open("github_api_info.json") as read_file:
    user_pass = json.load(read_file)


# Read in the ESEM - Dataset which is the name of 1002 repos and their activity status (archived/FSE are inactive) and
# and active is active
checklist = []
with open('ESEM - Dataset.csv', newline='')as esemdata:
    labeled_data = csv.DictReader(esemdata, delimiter=',')
    """
    with open ('checklist.txt') as text_file:
        c_list =[]
        for row in text_file:
            c_list.append(row.replace('\n', ''))

        for record in labeled_data:
            for x in c_list:
                # print(x, record['Repository'])
                # print(x == record['Repository'])
                if x == record['Repository']:
                    print(record['Repository'], record['Archived'])

    
    for row in labeled_data:
        try:
            repo = gh_api.get_repo(row['Repository'])
            name_of = repo.name
        except:
            name_of = 'n/a'
            checklist.append(row['Repository'])



with open('checklist.txt', 'w') as check_file:
        for item in checklist:
            check_file.write("%s\n" % item)"""


test_repo = 'itsabot/itsabot'.split('/')
print(test_repo)

index = 1
finished = False
data = []
while not finished:
    url = 'https://api.github.com/repos/'+test_repo[0]+'/'+ test_repo[1]+ '/commits?per_page=100&page=' + str(index)
    r = requests.get(url, auth=(user_pass['Username'], user_pass['Password']))
    print(r.json())
    if r.json() == []:
        finished = True
    else:
        data = data + r.json()
    index += 1



with open('test2.json', 'w') as json_test:
    json.dump(data, json_test)
