#!/usr/bin/python3
f = open("day2input_cleaned")

position = 0
depth = 0

i = 1

for l in f:
    direction = l.split(" ")[0]
    quantity = int(l.split(" ")[1])
    if direction == "up":
        depth -= quantity
    elif direction == "down":
        depth += quantity
    elif direction == "forward":
        position += quantity
#    print(l.strip())
#    i += 1
#    if i == 5:
#        break

print(f'position = {position}')
print(f'depth = {depth}')
print(f'final horizontal position X final depth = {position * depth}')
