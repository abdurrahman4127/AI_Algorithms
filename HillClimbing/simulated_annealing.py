import random
import math

def initialize():
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
    alpha = 0.99
    stopping_T = 0.00001
    stopping_iter = 100000
    current_state = initial_state
    current_cost = claculate_cost(current_state)
    i = 0
    while T > stopping_T and i < stopping_iter:
        next_state = get_random_neighbour(current_state)
        next_cost = claculate_cost(next_state)
        
        del_E = next_cost - current_cost
        
        if del_E < 0:
            current_state = next_state
            current_cost = next_cost
        else:
            if math.exp(-del_E/T) > random.uniform(0, 1):
                current_state = next_state
                current_cost = next_cost
       
        T *= alpha
        i += 1
        
        
    return current_state, current_cost


def main():
    initial_state = initialize()
    final_state, cost = simulated_annealing(initial_state)
    print(f"initial: {initial_state} | cost = {claculate_cost(initial_state)}")
    print(f"final: {final_state} | cost = {cost}")

main()
