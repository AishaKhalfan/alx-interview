#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics
    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption
    (CTRL + C), print these statistics from the beginning
"""


import sys
import re


def print_status_codes(status_codes_dict):
    '''This print status code with its no.cof count.
    Format:
        <status>: <count>
    '''
    for key, value in sorted(status_codes_dict.items()):
        print("{}: {}".format(key, value))


status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # keep count of the number lines counted

try:
    for line in sys.stdin:
        # Use regular expressions to extract status code and file size
        match = re.match(r'.*\s"GET\s/projects/\d+"\s(\d+)\s(\d+)', line)
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))
            # check if the status code received exists in the dictionary and
            # increment its count
            if status_code in status_codes_dict.keys():
                status_codes_dict[status_code] += 1

            # update total size
            total_size += file_size

            # update count of lines
            count += 1

        if count == 10:
            count = 0  # reset count
            print('File size: {}'.format(total_size))
            print_status_codes(status_codes_dict)

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    print_status_codes(status_codes_dict)
