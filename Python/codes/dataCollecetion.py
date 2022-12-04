import csv

titles = []

with open("csv/testing.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Employee Markme"].strip().upper()      #strip or erase whitespace left and right and then force everything to uppercase
        if not title in titles:         #if title is not in the titles list then add it on the list(append)
            titles.append(title)        #to filter Duplicates

for title in titles:        
    print(title)