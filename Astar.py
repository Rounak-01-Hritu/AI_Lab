import heapq

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

def print_state(state):
    for row in state:
        print(row)
    print()

def manhattan_distance(current, goal):
    pos = {}
    for i in range(3):
        for j in range(3):
            pos[goal[i][j]] = (i, j)

    dist = 0
    for i in range(3):
        for j in range(3):
            if current[i][j] != 0:
                x, y = pos[current[i][j]]
                dist += abs(i - x) + abs(j - y)
    return dist

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def a_star(start):
    pq = []
    heapq.heappush(pq, (0, start, 0))
    visited = set()

    while pq:
        f, current, g = heapq.heappop(pq)

        if current == goal_state:
            print("Goal State Reached!\n")
            print("Final State:")
            print_state(current)
            return

        visited.add(str(current))
        x, y = find_zero(current)

        for i in range(4):
            new_x = x + row[i]
            new_y = y + col[i]

            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [r[:] for r in current]
                new_state[x][y], new_state[new_x][new_y] = \
                    new_state[new_x][new_y], new_state[x][y]

                if str(new_state) not in visited:
                    h = manhattan_distance(new_state, goal_state)
                    heapq.heappush(pq, (g + h, new_state, g + 1))

start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

print("Initial State:")
print_state(start_state)

a_star(start_state)