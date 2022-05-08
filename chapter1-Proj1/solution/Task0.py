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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, '97424 22395' texts '90365 06212' at time '01-09-2016 06:03:22'
"Last record of calls, '98447 62998' calls '(080)46304537' at time '30-09-2016 23:57:15', lasting '2151' seconds"
"""
print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}")   # ['97424 22395', '90365 06212', '01-09-2016 06:03:22']
print(f"Last record of calls, {calls[-1][0]} calls {calls[-1][1]} at time {calls[-1][2]}, lasting {calls[-1][3]} seconds")  # ['98447 62998', '(080)46304537', '30-09-2016 23:57:15', '2151']


