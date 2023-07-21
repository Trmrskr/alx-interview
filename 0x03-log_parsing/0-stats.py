#!/usr/bin/python3
"""
Script reads stdin line by line and computes metrics
"""

import sys


def print_status(status_code, size):
    """print status information"""
    print("File size: {}".format(size))
    for key in sorted(status_code.keys()):
        if status_code[key] != 0:
            print("{} {}".format(key, status_code[key]))


def log_stat():
    """Compute the log statistics"""
    status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0
    total_file_size = 0

    try:
        data = sys.stdin.read()
        lines = data.rstrip().split("\n")

        for line in lines:
            if count != 0 and count % 10 == 0:
                print_status(status_code, total_file_size)

            words = line.split(" ")
            count += 1
            total_file_size += int(words[-1])
            code = words[-2]
            if code in status_code:
                status_code[code] += 1
        print_status(status_code, total_file_size)
    except KeyboardInterrupt:
        print_status(status_code, total_file_size)
        raise


if __name__ == "__main__":
    """The main namespace"""
    log_stat()
