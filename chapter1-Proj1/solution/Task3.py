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
bangalore_calls_to = set()
numbers_fixed = set()
numbers_mobile = set()
numbers_telemarketer = set()
numbers_others = set()
codes = set()
call_from_bang2any_count = 0
call_from_bang2bang_count = 0
for record in calls:
  if record[0].startswith("(080)"):
    call_from_bang2any_count += 1
    callee = record[1]
    if callee.startswith("(080)"):
      call_from_bang2bang_count += 1
    if callee not in bangalore_calls_to:
      bangalore_calls_to.add(callee)
      if callee.startswith("(0"):
        numbers_fixed.add(callee)
        parts = callee.split(")")
        code = parts[0][1:]
        if code not in codes:
          codes.add(code)
      elif (" " in callee) and (callee[0] in ["7", "8", "9"]):
        numbers_mobile.add(callee)
        codes.add(callee[:4])
      elif callee.startswith("140"):
        numbers_telemarketer.add(callee)
        codes.add("140")
      else:
        numbers_others.add(callee)
print("The numbers called by people in Bangalore have codes:")
for code in sorted(codes):
  print(code)
print("%0.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."% (call_from_bang2bang_count * 100 / call_from_bang2any_count))


