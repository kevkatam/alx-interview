#!/usr/bin/python3
"""
module containing a script that reads stdin line by line and computes metrics
"""
import sys


status = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = [0]


def process_metrics():
    """ that prints computed metrics """
    print(f"File size: {sum(total_size)}")
    for key, value in sorted(status.items()):
        if value:
            print(f"{key}: {value}")


try:
    for i, line in enumerate(sys.stdin, start=1):
        parts = line.rstrip().split()
        try:
            s_code = parts[-2]
            size = parts[-1]
            if s_code in status.keys():
                status[s_code] += 1
            total_size.append(int(size))
        except Exception:
            pass
        if i % 10 == 0:
            process_metrics()
    process_metrics()
except KeyboardInterrupt:
    process_metrics()
    raise
