# INPUT_DATA: str = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3"""
with open("2025/day_09/d9_input.txt") as f: INPUT_DATA: str = f.read()

points: list[tuple[int, int]] = []
for line in INPUT_DATA.split('\n'):
    x, y = map(int, line.split(','))
    points.append((x, y))

max_area: int = 0
for point1 in points:
    for point2 in points:
        max_area = max(max_area, abs((point1[0] - point2[0] + 1) * (point1[1] - point2[1] + 1)))

print(f"\nMax area: {max_area}")

# personal solution: 4759420470