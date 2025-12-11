# INPUT_DATA: str = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out"""
with open("2025/day_11/d11_input.txt") as f: INPUT_DATA: str = f.read()

def count_paths(machine: str, targets: set[str], visited: set[str]) -> dict[str, int]:
    counts = {target: 0 for target in targets}
    if machine in targets:
        counts[machine] = 1
        return counts
    if machine in visited:
        return counts
    if machine in cache:
        return cache[machine]
    visited.add(machine)
    for output in machines[machine]:
        output_counts = count_paths(output, targets, visited)
        for target in targets:
            counts[target] += output_counts[target]
    visited.remove(machine)
    cache[machine] = counts
    return counts

machines: dict[str, set[str]] = {}
for line in INPUT_DATA.split('\n'):
    machine, outputs = line.split(': ')
    machines[machine] = set(outputs.split(' '))

paths: dict[str, dict[str, int]] = {}
for start, targets in [
    ('svr', {'dac', 'fft', 'out'}),
    ('dac', {'fft', 'out', 'svr'}),
    ('fft', {'out', 'svr', 'dac'})
]:
    cache: dict[str, dict[str, int]] = {}
    paths[start] = count_paths(start, targets, set())

total_paths: int = paths['svr']['dac'] * paths['dac']['fft'] * paths['fft']['out'] + paths['svr']['fft'] * paths['fft']['dac'] * paths['dac']['out']

print(f"\nTotal paths: {total_paths}")

# personal solution: 509312913844956
