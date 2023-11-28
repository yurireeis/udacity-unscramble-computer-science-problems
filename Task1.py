"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from functools import reduce
from common import texts, calls


records = texts + calls


'''
order: O(2n+5)
'''
def evaluate_repeated_numbers(acc, x):
    incoming, answering = x[:2]
    has_incoming = incoming in acc
    has_answering = answering in acc
    if not has_incoming and not has_answering: return acc + [incoming, answering]
    if not has_incoming: return acc + [incoming]
    if not has_answering: return acc + [answering]
    return acc

'''
order: O(n)
'''
def get_unique_phone_numbers(records):
    return reduce(evaluate_repeated_numbers, records, [])


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
different_phone_numbers = get_unique_phone_numbers(records)
print("There are {} different telephone numbers in the records.".format(len(different_phone_numbers)))
