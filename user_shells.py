#!/usr/bin/python3

from collections import Counter
import re

etcpasswd = open('/etc/passwd')
pwf = etcpasswd.read()
etcpasswd.close()

lines = pwf.rstrip().split("\n")
shells = [re.split(":", line)[-1] for line in lines]

for value, count in Counter(shells).most_common():
    print(value + ":", count)

