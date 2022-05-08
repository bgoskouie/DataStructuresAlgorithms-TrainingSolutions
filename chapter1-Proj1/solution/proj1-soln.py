
import copy
# proj1-soln.py

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

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
phone_texts_l = []
for record in texts:
    if record[0] not in phone_texts_l:
        phone_texts_l.append(record[0])
    if record[1] not in phone_texts_l:
        phone_texts_l.append(record[1])
phone_calls_l = []
for record in calls:
    if record[0] not in phone_calls_l:
        phone_calls_l.append(record[0])
    if record[1] not in phone_calls_l:
        phone_calls_l.append(record[1])
print(f"There are {len(phone_texts_l) + len(phone_calls_l)} different telephone numbers in the records.")

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
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
a = 0
bangalore_calls_to = []
numbers_fixed = []
numbers_mobile = []
numbers_telemarketer = []
numbers_others = []
numbers_fixed_codes = []
call_from_bang2bang_count = 0
for record in calls:
    if record[0].startswith("(080)"):
        if record[1] not in bangalore_calls_to:
            bangalore_calls_to.append(record[1])
            if record[1].startswith("(0"):
                numbers_fixed.append(record[1])
                parts = record[1].split(")")
                code = parts[0][1:]
                if code not in numbers_fixed_codes:
                    numbers_fixed_codes.append(code)
                if record[1].startswith("(080)"):
                    call_from_bang2bang_count += 1
            elif (" " in record[1] and record[1][0] in ["7", "8", "9"]):
                numbers_mobile.append(record[1])
            elif record[1].startswith("140"):
                numbers_telemarketer.append(record[1])
            else:
                numbers_others.append(record[1])
print("The numbers called by people in Bangalore have codes:")
for code in sorted(numbers_fixed_codes):
    print(code)
print(f"{int(call_from_bang2bang_count * 100 / len(numbers_fixed))} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
a = 0
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
texts.append(['1245 12425', '5432 145', '451'])
texts.append(['1245 12424', '5432 145', '451'])
texts.append(['1245 12426', '5432 145', '451'])
calls.append(['1245 12425', '5432 145', '451'])
rcds = [['1245 12425', '5432 145', '451'], ['1245 12424', '5432 145', '451'], ['1245 12426', '5432 145', '451']]
dflt = {"call_from": False, "call_to": False, "text_from": False, "text_to": False}
num_d = {}
for rec in texts:
    if rec in rcds:
        a = 0
    if rec[0] not in num_d.keys():
        num_d.update({rec[0]: copy.deepcopy(dflt)})
    if rec[1] not in num_d.keys():
        num_d.update({rec[1]: copy.deepcopy(dflt)})
    num_d[rec[0]]["text_from"] = True
    num_d[rec[1]]["text_to"] = True
for rec in calls:
    if rec in rcds:
        a = 0
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
a = 0