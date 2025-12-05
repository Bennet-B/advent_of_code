# Note: In part 2 (see: d5_p2.py), I switched to a much faster approach for performance (by combining ranges rather than just brute force); that strategy could be applied here as well!

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

fresh_ranges, available_ingredients = INPUT_DATA.split("\n\n")
ingredients: list[int] = list(map(int, available_ingredients.split('\n')))
mapped_ranges: list[tuple[int, int]] = []

for fresh_range in fresh_ranges.split('\n'):
    lower, upper = map(int, fresh_range.split('-'))
    mapped_ranges.append((lower, upper))

count: int = 0

for ingredient in ingredients:
    for fresh_range in mapped_ranges:
        if(ingredient >= fresh_range[0] and ingredient <= fresh_range[1]):
            count += 1
            break

print(f"\nFresh ingredients: {count}")

# personal solution: 681