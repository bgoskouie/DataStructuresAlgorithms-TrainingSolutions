"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers = set()
for record in texts:
    if record[0] not in numbers:
        numbers.add(record[0])
    if record[1] not in numbers:
        numbers.add(record[1])
for record in calls:
    if record[0] not in numbers:
        numbers.add(record[0])
    if record[1] not in numbers:
        numbers.add(record[1])
print(f"There are {len(numbers)} different telephone numbers in the records.")


