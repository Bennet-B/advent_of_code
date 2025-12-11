# INPUT_DATA: str = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out"""
with open("2025/day_11/d11_input.txt") as f: INPUT_DATA: str = f.read()

def count_paths(machine: str, visited: set[str]) -> int:
    if machine == 'out':
        return 1
    if machine in visited:
        return 0
    visited.add(machine)
    total_paths = 0
    for output in machines[machine]:
        total_paths += count_paths(output, visited)
    visited.remove(machine)
    return total_paths

machines: dict[str, set[str]] = {}
for line in INPUT_DATA.split('\n'):
    machine, outputs = line.split(': ')
    machines[machine] = set(outputs.split(' '))

print(f"\nTotal paths: {count_paths('you', set())}")

# personal solution: 636
