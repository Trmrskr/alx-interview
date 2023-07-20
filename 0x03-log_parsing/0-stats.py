#!/usr/bin/env python3
"""
Script reads stdin line by line and computes metrics
"""

import sys

def printStatus(statusCode, size):
    """print status information"""
    print("File size: {}".format(size))
    for key in sorted(statusCode.keys()):
        if statusCode[key] != 0:
            print("{} {}".format(key, statusCode[key]))

statusCode = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
count = 0
total_file_size = 0

try:
    data = sys.stdin.read()
    lines = data.rstrip().split("\n")

    for line in lines:
        count += 1

        if count != 0 and count % 10 == 0:
            printStatus(statusCode, total_file_size)

        words = line.split(" ")
        total_file_size += int(words[-1])
        code = int(words[-2])
        if code in statusCode:
            statusCode[code] += 1

    printStatus(statusCode, total_file_size)
except KeyboardInterrupt:
    printStatus(statusCode, total_file_size)
    raise
