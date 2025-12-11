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

edges_x: list[tuple[int, int, int]] = []
edges_y: list[tuple[int, int, int]] = []
for idx, point in enumerate(points):
    next_point = points[(idx + 1) % len(points)]
    if point[0] == next_point[0]:
        edges_x.append((point[0], min(point[1], next_point[1]), max(point[1], next_point[1])))
    else:
        edges_y.append((point[1], min(point[0], next_point[0]), max(point[0], next_point[0])))

max_area: int = 0
for p1 in points:
    for p2 in points:
        min_x, min_y = min(p1[0], p2[0]), min(p1[1], p2[1])
        max_x, max_y = max(p1[0], p2[0]), max(p1[1], p2[1])

        intersects = False
        for x, start, end in edges_x:            
            if min_x < x < max_x and not (end <= min_y or start >= max_y):
                intersects = True
                break
        if intersects:
            continue
        for y, start, end in edges_y:
            if min_y < y < max_y and not (end <= min_x or start >= max_x):
                intersects = True
                break
        if not intersects:
            area = (max_x - min_x + 1) * (max_y - min_y + 1)
            max_area = max(max_area, area)

print(f"\nMax area: {max_area}")

# personal solution: 1603439684