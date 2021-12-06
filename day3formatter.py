#!/usr/bin/python3
f = open("day3input_raw")
f_out = open('day3input_cleaned', 'w')
#i = 1
for l in f:
#    print(f'line {i}: {l.strip()}')
    numbers = l.strip().split(" ")
    for number in numbers:
        #print(number)
        f_out.write(f'{number}\n')
#    i += 1
#    if i == 3:
#        break
