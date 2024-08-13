#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
import signal

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def process_line(line, total_size, status_codes):
    parts = line.split()
    if len(parts) < 7:
        return total_size  # skip lines that don't match the format

    ip, dash, date, request_type, url, protocol, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]

    try:
        total_size += int(file_size)
    except ValueError:
        return total_size  # skip line if file size is not an integer

    if status_code.isdigit() and int(status_code) in status_codes:
        status_codes[int(status_code)] += 1

    return total_size

def signal_handler(sig, frame):
    print_stats(total_size, status_codes)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        total_size = process_line(line.strip(), total_size, status_codes)
        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)
except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    sys.exit(0)

# Print the final stats if the loop ends
print_stats(total_size, status_codes)
