INPUT_DATA: str = """987654321111111
811111111111119
234234234234278
818181911112111"""

sum: int = 0

for bank in INPUT_DATA.split('\n'):
    first_idx: int = 0
    first_digit: int = int(bank[0])
    second_digit: int = -1    
    for idx, c in enumerate(bank[1:-1]):
        digit: int = int(c)
        if(digit > first_digit):
            first_idx = idx + 1
            first_digit = digit

    for c in bank[first_idx + 1:]:
        digit: int = int(c)
        if(digit > second_digit):
            second_digit = digit

    sum += int(str(first_digit) + str(second_digit))
    #print(str(first_digit) + str(second_digit))

print(f"\nMaximum joltage: {sum}")

# personal solution: 16812