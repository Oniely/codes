import csv

titles = dict()

with open("csv/testing.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Employee Markme"].strip().upper()      
        if not title in titles:
            titles[title] = 0
        titles[title] += 1

def get_value(title):
    return titles[title]   

for title in sorted(titles, key=get_value, reverse=True):  
    print(title, titles[title])