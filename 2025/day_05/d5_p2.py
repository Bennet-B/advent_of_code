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

mapped_ranges: list[tuple[int, int]] = []

for fresh_range in INPUT_DATA.split("\n\n")[0].split('\n'):
    lower, upper = map(int, fresh_range.split('-'))
    mapped_ranges.append((lower, upper))

new_ranges: list[tuple[int, int]] = []
has_changes: bool = True

while has_changes:
    has_changes = False
    for current_range in mapped_ranges:
        was_merged = False
        for idx, existing_range in enumerate(new_ranges):
            if current_range[0] >= existing_range[0] and current_range[0] <= existing_range[1]:
                was_merged = True
                if current_range[1] > existing_range[1]:
                    new_ranges[idx] = (existing_range[0], current_range[1])
                break
            elif current_range[1] >= existing_range[0] and current_range[1] <= existing_range[1]:
                was_merged = True
                new_ranges[idx] = (current_range[0], existing_range[1])
                break
            elif existing_range[0] > current_range[0] and existing_range[1] < current_range[1]:
                was_merged = True
                new_ranges[idx] = (current_range[0], current_range[1])
                break
                
        if not was_merged:
            new_ranges.append(current_range)
        has_changes = has_changes or was_merged
        
    mapped_ranges = new_ranges
    new_ranges = []

count: int = 0

for range_x in mapped_ranges:
    count += range_x[1] - range_x[0] + 1

print(f"\nPossibly fresh ingredients: {count}")

# personal solution: 348820208020395