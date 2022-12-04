import csv

titles = set()

with open("csv/testing.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Employee Markme"].strip().upper()      
        titles.add(title)

#sorting csv or set from a-z
for title in sorted(titles):  
    print(title)