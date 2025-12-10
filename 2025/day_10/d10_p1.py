INPUT_DATA: str = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

lights: list[list[bool]] = []
buttons: list[list[list[int]]] = []

for line in INPUT_DATA.split('\n'):
    parts = line.split(' ')
    lights.append([])
    for c in parts[0][1:-1]:
        lights[-1].append(c == '#')
    buttons.append([])
    for nums in parts[1:-1]:
        buttons[-1].append(list(map(int, nums[1:-1].split(','))))

min_results: list[int] = []

for idx in range(len(lights)):
    seen_states: set[tuple[bool, ...]] = set()
    stack: list[tuple[list[bool], int]] = [([False] * len(lights[idx]), 0)]
    is_solved = False
    while not is_solved:
        stack.sort(key=lambda s: s[1], reverse=True)
        state = stack.pop()
        depth = state[1] + 1
        for button in buttons[idx]:
            light = state[0].copy()
            for sw_idx in button:
                light[sw_idx] = not light[sw_idx]
            if light == lights[idx]:
                min_results.append(depth)
                is_solved = True
                break
            light_tuple = tuple(light)
            if light_tuple not in seen_states:
                seen_states.add(light_tuple)
                stack.append((light, depth))    

print(f"\nTotal: {sum(min_results)}")

# personal solution: 507