from dfs import dfs 

from inputs import g1

paths = []

def eulerian(graph_dict):
    graph_dict = g1.graph_dict
    first_vertex = list(graph_dict.keys())[0]
    last_vertex = list(graph_dict.keys())[-1]
    updated_graph_dict = {}

    edges_object = list(graph_dict.values())                # Edge Case 1
    edges = []
    for vertex in edges_object:
        vertex_edges = list(vertex.edges.keys())
        edges += vertex_edges
    
    if first_vertex not in edges or last_vertex not in edges:
        print("There is no Eulerian Path nor Cycle")
        return None
    
    vertices = list(graph_dict.keys())

    for vertex in vertices:
        if not vertex in edges:
            graph_dict.pop(vertex)
    
    odd_degree_counter = 0                                 # Edge Case 2
    for vertex, edge in graph_dict.items():
        edges = list(edge.edges.keys())
        updated_graph_dict[vertex] = edges
        vertices_sum = 0 
        for edge in edges:
            vertices_sum += edge 
        
        if vertices_sum % 2 == 1:
            odd_degree_counter += 1 
        else:
            continue

    if odd_degree_counter > 2:
        print("There is no Eulerian Path")
        return 
    
    sets = [[vertex, edge] for vertex, edge in updated_graph_dict.items()]          #Eulerian Path
    
    for vertex in sets:
        edges_dict = {}
        current_vertex_edges = vertex[-1][:]
        for lst in sets:
            for number in lst[-1]:
                if not number in edges_dict:
                    edges_dict[number] = False
        while len(vertex[-1]) != 0:
            output = dfs(updated_graph_dict, vertex[0], edges_dict)
            
            paths.append(output)
            vertex[-1].pop(0)
            for key in edges_dict.keys():
                edges_dict[key] = False
        
        vertex[-1] = current_vertex_edges
        updated_graph_dict[vertex[0]] = current_vertex_edges

    eulerian_paths = eulerian_path_checker(updated_graph_dict, paths)[:2]

    if eulerian_paths:
        for path in eulerian_paths:
            print("The graph has an Eulerian Path: {}".format(path))

        eulerian_cycles = eulerian_cycle(updated_graph_dict, eulerian_paths)

        if eulerian_cycles:                                                                #Eulerian Cycle
            for cycle in eulerian_cycle:
                print("The graph has an Eulerian Cycle: {}".format(cycle))
        else:
            print("The graph does not have any Eulerian Cycles")
    else:
        print("The graph does not have any Eulerian Paths")
    

def eulerian_path_checker(graph, paths):
    eulerian_paths = []
    for path in paths:
        checker = None
        if path == None:
            continue 
        else:
            for vertex in range(len(path)):
                try:
                    current_vertex = path[vertex]
                    next_vertex = path[vertex + 1]
                    current_edges = graph[current_vertex] 
                    if next_vertex in current_edges:
                        continue 
                    else:
                        checker = False
                        break 
                except IndexError:
                    break
            if checker != False:
                eulerian_paths.append(path)
            else:
                pass

    if len(eulerian_paths) == 0:
        return None
    else:
        return eulerian_paths


def eulerian_cycle(graph, el_paths):
    cycles = []
    for path in el_paths:
        last_vertex = list(graph.keys())[-1]
        first_vertex = path[0]
        if first_vertex in graph[last_vertex]:
            path += [first_vertex]
            cycles.append(path)
        else:
            continue
    
    if len(cycles) == 0:
        return None

    



print(eulerian(g1))