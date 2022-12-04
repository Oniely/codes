import csv

# dictionary data collection
# counting how many duplicate a title has
# and sorting them into the highest value
# hence the reverse=True
titles = dict()

with open("csv/testing.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Employee Markme"].strip().upper()      
        if not title in titles:
            titles[title] = 0
        titles[title] += 1

# lambda 1 liner function if you dont want to reuse a function(def)
for title in sorted(titles, key=lambda title: titles[title], reverse=True):  
    print(title, titles[title])