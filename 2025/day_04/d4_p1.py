INPUT_DATA: str = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

good_rolls: int = 0
board: list[list[int]] = []

for x, line in enumerate(INPUT_DATA.split('\n')):
    board.append([False])
    for y, c in enumerate(line):
        board[x].append(c == '@')
    board[x].append(False)

board.insert(0, [False] * len(board[1]))
board.append([False] * len(board[1]))

for x in range(len(board)):
    print()
    for y in range(len(board[0])):
        if(board[x][y]):
            print('@', end='')
        else:
            print('_', end='')

for x in range(1, len(board) - 1):
    for y in range(1, len(board[0]) - 1):
        if(board[x][y]):
            n_count: int = (board[x-1][y-1] + board[x-1][y] + board[x-1][y+1] +
                            board[x][y-1] + board[x][y+1] +
                            board[x+1][y-1] + board[x+1][y] + board[x+1][y+1])
            if(n_count < 4):
                good_rolls += 1

print(f"\nGood rolls: {good_rolls}")

# personal solution: 1433