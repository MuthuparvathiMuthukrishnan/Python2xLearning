#CSV
import csv #import csv to read csv file
with open('Data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0],row[1], sep = "| ")
