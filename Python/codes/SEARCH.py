import csv
import re

# dictionary data collection
# counting how many duplicate a title has
# and sorting them into the highest value
# hence the reverse=True
titles = input("Title: ").strip().upper()

counter = 0

with open("csv/testing.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Employee Markme"].strip().upper() 
        if re.search("^(TRIVEDI|DEEP TRIVEDI)$", title): #regular expression for python (^, $, .*, .+, etc) just search this on google
            counter += 1

print(counter)