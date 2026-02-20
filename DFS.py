N = 3

class P8Board:
    def __init__(self, board, x, y, depth):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth

row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def is_goal(board):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal

def DFS(start, x, y):
    stack = []
    visited = set()
    stack.append(P8Board(start, x, y, 0))
    visited.add(tuple(map(tuple, start)))

    while stack:
        current = stack.pop()

        if is_goal(current.board):
            print("Solution found at depth:", current.depth)
            print("Final board state:")
            for r in current.board:
                print(r)
            return

        # Try 4 moves
        for i in range(4):
            new_x = current.x + row[i]
            new_y = current.y + col[i]

            if is_valid(new_x, new_y):
                new_board = [r[:] for r in current.board]

                # SWAP (fixed broken line)
                new_board[current.x][current.y], new_board[new_x][new_y] = \
                new_board[new_x][new_y], new_board[current.x][current.y]

                board_tuple = tuple(map(tuple, new_board))
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    stack.append(P8Board(new_board, new_x, new_y, current.depth + 1))

    print("No solution found.")

# Initial test
start_board = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]
x, y = 1, 1
DFS(start_board, x, y)
 