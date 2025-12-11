# INPUT_DATA: str = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""
with open("2025/day_01/d1_input.txt") as f: INPUT_DATA: str = f.read()
MAX_VALUE: int = 100

value: int = 50
count: int = 0

for rotation in INPUT_DATA.split('\n'):
    steps = int(rotation[1:]) * (1 if rotation[0] == 'R' else -1)
    count += max(0, 1 + (abs(steps) - (((MAX_VALUE - value) if steps > 0 else value) % MAX_VALUE) - 1) // MAX_VALUE)
    value = (value + steps) % MAX_VALUE
    #print(value)

print(f"\nHits of 0: {count}")

# personal solution: 6496
