#!/usr/bin/python3
import pandas as pd

# df will be used for oxygen generator rating
# df_co2 will be used for co2 scrubber rating
df = pd.read_csv('day3input_cleaned', dtype=str, names=["Raw Bits"])

# Expand bits into individual columns
df_bits = df['Raw Bits'].str.split("", expand=True)
df['bit1'] = df_bits[1]
df['bit2'] = df_bits[2]
df['bit3'] = df_bits[3]
df['bit4'] = df_bits[4]
df['bit5'] = df_bits[5]
df['bit6'] = df_bits[6]
df['bit7'] = df_bits[7]
df['bit8'] = df_bits[8]
df['bit9'] = df_bits[9]
df['bit10'] = df_bits[10]
df['bit11'] = df_bits[11]
df['bit12'] = df_bits[12]
df_co2 = df.copy()

# Start with bit 1
bit = 1
while df.shape[0] > 1:
    # print(f"##### BIT{bit} EVALUATION ######")
    counts = df[f'bit{bit}'].value_counts()
    zeros = counts["0"]
    ones = counts["1"]
    # print(counts)
    # print(f'zeros = {zeros}')
    # print(f'ones = {ones}')
    if zeros > ones:
        # print('zeros greater than ones')
        filter = df[f'bit{bit}'] == "0"
        df = df[filter]
    elif ones > zeros:
        # print('ones greater than zeros')
        filter = df[f'bit{bit}'] == "1"
        df = df[filter]
    elif zeros == ones:
        # print('zeros equal to ones')
        filter = df[f'bit{bit}'] == "1"
        df = df[filter]
    bit += 1
    # print(df)
    # if bit == 5:
    #     break

# now do the opposite evaluation for co1. Start with bit 1
bit = 1
while df_co2.shape[0] > 1:
    # print(f"##### BIT{bit} EVALUATION ######")
    counts = df_co2[f'bit{bit}'].value_counts()
    zeros = counts["0"]
    ones = counts["1"]
    # print(counts)
    # print(f'zeros = {zeros}')
    # print(f'ones = {ones}')
    if zeros > ones:
        # print('zeros greater than ones')
        filter = df_co2[f'bit{bit}'] == "1"
        df_co2 = df_co2[filter]
    elif ones > zeros:
        # print('ones greater than zeros')
        filter = df_co2[f'bit{bit}'] == "0"
        df_co2 = df_co2[filter]
    elif zeros == ones:
        # print('zeros equal to ones')
        filter = df_co2[f'bit{bit}'] == "0"
        df_co2 = df_co2[filter]
    bit += 1
    # print(df_co2)
    # if bit == 5:
    #     break

oxy_dec = int(df.iat[0, 0], 2)
co2_dec = int(df_co2.iat[0, 0], 2)
print(f'oxygen generator rating = {oxy_dec}')
print(f'CO2 scrubber rating = {co2_dec}')
print(f'life support rating = {oxy_dec * co2_dec}')