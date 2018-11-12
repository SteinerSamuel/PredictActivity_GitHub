import json
import datetime
import csv

labeled_data = []

"""
with open('ESEM - Dataset.csv', newline='')as esemdata:
    labeled_data = csv.DictReader(esemdata, delimiter=',')

    active = 0
    FSE = 0
    Archived = 0

    for x in labeled_data:
        if x['Status'] == "Active":
            active += 1
        elif x['Status'] == "Archived":
            Archived += 1
        else:
            FSE += 1

print(active)
print(FSE)
print(Archived)
"""
with open("commit_test.json") as json_test:
    data = json.load(json_test)
y = 0
datet = datetime.datetime.strptime('1996-12-31', '%Y-%m-%d'
                                   )
for x in data:
    datestr = x['commit']['author']['date'].split('T')[0]
    newdate = datetime.datetime.strptime(datestr, '%Y-%m-%d')
    if newdate > datet:
        datet = newdate

print(datet)

dates = []
i = 8
while i > 0:
    dates += dates + datet.timedelta(days=-31*i)
    i -= 1

print(dates)