
def dfs(graph, current_vertex, edges, prev_vertex=None, visited=None):
    edges_vertices = (list(graph.values()))

    lst_values = []
    for lst in edges_vertices:
        lst_values.append(len(lst))
    
    biggest_lst = max(lst_values)
    biggest_edge = None

    for vertex in graph.keys():
        if len(graph[vertex]) == biggest_lst:
            biggest_edge = vertex
            break

    edges[current_vertex] = True
    if visited == None:
        visited = []
    visited.append(current_vertex)
    
    if true_counter(edges) == True:
        return visited 
    else:
        for neighbour in graph[current_vertex]:
            if neighbour == prev_vertex:
                continue
            if not neighbour in visited or neighbour == biggest_edge:
                new_path = dfs(graph, neighbour, edges, current_vertex, visited)
            


                if new_path:
                    return new_path 
    
    
    return None


def true_counter(edges_dict):
    count = 0
    for edge, status in edges_dict.items():
        if status == True:
            count += 1
        else:
            continue 
    
    if count == len(edges_dict.keys()):
        return True
    else:
        return False
        