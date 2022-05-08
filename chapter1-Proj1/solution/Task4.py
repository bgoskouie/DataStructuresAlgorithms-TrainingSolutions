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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
import copy
dflt = {"call_from": False, "call_to": False, "text_from": False, "text_to": False}
num_d = {}
for rec in texts:
    if rec[0] not in num_d.keys():
        num_d.update({rec[0]: copy.deepcopy(dflt)})
    if rec[1] not in num_d.keys():
        num_d.update({rec[1]: copy.deepcopy(dflt)})
    num_d[rec[0]]["text_from"] = True
    num_d[rec[1]]["text_to"] = True
for rec in calls:
    if rec[0] not in num_d.keys():
        num_d.update({rec[0]: copy.deepcopy(dflt)})
    if rec[1] not in num_d.keys():
        num_d.update({rec[1]: copy.deepcopy(dflt)})
    num_d[rec[0]]["call_from"] = True
    num_d[rec[1]]["call_to"] = True
possible_telemarketers = [num for num, attrs in num_d.items() if (attrs["call_from"] == True and attrs["call_to"] == False and attrs["text_from"] == False and attrs["text_to"] == False)]
print("These numbers could be telemarketers: ")
for num in sorted(set(possible_telemarketers)):
    print(num)


