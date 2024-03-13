import csv

test_data = [
    ['Name','Age','City'],
    ['Paru',28,'New York'],
    ['Krish',28,'Los Angeles']
]
try:
    with open('mydata.csv','w') as file:
        writer = csv.writer(file)
        for data in test_data:
            writer.writerow(data)
except FileNotFoundError as f:
    print(f)
finally:
    print('Close your files!')