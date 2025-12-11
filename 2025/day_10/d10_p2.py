# i needed to use linear programming lib for this one :(, the lib looks great even if its the first time i use it.
# cant really call this a win though...

from typing import Any
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus, PULP_CBC_CMD  # type: ignore

# INPUT_DATA: str = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
with open("2025/day_10/d10_input.txt") as f: INPUT_DATA: str = f.read()

joltages: list[list[int]] = []
buttons: list[list[set[int]]] = []
for line in INPUT_DATA.strip().split('\n'):
    parts: list[str] = line.split(' ')
    joltages.append(list(map(int, parts[-1][1:-1].split(','))))
    buttons.append([set(map(int, nums[1:-1].split(','))) for nums in parts[1:-1]])

min_results: list[int] = []
for target, button_configs in zip(joltages, buttons):
    prob: Any = LpProblem("ButtonPresses", LpMinimize)
    button_vars: list[Any] = [LpVariable(f"button_{i}", lowBound=0, cat='Integer') for i in range(len(button_configs))]
    prob += lpSum(button_vars)
    for pos in range(len(target)):
        prob += lpSum(button_vars[i] for i in range(len(button_configs)) if pos in button_configs[i]) == target[pos]
    
    prob.solve(PULP_CBC_CMD(msg=False))
    
    if LpStatus[prob.status] == 'Optimal':
        min_results.append(int(sum(v.varValue for v in button_vars)))
    else:
        print("No optimal solution found.")
        break

print(f"\nTotal: {sum(min_results)}")

# personal solution: 18981