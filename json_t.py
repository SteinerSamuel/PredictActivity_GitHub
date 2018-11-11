import json
import csv

labeled_data = []

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
""""
with open("test2.json") as json_test:
    data = json.load(json_test)
y = 0
for x in data:
    y+=1
    print(y)
    print(x)
"""
