import random
import math

def initialize():
    # return [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
    return [2, 1, 5, 0]

def get_random_neighbour(state):
    i = random.randint(0, len(state)-2)
    return state[:i] + [state[i+1]] + [state[i]] + state[i+2:]

def claculate_cost(state):
    inversions = 0
    for i in range(0, len(state)):
        for j in range(i+1, len(state)):
            if state[i] > state[j]:
                inversions += 1
    return inversions 


def simulated_annealing(initial_state):
    T = 1.0
    cooling_rate = 0.99             # the cooling rate (0 to 0.99) 
    T_limit = 0.00001
    iteration_start = 0
    iteration_limit = 1000
    
    current_state = initial_state
    current_cost = claculate_cost(current_state)
    
    while T > T_limit and iteration_start < iteration_limit:
        next_state = get_random_neighbour(current_state)   # getting a random neighbour
        next_cost = claculate_cost(next_state)
        
        del_E = next_cost - current_cost
        
        # if next state has lower cost, choose that one
        if del_E < 0:
            current_state = next_state
            current_cost = next_cost
        else:
            # if next state has higher cost, choose it with a random possibility
            if math.exp(-del_E/T) > random.uniform(0, 1):   # e ^ (-del_E/T)
                current_state = next_state
                current_cost = next_cost
       
        T *= cooling_rate         # update temperature
        iteration_start += 1      # update iteration number
        
        
    return current_state, current_cost


def main():
    initial_state = initialize()
    print(f"initial: {initial_state} | cost = {claculate_cost(initial_state)}")
    
    final_state, cost = simulated_annealing(initial_state)
    print(f"final: {final_state} | cost = {cost}")

main()
