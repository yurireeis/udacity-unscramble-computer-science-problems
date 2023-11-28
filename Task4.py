"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from functools import reduce
import re
from common import TYPES, texts, calls

'''
order:
    - space:
    - time:
'''
def every_unique_number_on_texts(acc, x):
    if not x[0] in acc and not x[1] in acc: return [*acc, x[0], x[1]] 
    if x[0] not in acc: return [*acc, x[0]]
    if x[1] not in acc: return [*acc, x[1]]
    return acc

'''
order:
    - space:
    - time:
'''
def by_parsed_phone(phone): return ''.join(re.findall(r"(\d+)", phone))

'''
order:
    - space:
    - time:
'''
def by_parsed_phone_led_by_zero(phone):
    parsed_phone = by_parsed_phone(phone)
    return int('1{}'.format(parsed_phone)) if parsed_phone.startswith('0') else int(parsed_phone)

'''
order:
    - space:
    - time:
'''
def possible_telemarketers_triage(calls, texts):
    unique_text_numbers = reduce(every_unique_number_on_texts, texts, [])
    unique_incoming_call_numbers = reduce(lambda acc, x: acc if x[0] in acc else [*acc, x[0]] , calls, [])
    unique_answering_call_numbers = reduce(lambda acc, x: acc if x[1] in acc else [*acc, x[1]] , calls, [])
    all_numbers_to_analyse = reduce(lambda acc, x: acc if x in acc else [*acc, x], unique_answering_call_numbers+unique_text_numbers, [])

    def by_possible_telemarketers(acc, x): return [*acc, x] if x not in all_numbers_to_analyse else acc

    sorted_phones = sorted(reduce(by_possible_telemarketers, unique_incoming_call_numbers, []), key=by_parsed_phone_led_by_zero)

    return sorted_phones


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

unique_possible_telemarketers = possible_telemarketers_triage(calls, texts)
print("These numbers could be telemarketers: ")
for phone in unique_possible_telemarketers: print("- {}".format(phone))
