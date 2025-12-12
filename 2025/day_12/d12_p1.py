with open("2025/day_12/d12_input.txt") as f: INPUT_DATA: str = f.read()
# won't get the right answer for the task example
# a really disceptive problem statement (if you want to see my struggles, have a look at d12_p1_old.py)

sections: list[str] = INPUT_DATA.split("\n\n")
shapes: dict[int, int] = {}
for section in sections[:-1]:
    idx_str, shape_str = section.split(":\n")
    shapes[int(idx_str)] = shape_str.count('#')
idx_count: int = len(shapes)  

boxes: list[tuple[tuple[int, int], tuple[int, ...]]] = []
for line in sections[-1].split("\n"):
    size_str, idx_count_str = line.split(": ")
    width, height = [int(s) for s in size_str.split("x")]
    shape_indices: tuple[int, ...] = tuple(int(s) for s in idx_count_str.split(" "))
    boxes.append(((width, height), shape_indices))

solvable_count: int = 0
for box in boxes:
    cells_to_place: int = 0
    for idx in range(idx_count):
        cells_to_place += shapes[idx] * box[1][idx]
    if cells_to_place <= box[0][0] * box[0][1]:
        solvable_count += 1

print(f"\nProbably solvable: {solvable_count}")

# personal solution: 589

# just sorting out the really bad ones, was enough to get the right answer... 🤡