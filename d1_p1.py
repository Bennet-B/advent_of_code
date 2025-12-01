INPUT_DATA: str = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

MAX_VALUE: int = 100
START_VALUE: int = 50
TARGET: int = 0

value: int = START_VALUE
count: int = 0

for rotation in INPUT_DATA.split('\n'):
    value += int(rotation[1:]) * (1 if rotation[0] == 'R' else -1)
    value = (value + MAX_VALUE) % MAX_VALUE
    count += value == TARGET
    #print(value)

print(f"\nOccurrences of {TARGET}: {count}")
