#!/usr/bin/python3
f = open('day1input')
#f = open('temp')
count = 0
window = []
last = -1
i = 0
for line in f:
    if len(window) < 3:
        window.append(int(line.strip()))
    else:
        window[i] = int(line.strip())
    if len(window) == 3:
        next = sum(window)
        diff = 0
        if last > -1:
            diff = next - last
        if diff > 0:
            count += 1
        last = next
    i += 1
    if i > 2:
        i = 0
print(count)

