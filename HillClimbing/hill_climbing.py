def initialize():
    return [2, 1, 5, 0]
    # return [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]


def calculate_cost(state):
    cost = 0
    for i in range(0, len(state)):
        for j in range(i+1, len(state)):
            if state[i] > state[j]:
                cost += 1
    return cost

def get_neighbour(i, j, state):
    return state[:i] + [state[j]] + state[i+1:j] + [state[i]] + state[j+1:]

def state_generation(current_state):
    while True:
        current_state_cost = calculate_cost(current_state)
        # print(f"{current_state} | cost = {current_state_cost}")
        
        neighbors = []  
        for i in range(len(current_state)):
            for j in range(i+1, len(current_state)):
                neighbor = get_neighbour(i, j, current_state)
                neighbors.append(neighbor)
                
        neighbor_costs = []
        for i in neighbors:
            neighbor_cost = calculate_cost(i)
            neighbor_costs.append(neighbor_cost)
        
        # print(neighbors)
        # print(neighbor_costs)
        
        min_neighbor_cost = min(neighbor_costs)
        min_neighbor_idx = neighbor_costs.index(min_neighbor_cost)
        min_next_state = neighbors[min_neighbor_idx]
        
        if min_neighbor_cost < current_state_cost:
            current_state = min_next_state
        else:
            print(f"final state: {current_state} | cost = {current_state_cost}")
            break


def main():
    state = initialize()
    print(f"initial state: {state} | cost = {calculate_cost(state)}")
    state_generation(state)

main()
