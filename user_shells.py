#!/usr/bin/python3

from collections import Counter
import re

etcpasswd = open('/etc/passwd')
shells = re.findall('(?<=:)([^:]+)$', etcpasswd.read().rstrip(), re.MULTILINE)
etcpasswd.close()

for value, count in Counter(shells).most_common():
    print(value + ":", count)

