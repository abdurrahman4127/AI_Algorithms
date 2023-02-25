from queue import PriorityQueue

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
        self.nodename = nodename
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other_node):
        return self.f < other_node.f

    
NOb = Node('S', None, 0, H['S'])
pq = PriorityQueue()
pq.put(NOb)

while not pq.empty():
    NOb = pq.get()
    current_nodename = NOb.nodename

    if current_nodename == 'D':
        total_cost = NOb.f
        goal_path = []

        goal_path.append(current_nodename)
        parent = NOb.parent

        while parent:
            goal_path.append(parent.nodename)
            parent = parent.parent

        goal_path.reverse()

        print(goal_path)
        print(total_cost)

        break

    else:
        for i in range(len(adjacency_list[current_nodename])):
            next_node = adjacency_list[current_nodename][i]
            next_nodename = next_node[0]
            cost = next_node[1]

            g = cost + NOb.g
            h = H[next_nodename]

            next_NOb = Node(next_nodename, NOb, g, h)  
            pq.put(next_NOb)