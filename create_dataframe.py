"""
This program makes a data frame for the initial test of activity based on research paper located here:
https://arxiv.org/pdf/1809.04041.pdf
This project will have to train an ML model to create a data set for predictive analysis
"""
import csv
import json
import json_t as dm
import requests
import pandas


def get_Git_data(user_pass, url):
    index = 1
    finished = False
    data = []
    while not finished:
        url_index = url + str(index)
        r = requests.get(url_index, auth=(user_pass['Username'], user_pass['Password']))
        print(r.json())
        if r.json() == []:
            finished = True
        else:
            data = data + r.json()
        index += 1

    return data

# Connect to the GitHub api with Username and Password specified in github_api_info.json
with open("github_api_info.json") as read_file:
    user_pass = json.load(read_file)

# Read in the ESEM - Dataset which is the name of 994 repos and their activity status (archived/FSE are inactive) and
# and active is active
Data_frame = {'Repository':[], 'Status':[]}
with open('ESEM - Dataset.csv', newline='')as esemdata:
    labeled_data = csv.DictReader(esemdata, delimiter=',')
    for x in labeled_data:
        Data_frame['Repository'] += [x['Repository']]
        Data_frame['Status'] += [x['Status']]

months = 24
interval = 3




