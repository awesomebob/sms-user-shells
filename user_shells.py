#!/usr/bin/python3

from collections import Counter
import re

with open('/etc/passwd') as f:
    shells = re.findall('(?<=:)([^:]+)$', f.read().rstrip(), re.MULTILINE)

for value, count in Counter(shells).most_common():
    print(value + ":", count)

