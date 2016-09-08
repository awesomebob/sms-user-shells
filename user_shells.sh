#!/bin/bash

cat /etc/passwd | \
cut -d ':' -f 7 | \
sort | uniq -c  | \
sort -nr        | \
awk '{print $2 ": " $1}'

