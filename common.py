import csv


TYPES = dict(FIXED_PHONE_CALL='fixed', MOBILE_PHONE_CALL='mobile', TELEMARKETING_PHONE_CALL='telemarketing')

def get_csv_content(filepath):
    with open(filepath, 'r') as f:
        return list(csv.reader(f))


texts = get_csv_content('texts.csv')
calls = get_csv_content('calls.csv')
