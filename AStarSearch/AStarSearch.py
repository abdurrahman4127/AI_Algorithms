from queue import PriorityQueue

# dictionary for nodes and their adjacents
adjacency_list = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('D', 12)],
    'B': [('C', 2)],
    'C': [('D', 3)],
    'D': [('C', 4)]
}

# dictionary for heursitics
H = {'S': 7, 'A': 6, 'B': 2, 'C': 1, 'D': 0}


class Node:
    def __init__(self, nodename, parent, g, h):
        self.node_name = nodename
        self.parent = parent
        self.g = g             # (actual) cost from source to current node
        self.h = h             # heuristic cost of a node from goal node
        self.f = g + h         # heuristic cost + actual cost (from src)

    # orderin the priority queue based on the value of 'f'
    def __lt__(self, other_node):
        return self.f < other_node.f


def a_star_search(src, goal):
    NOb = Node(src, None, 0, H[src])  # params: nodename, parent, g, h
    
    pq = PriorityQueue()
    pq.put(NOb)
 
    # while pq:  # while pq exists
    while not pq.empty():  
        NOb = pq.get()  # getting the node with minimum 'f'      
        current_nodename = NOb.node_name

        if current_nodename == goal:   # or if H[current_nodename] = 0
            total_cost = NOb.f
            
            goal_path = []
            goal_path.append(current_nodename)  # adding the starting node
            
            parent_node = NOb.parent
            while parent_node:          # while parent node exists
                goal_path.append(parent_node.node_name)
                parent_node = parent_node.parent  # updating the parent to its parent
            
            goal_path.reverse()

            break

        else:
            # traversing current node's adjacent nodes
            for i in range(len(adjacency_list[current_nodename])):  
                next_node = adjacency_list[current_nodename][i]   # consists (nodename, cost) 
                next_nodename = next_node[0]
                cost = next_node[1]

                # g = cost of current node + (cost of reaching that node from source, NOb.g)
                g = cost + NOb.g     

                # params: Node(nodename, parent, g, h)
                next_NOb = Node(next_nodename, NOb, g, H[next_nodename]) 
                pq.put(next_NOb)

            # NOb = None

    return goal_path, total_cost


# starting the exeucution
def main():
    goal_path, total_cost = a_star_search(src='S', goal='D')

    print(f"total cost: {total_cost}")
    print(" --> ".join(goal_path))

main()