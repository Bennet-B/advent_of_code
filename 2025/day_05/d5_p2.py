# TODO: optimize, basic first approch

INPUT_DATA: str = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

mapped_ranges: list[(int, int)] = []

for fresh_range in INPUT_DATA.split("\n\n")[0].split('\n'):
    lower, upper = map(int, fresh_range.split('-'))
    mapped_ranges.append((lower, upper))

print(mapped_ranges)

new_ranges: list[(int, int)] = []
has_changes: bool = True
while has_changes:
    has_changes = False
    for range_x in mapped_ranges:
        handled = False
        for idx, mapped_range in enumerate(new_ranges):
            if range_x[0] >= mapped_range[0] and range_x[0] <= mapped_range[1]:
                handled = True
                if(range_x[1] > mapped_range[1]):
                    new_ranges[idx] = (mapped_range[0], range_x[1])
                break
            if range_x[1] >= mapped_range[0] and range_x[1] <= mapped_range[1]:
                handled = True
                new_ranges[idx] = (range_x[0], mapped_range[1])
                break
            if mapped_range[0] > range_x[0] and mapped_range[1] < range_x[1]:
                handled = True
                new_ranges[idx] = (range_x[0], range_x[1])
                break
        if not handled:
            new_ranges.append(range_x)
        has_changes = has_changes or handled
    mapped_ranges = new_ranges
    new_ranges = []

print()
print(mapped_ranges)

count: int = 0

for range_x in mapped_ranges:
    count += range_x[1] - range_x[0] + 1

print(f"\nPossibly fresh ingredients: {count}")

# personal solution: 348820208020395