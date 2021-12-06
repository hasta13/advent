#!/usr/bin/python3
f = open('day3input_cleaned')
# i = 1
bit_sums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for l in f:
    # print(f'line {i}: {l.strip()}')
    j = 0
    for bit in l.strip():
        bit = int(bit)
        # print(bit)
        if bit == 0:
            bit_sums[j] -= 1
        elif bit == 1:
            bit_sums[j] += 1
        j += 1
    # i += 1
    # if i == 6:
    #     break

print(f'bit_sums = {bit_sums}')
i = 0
gamma_rate = ""
eplison_rate = ""
for bit_sum in bit_sums:
    if bit_sum > 0:
        gamma_rate += "1"
        eplison_rate += "0"
    elif bit_sum < 0:
        gamma_rate += "0"
        eplison_rate += "1"

print(f'gamma_rate = {gamma_rate} ({int(gamma_rate, 2)})')
print(f'eplison_rate = {eplison_rate} ({int(eplison_rate, 2)})')
print(f'power consumption = {int(gamma_rate, 2) * int(eplison_rate, 2)}')