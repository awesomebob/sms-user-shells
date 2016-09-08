#!/usr/bin/python3

from collections import Counter

with open('/etc/passwd') as f:
    shells = [line.rstrip().split(':').pop() for line in f]

for value, count in Counter(shells).most_common():
    print(value + ":", count)

