from typing import LiteralString

INPUT_DATA: LiteralString = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

lines: list[LiteralString] = INPUT_DATA.split('\n')
numbers: list[list[int]] = []

total_sum: int = 0
is_add: bool = True # immediately overridden in loop
product: int = 1
cidx: int = -1

for c in lines[-1].split(' '):
    if c == '+':
        is_add = True
        cidx += 1
        if product != 1:
            total_sum += product
            product = 1
    elif c == '*':
        is_add = False
        cidx += 1
        if product != 1:
            total_sum += product
            product = 1
    
    num_str: LiteralString = ''
    for lidx in range(len(lines) - 1):
        if lines[lidx][cidx] != ' ':
            num_str += lines[lidx][cidx]
    if is_add:
        total_sum += int(num_str)
    else:
        product *= int(num_str)

    #print(num_str)
    cidx += 1

if product != 1:
    total_sum += product

print(f"\nTotal: {total_sum}")

# personal solution: 12841228084455