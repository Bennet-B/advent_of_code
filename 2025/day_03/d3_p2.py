INPUT_DATA: str = """987654321111111
811111111111119
234234234234278
818181911112111"""

B_AMOUNT: int = 12

sum: int = 0

for bank in INPUT_DATA.split('\n'):
    last_idx: int = 0
    current_idx: int = 0
    digits: list[int] = [-1] * B_AMOUNT
    num: int = 0
    for i in range(B_AMOUNT):
        max_idx: int | None = i - B_AMOUNT + 1
        max_idx = max_idx if max_idx != 0 else None
        for idx, c in enumerate(bank[last_idx:max_idx]):
            digit: int = int(c)
            if(digit > digits[i]):
                current_idx = idx
                digits[i] = digit
                
        last_idx = current_idx + last_idx + 1
        num += digits[i] * 10**(B_AMOUNT - i - 1)
        
    sum += num
    #print(num)

print(f"\nMaximum joltage: {sum}")

# personal solution: 166345822896410