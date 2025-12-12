from typing import Iterator

INPUT_DATA: str = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
# dont even think about reading from the file! This solution can barely handle the input as is - hated the problem with all my heart - the amount of time i spent on thinking of a way to solve this (in time...) is ridiculous
# with open("2025/day_01/d1_input.txt") as f: INPUT_DATA: str = f.read()
# unfinsished and unoptimized approach, but this was so slow, that at some point i knew i could do all the optimizations i wanted and still be too way slow...

# always 3x3 shapes, never empty side row or column
SHAPE_SIZE: int = 3

sections: list[str] = list(map(str, INPUT_DATA.split("\n\n")))
shapes: dict[int, list[list[list[bool]]]] = {}
for section in sections[:-1]:
    idx_str, shape_str = section.split(":\n")
    idx = int(idx_str)
    shape: list[list[bool]] = []
    for line in shape_str.split("\n"):
        shape.append([c == '#' for c in line])
    shapes[idx] = []
    shapes[idx].append(shape)

    # rotations and flips that are unique (all combinations)
    for _ in range(3):
        shape = [list(row) for row in zip(*shape[::-1])]  # rotate 90 degrees
        if shape not in shapes[idx]:
            shapes[idx].append(shape)
    shape = [row[::-1] for row in shape]  # flip horizontally
    if shape not in shapes[idx]:
        shapes[idx].append(shape)
    for _ in range(3):
        shape = [list(row) for row in zip(*shape[::-1])]  # rotate 90 degrees
        if shape not in shapes[idx]:
            shapes[idx].append(shape)
idx_count: int = len(shapes)  

boxes: list[tuple[tuple[int, int], tuple[int, ...]]] = []
for line in sections[-1].split("\n"):
    size_str, idx_count_str = line.split(": ")
    width, height = [int(s) for s in size_str.split("x")]
    shape_indices: tuple[int, ...] = tuple(int(s) for s in idx_count_str.split(" "))
    boxes.append(((width, height), shape_indices))

def can_add_shape(shape: list[list[bool]], x: int, y: int, box: list[list[bool]]) -> bool:
    """
    Check if shape can be placed at (x, y) in box without overlapping existing filled cells.
    Does not check bounds! always stay within bounds minus shape size.
    """
    for cx in range(SHAPE_SIZE):
        for cy in range(SHAPE_SIZE):
            if shape[cy][cx] and box[y + cy][x + cx]:
                return False
    return True

def place_shape(shape: list[list[bool]], x: int, y: int, box: list[list[bool]]) -> None:
    """
    Places the shape at (x, y) in box.
    Does not check bounds! always stay within bounds minus shape size.
    Overrites existing cells - assumes can_add_shape was called first.
    """
    for cx in range(SHAPE_SIZE):
        for cy in range(SHAPE_SIZE):
            if shape[cy][cx]:
                box[y + cy][x + cx] = True

def initialize_boxes(width: int, height: int, indices: tuple[int, ...]) -> Iterator[tuple[tuple[int, ...], list[list[bool]]]]:
    for idx in range(idx_count):
        if indices[idx] > 0:
            for shape in shapes[idx]:
                box: list[list[bool]] = [[False for _ in range(width)] for _ in range(height)]
                place_shape(shape, 0, 0, box)
                yield (indices[:idx] + (indices[idx] - 1,) + indices[idx + 1:], box)

def can_solve(shapes_remaining: tuple[int, ...], x: int, y: int, box: list[list[bool]]) -> bool:
    if all(count == 0 for count in shapes_remaining):
        return True

    if str((shapes_remaining, box)) in cache:
        return False

    if x + SHAPE_SIZE > len(box[0]):
        x = 0
        y += 1
        if y + SHAPE_SIZE > len(box):
            cache.add(str((shapes_remaining, box)))
            return False

    # could count edges and try the least first, but because there will be unsolvable boxes, we need to try all options anyway
    for idx in range(idx_count):
        if shapes_remaining[idx] > 0:
            for shape in shapes[idx]:
                copy_box: list[list[bool]] = [row.copy() for row in box]
                if can_add_shape(shape, x, y, copy_box):
                    place_shape(shape, x, y, copy_box)
                    copy_remaining: tuple[int, ...] = shapes_remaining[:idx] + (shapes_remaining[idx] - 1,) + shapes_remaining[idx + 1:]
                    if can_solve(copy_remaining, x + 1, y, copy_box):
                        return True
                    
    return can_solve(shapes_remaining, x + 1, y, box)

solvable_boxes: int = 0
for box in boxes:
    cache: set[str] = set()
    for indicies, initial_state in initialize_boxes(box[0][0], box[0][1], box[1]):
        print(f"Trying box {box} with indicies {indicies}")
        if can_solve(indicies, 1, 0, initial_state):
            solvable_boxes += 1
            print('-', end='')
            break

print(f"\nSolvable boxes: {solvable_boxes}")

print('--- YOU ARE VERY PATIENT ---')
