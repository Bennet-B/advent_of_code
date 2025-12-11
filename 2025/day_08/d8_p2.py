# INPUT_DATA: str = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""
with open("2025/day_08/d8_input.txt") as f: INPUT_DATA: str = f.read()

vectors: list[tuple[int, int, int]] = []
for line in INPUT_DATA.split('\n'):
    x, y, z = map(int, line.split(','))
    vectors.append((x, y, z))

vec_map: list[tuple[int, int, float]] = []
for idx_x, vec_x in enumerate(vectors):
    for idx_y, vec_y in enumerate(vectors[idx_x + 1:]):
        distance: int = ((vec_x[0] - vec_y[0])**2 + (vec_x[1] - vec_y[1])**2 + (vec_x[2] - vec_y[2])**2)**0.5
        vec_map.append((idx_x, idx_x + 1 + idx_y, distance))

total_set: set[int] = set()
for m in sorted(vec_map, key=lambda t: t[2]):
    total_set.add(m[0])
    total_set.add(m[1])
    if len(total_set) == len(vectors):
        print(f"\nTotal: {vectors[m[0]][0] * vectors[m[1]][0]}")
        break
 
# personal solution: 3276581616