#!/usr/bin/python3
#f = open('input1')
f = open('temp')
q = queue.Queue(maxsize=3)
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

