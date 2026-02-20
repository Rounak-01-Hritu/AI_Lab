from collections import deque

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

def BFS(start, x, y):
    queue = deque()
    visited = set()

    queue.append(P8Board(start, x, y, 0))
    visited.add(tuple(map(tuple, start)))

    while queue:
        current = queue.popleft()

        if is_goal(current.board):
            print("Solution found at depth:", current.depth)
            print("Final board state:")
            for r in current.board:
                print(r)
            return

        for i in range(4):
            new_x = current.x + row[i]
            new_y = current.y + col[i]

            if is_valid(new_x, new_y):
                new_board = [r[:] for r in current.board]

                new_board[current.x][current.y], new_board[new_x][new_y] = \
                    new_board[new_x][new_y], new_board[current.x][current.y]

                board_tuple = tuple(map(tuple, new_board))
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    queue.append(P8Board(new_board, new_x, new_y, current.depth + 1))

    print("No solution found")


# Test
start_board = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]
x, y = 1, 1

BFS(start_board, x, y)
