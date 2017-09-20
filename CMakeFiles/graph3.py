import fileinput
import os


print(os.path.abspath(os.curdir))


def make_graph():
    graph = {}
    graph_direction_matrix = {}
    graph_distances = {}

    file = fileinput.input()

    first_line_list = file.readline().split()
    rows = int(first_line_list[0])
    cols = int(first_line_list[1])
    start_position_tarzan = tuple(map(int, file.readline().split()))
    #print(start_position_tarzan)

    #print(type(first_line_list))

    contents = []
    row = 1

    for line in file:
        # row = file.lineno()
        # print(row)
        contents = line.split()
        #print(contents)
        col = 1
        for direction in contents:
            graph_direction_matrix[row, col] = direction
            #print(graph_direction_matrix)
            col += 1
        row += 1


    for key in graph_direction_matrix.keys():
        if graph_direction_matrix[key] != 'X':
            if graph_direction_matrix[key] == 'S': ##down
                graph_distances[key] = [{(key[0]+3,key[1]) : 3}] + [{(key[0]+4,key[1]) : 4}]
            if graph_direction_matrix[key] == 'N': ##up
                graph_distances[key] = [{(key[0]-3,key[1]) : 3}] + [{(key[0]-4,key[1]) : 4}]
            if graph_direction_matrix[key] == 'E':
                graph_distances[key] = [{(key[0],key[1]+3) : 3}] + [{(key[0],key[1]+4) : 4}]
            if graph_direction_matrix[key] == 'W':
                graph_distances[key] = [{(key[0],key[1]-3) : 3}] + [{(key[0],key[1]-4) : 4}]
            if graph_direction_matrix[key] == 'NE':
                graph_distances[key] = [{(key[0]-3,key[1]+3) : 3}] + [{(key[0]-4,key[1]+4) : 4}]
            if graph_direction_matrix[key] == 'NW':
                graph_distances[key] = [{(key[0]-3,key[1]-3) : 3}] + [{(key[0]-4,key[1]-4) : 4}]
            if graph_direction_matrix[key] == 'SE':
                graph_distances[key] = [{(key[0]+3,key[1]+3) : 3}] + [{(key[0]+4,key[1]+4) : 4}]
            if graph_direction_matrix[key] == 'SW':
                graph_distances[key] = [{(key[0]+3,key[1]-3) : 3}] + [{(key[0]+4,key[1]+4) : 4}]
            if graph_direction_matrix[key] == 'J':
                graph_distances[key] = (key[0],key[1])

    print(graph_distances)
    print (graph_direction_matrix)

    for key in graph_direction_matrix.keys():
        if graph_direction_matrix[key] != 'X':
            if graph_direction_matrix[key] == 'S':  ##down
                graph[key] = [(key[0] + 3, key[1])] + [(key[0] + 4, key[1])]
            if graph_direction_matrix[key] == 'N':  ##up
                graph[key] = [(key[0] - 3, key[1])] + [(key[0] - 4, key[1])]
            if graph_direction_matrix[key] == 'E':
                graph[key] = [(key[0], key[1] + 3)] + [(key[0], key[1] + 4)]
            if graph_direction_matrix[key] == 'W':
                graph[key] = [(key[0], key[1] - 3)] + [(key[0], key[1] - 4)]
            if graph_direction_matrix[key] == 'NE':
                graph[key] = [(key[0] - 3, key[1] + 3)] + [(key[0] - 4, key[1] + 4)]
            if graph_direction_matrix[key] == 'NW':
                graph[key] = [(key[0] - 3, key[1] - 3)] + [(key[0] - 4, key[1] - 4)]
            if graph_direction_matrix[key] == 'SE':
                graph[key] = [(key[0] + 3, key[1] + 3)] + [(key[0] + 4, key[1] + 4)]
            if graph_direction_matrix[key] == 'SW':
                graph[key] = [(key[0] + 3, key[1] - 3)] + [(key[0] + 4, key[1] + 4)]
            if graph_direction_matrix[key] == 'J':
                graph[key] = (key[0], key[1])




    #return graph

    #print(graph)
    #print("\n")
    goal = ()
    #print(start_position_tarzan)

    for item in graph_direction_matrix.items():
        if 'J' in item:
            goal = item[0]


    start = start_position_tarzan
    #print(start)

    path = find_path(graph,start_position_tarzan,goal)
    print(path)

    direction = ""
    distances = []
    for node in path:
        direction += graph_direction_matrix[node]
        ##distances.append(graph_distances[node][0])
        list_of_dict = graph_distances[node]
        #for dic in list_of_dict:
            #print(dic)
            #if dic.has_key(node):
            #   direction += "-"+dic[node]
        #print distances
        direction += " "

    print direction

    #print(type(start_position_tarzan))

    values = graph_direction_matrix.values()
    keys = graph_direction_matrix.keys()

    #print((5,1) in keys)

    #print('J' in values)

    ##print(graph_direction_matrix)


    # print(graph[8,1])


    # print(graph[start_position_tarzan[0],start_position_tarzan[1]])
    # print(graph_direction_matrix[1,1])





def find_path(graph, start, goal, path = []):
    path = path + [start]
    if start == goal:
        return path
    if not graph.has_key(start):
        return None
    for neighbor in graph[start]:
        if neighbor not in path:
            newpath = find_path(graph, neighbor, goal, path)
            if newpath: return newpath
    return None


make_graph()
