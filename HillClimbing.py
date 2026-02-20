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

def generate_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    for i in range(4):
        new_x = x + row[i]
        new_y = y + col[i]

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [r[:] for r in state]
            new_state[x][y], new_state[new_x][new_y] = \
                new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def hill_climbing(start):
    current = start
    print("Initial State:")
    print_state(current)

    while True:
        current_h = manhattan_distance(current)
        neighbors = generate_neighbors(current)

        next_state = current
        next_h = current_h

        for state in neighbors:
            h = manhattan_distance(state)
            if h < next_h:
                next_state = state
                next_h = h

        if next_h >= current_h:
            break

        current = next_state

    if current == goal_state:
        print("Goal State Reached!\n")
    else:
        print("Stopped at Local Optimum\n")

    print("Final State:")
    print_state(current)

start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

hill_climbing(start_state)