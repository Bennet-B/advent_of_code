INPUT_DATA: str = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

JUNCTION_AMOUNT: int = 10
# JUNCTION_AMOUNT: int = 1000

vectors: list[tuple[int, int, int]] = []

for line in INPUT_DATA.split('\n'):
    vectors.append(tuple(map(int, line.split(','))))

# index of nearest vector, distance
vec_map: list[int, int, float] = []

for idx_x, vec_x in enumerate(vectors):
    print(len(vec_map))
    for idx_y, vec_y in enumerate(vectors[idx_x + 1:]):
        distance: int = ((vec_x[0] - vec_y[0])**2 + (vec_x[1] - vec_y[1])**2 + (vec_x[2] - vec_y[2])**2)**0.5
        vec_map.append((idx_x, idx_x + 1 + idx_y, distance))

print(f"Total vectors: {len(vectors)}")

circuits: list[set[int]] = []
for m in sorted(vec_map, key=lambda t: t[2])[:JUNCTION_AMOUNT]:
    print(vectors[m[0]], vectors[m[1]], m[2])
    circuits.append(set([m[0], m[1]]))

print(f"Initial circuits: {circuits}")

new_circuits: list[set[int]] = []
has_changes: bool = True
while has_changes:
    print("--- New iteration ---")
    has_changes = False
    for current_circuit in circuits:
        was_merged: bool = False
        for idx, new_circuit in enumerate(new_circuits):
            if current_circuit & new_circuit:
                new_circuits[idx] = current_circuit | new_circuit
                was_merged = True
                break
               
        if not was_merged:
            new_circuits.append(current_circuit)
        has_changes = has_changes or was_merged
 
    circuits = new_circuits
    new_circuits = []
 
total: int = 1
 
for size in sorted(circuits, key=lambda s: len(s), reverse=True)[:3]:
    total *= len(size)
    print(len(size))
 
print(circuits)
 
print(f"\nTotal: {total}")
 
# personal solution: 330786