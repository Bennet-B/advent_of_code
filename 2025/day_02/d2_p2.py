from typing import Iterator
import math

# INPUT_DATA: str = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
with open("2025/day_02/d2_input.txt") as f: INPUT_DATA: str = f.read()

def divisor_pairs(n: int) -> Iterator[tuple[int, int]]:
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i, n // i

def repeats(x: int, y: int) -> Iterator[int]:
    for pattern in range(10**(x - 1), 10**x):
        yield int(str(pattern) * y)
    if x != 1 and y != 1 and x != y:
        for pattern in range(10**(y - 1), 10**(y)):
            yield int(str(pattern) * x)

sum: int = 0
for range_str in INPUT_DATA.split(','):
    start, end = range_str.split('-')
    lower, upper = max(11, int(start)), int(end)
    for length in range(len(start), len(end) + 1):
        checked: set[int] = set()
        for x, y in divisor_pairs(length):
            for invalidid in repeats(x, y):
                if lower <= invalidid <= upper and invalidid not in checked:
                    #print(invalidid)
                    sum += invalidid
                    checked.add(invalidid)

print(f"\nSum of invalid ids: {sum}")

# personal solution: 27180728081