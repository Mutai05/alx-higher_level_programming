#!/usr/bin/python3
"""Reads stdin line by line, computes metrics, and prints statistics"""

import sys

def print_stats(total_size, status_count):
    """Prints the statistics computed"""
    print("File size: {}".format(total_size))
    sorted_statuses = sorted(status_count.items())
    for status, count in sorted_statuses:
        if count > 0:
            print("{}: {}".format(status, count))

def parse_line(line):
    """Parses the input line to extract status code and file size"""
    parts = line.split()
    if len(parts) >= 2:
        status_code = parts[-2]
        file_size = parts[-1]
        return int(status_code), int(file_size)
    return None, None

def main():
    """Main function to process input and compute statistics"""
    total_size = 0
    status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            line_count += 1
            status, size = parse_line(line)
            if status and size:
                total_size += size
                if status in status_count:
                    status_count[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_count)

    except KeyboardInterrupt:
        print_stats(total_size, status_count)
        raise

if __name__ == "__main__":
    main()
