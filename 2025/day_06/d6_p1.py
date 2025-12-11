# INPUT_DATA: str = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """
with open("2025/day_06/d6_input.txt") as f: INPUT_DATA: str = f.read()

lines: list[str] = INPUT_DATA.split('\n')
numbers: list[list[int]] = []
for s in lines[:-1]:
    numbers.append(list(map(int, s.split())))

total_sum: int = 0
for idx, op in enumerate(lines[-1].split()):
    if op == '+':
        for i in range(len(numbers)):
            total_sum += numbers[i][idx]
    else:
        product: int = 1
        for i in range(len(numbers)):
            product *= numbers[i][idx]
        total_sum += product
        
print(f"\nTotal: {total_sum}")

# personal solution: 7644505810277