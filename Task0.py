"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from common import texts, calls


'''
order: O(1)
'''
def get_first_and_last_items(items):
    return items[0], items[-1]


'''
order: O(1)
'''
def show_record_message_with_incoming_answering_and_time(record, message):
    print(message.format(*record))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
desired_text = get_first_and_last_items(texts)[0]
desired_call = get_first_and_last_items(calls)[-1]

show_record_message_with_incoming_answering_and_time(desired_text, "First record of texts, {} texts {} at time {}")
show_record_message_with_incoming_answering_and_time(desired_call, "Last record of calls, {} calls {} at time {}, lasting {} seconds")
