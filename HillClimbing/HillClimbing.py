def initialize():
    return [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
    # return [2, 1, 5, 0]

# getting neighbours
def get_all_neighbours(i, state):
    if i == len(state) - 1:     # can't shift to right if only an element is left
        return state
    return state[:i] + [state[i+1], state[i]] + state[i+2:]
    # until index + after index (1st one) + the index + rest (after 2nd index)

# calculating inversions
def claculate_cost(state):
    inversions = 0
    
    for i in range(0, len(state)):
        for j in range(i+1, len(state)):
            if state[i] > state[j]:
                inversions += 1
    
    return inversions 


def state_generation(current_state):
    while True:
        current_state_cost = claculate_cost(current_state)
        print(f"{current_state} | cost: {current_state_cost}")
        
        min_next_cost = 99999 # infinity
        min_next_state = None
        
        # getting all neighbours 
        all_neighbours = []
        for i in range(len(current_state)):
            neighbour = get_all_neighbours(i, current_state)
            all_neighbours.append(neighbour)
            
        # getting all neighbours' cost
        neighbour_costs = []
        for i in range(len(all_neighbours)):
            cost = claculate_cost(all_neighbours[i])  # 'all_neighbours' contains lists of all neighbours
            neighbour_costs.append(cost)
            
        
        # neighbour selection.......
        min_next_cost = min(neighbour_costs)   
        
        # index of the neighbour who has the lowest cost 
        index = neighbour_costs.index(min_next_cost)  
        min_next_state = all_neighbours[index]

        # checking if min of neighbour is lower than current state  
        if min_next_cost < current_state_cost:
            current_state = min_next_state
        else:
            print(f"final state: {current_state} | cost: {current_state_cost}")
            break
        
        
def main():
    state = initialize()
    state_generation(state)

# stating the execution
main()