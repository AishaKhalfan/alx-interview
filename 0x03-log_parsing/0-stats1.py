import re
import sys

# Regular expression pattern to match the desired format
pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*)\] "GET \/projects\/(\d+) HTTP\/1\.1" (\d{3}) (\d+)'

# Initialize variables to store metrics
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_read = 0

try:
    while True:
        line = input("Enter a line (or press CTRL + C to finish): ")

        # Check if the line matches the desired format
        match = re.match(pattern, line)
        if not match:
            print("Skipped invalid line:", line)
            continue

        # Extract relevant data from the matched line
        file_size = int(match.group(5))
        status_code = int(match.group(4))

        # Update metrics
        total_size += file_size
        status_counts[status_code] += 1
        lines_read += 1

        # Print statistics every 10 lines
        if lines_read % 10 == 0:
            print("Total file size: File size:", total_size)
            print("Number of lines by status code:")
            for code, count in sorted(status_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    # If CTRL + C is pressed, print the final statistics
    print("Final Statistics:")
    print("Total file size: File size:", total_size)
    print("Number of lines by status code:")
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")

