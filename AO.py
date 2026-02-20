goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

def print_state(state):
    for r in state:
        print(r)
    print()

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_successors(state):
    successors = []
    x, y = find_zero(state)

    for i in range(4):
        new_x = x + row[i]
        new_y = y + col[i]

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [r[:] for r in state]
            new_state[x][y], new_state[new_x][new_y] = \
                new_state[new_x][new_y], new_state[x][y]
            successors.append(new_state)

    return successors

def ao_star(start):
    current = start
    print("Initial State:")
    print_state(current)

    while current != goal_state:
        successors = generate_successors(current)
        costs = []

        for state in successors:
            h = manhattan_distance(state)
            costs.append((h, state))

        costs.sort(key=lambda x: x[0])
        current = costs[0][1]

    print("Goal State Reached!")
    print("\nFinal State:")
    print_state(current)

start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

ao_star(start_state)