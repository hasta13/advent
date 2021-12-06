#!/usr/bin/python3
f = open('day1input')
#f = open('temp')
last = -1
count = 0
for line in f:
    next = int(line.strip())
    diff = 0
    if last > -1:
        diff = next - last
    if diff > 0:
        count += 1
    last = next
print(count)

