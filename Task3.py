"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from functools import reduce
import re
from common import TYPES, calls


'''
order: O(6)
'''
def evaluate_phone_type(phone):
    fixed_call_match = re.match(r"\((\d+)\)(\d+)", phone)
    if fixed_call_match: return fixed_call_match[1], TYPES['FIXED_PHONE_CALL']
    if phone.startswith('140'): return '140', TYPES['MOBILE_PHONE_CALL']
    mobile_call_match = re.match(r"^([9,8,7]{1})(\d{3})\d{0,1}\s\d+", phone)
    if mobile_call_match: return mobile_call_match[1]+mobile_call_match[2], TYPES['TELEMARKETING_PHONE_CALL']
    return '???', 'unknown'


'''
order: O(5)
'''
def by_unique_numbers_from_bangalore(acc, x):
    incoming, answering, incoming_date, duration = x
    if not incoming.startswith('(080)'): return acc
    incoming_prefix, incoming_phone_type = evaluate_phone_type(incoming)
    answering_prefix, answering_phone_type = evaluate_phone_type(answering)
    return [*acc, [incoming, incoming_prefix, incoming_phone_type, answering, answering_prefix, answering_phone_type, incoming_date, duration]]


'''
order: O(n)
'''
def find_all_numbers_from_bangalore(calls):
    return reduce(by_unique_numbers_from_bangalore, calls, [])


'''
order: O(3)
'''
def by_unique_answering_codes(acc, x):
    answering_prefix, answering_phone_type = x[4], x[5]
    return acc if TYPES['FIXED_PHONE_CALL'] is not answering_phone_type or answering_prefix in acc else [*acc, answering_prefix]


'''
order: O(n)
'''
def find_unique_codes_from_answering_phones(records):
    return reduce(by_unique_answering_codes, records, [])


'''
order: O(n+1)
'''
def print_message_about_people_called_in_bangalore(codes):
    print("The numbers called by people in Bangalore have codes:")
    for code in codes: print("- {}".format(code))


'''
order: O(2)
'''
def calculate_percentage(numerator, denominator):
    return 0 if 0 == numerator or 0 == denominator else (numerator / denominator) * 100


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
bangalore_records = find_all_numbers_from_bangalore(calls)
answering_codes = sorted(find_unique_codes_from_answering_phones(bangalore_records), key=lambda x: int(x))
bangalore_to_bangalore_fixed_phone_calls = list(filter(lambda x: TYPES['FIXED_PHONE_CALL'] is x[5], bangalore_records))
calls_from_bangalore_to_other_fixed_lines_percent = calculate_percentage(len(bangalore_to_bangalore_fixed_phone_calls), len(bangalore_records))

print_message_about_people_called_in_bangalore(answering_codes)
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(calls_from_bangalore_to_other_fixed_lines_percent))
