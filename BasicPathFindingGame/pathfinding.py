from collections import deque



def find_path(start_node, end_node, game_map):
    ''' Attempts to find a path from start_coords to end_coords on
        the given game_map, using a basic implementation of the
        A* algorithm. Returns a deque object for the path.
        
        set entries are 5-tuples with the format of:
        (child node, parent node, G cost, H cost, F cost) '''
    
    def find_lowest_cost_node(search_set):
        ''' Finds the node with the lowest F cost in the given set '''
        
        low_cost_node = None
        for node in search_set:
            if low_cost_node == None or node[4] < low_cost_node[4]:
                low_cost_node = node
        
        return low_cost_node
    
    
    open_set = set()
    close_set = set()
    
    open_set.add((start_node, start_node, 0, 0, 0))
    current_node = find_lowest_cost_node(open_set)
    
    while(len(open_set) != 0 and current_node[0] != end_node):
        current_node = find_lowest_cost_node(open_set)
        close_set.add(current_node)
        open_set.remove(current_node)
        
        for node in game_map.get_adjacent_nodes(current_node[0].get_coordinates()):
            for close_check_node in close_set:
                if close_check_node[0] == node:
                    break
                
            else:
                if current_node[0].get_x() != node.get_x() and current_node[0].get_y() != node.get_y():
                    g_cost = current_node[2]+3
                else:
                    g_cost = current_node[2]+2
                h_cost = (abs(node.get_x() - end_node.get_x()) + abs(node.get_y() - end_node.get_y()))
                f_cost = g_cost + h_cost
                
                for check_node in set(open_set):
                    if check_node[0] == node:
                        if g_cost < check_node[2]:
                            open_set.remove(check_node)
                            open_set.add((node, current_node, g_cost, h_cost, g_cost+h_cost))
                        break
                    
                else:
                    open_set.add((node, current_node, g_cost, h_cost, g_cost+h_cost))
                
    if current_node[0] == end_node:
        final_path = deque()
            
        while (current_node[0] != start_node):
            final_path.append(current_node[0])
            current_node = current_node[1]
            
        return final_path
        
    else:
        return deque()
            