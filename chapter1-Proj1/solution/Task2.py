"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phonenumber_length_d = {}
for record in calls:
    for phonenum in [record[0], record[1]]:
        if phonenum in phonenumber_length_d.keys():
            phonenumber_length_d[phonenum] += int(record[3])
        else:
            phonenumber_length_d.update({phonenum : int(record[3])})
# initialize with a random item:
longest = [list(phonenumber_length_d.keys())[0], list(phonenumber_length_d.values())[0]]
for phonenum, length in phonenumber_length_d.items():
    if length > longest[1]:
        longest = [phonenum, length]
print(f"{longest[0]} spent the longest time, {longest[1]} seconds, on the phone during September 2016.")

