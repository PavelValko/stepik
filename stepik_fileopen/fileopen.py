import re

with open('dataset_3363_2.txt', 'r') as file:
    string = file.readline()
    string_strip = string.strip()

# add to list all symbols
symbols = re.split('\d+', string_strip)
# add to list all digits
digits = re.findall('[0-9]+', string_strip)

for i in range(len(symbols) - 1):
    print(symbols[i] * int(digits[i]), end='')
