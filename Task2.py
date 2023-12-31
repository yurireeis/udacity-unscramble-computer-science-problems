"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from functools import reduce
from datetime import datetime
from common import calls


'''
order: O(3)
'''
def evaluate_previous_and_next_calls(acc, x):
    incoming, answering, incoming_date, duration = x
    return [incoming, duration, datetime.strptime(incoming_date, "%d-%m-%Y %H:%M:%S").strftime("%B, %Y")] if not acc or int(acc[1]) < int(duration) else acc


'''
order: O(n)
'''
def get_longest_call_phone_number_and_duration(records):
    return reduce(evaluate_previous_and_next_calls, records, None)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
record = get_longest_call_phone_number_and_duration(calls)
print("{} spent the longest time, {} seconds, on the phone during {}.".format(*record))
