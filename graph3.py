import fileinput
import os
import sys

#print(os.path.abspath(os.curdir))


def make_graph():
    graph = {}
    graph_direction = {}
    graph_distances = {}

    file = fileinput.input(sys.argv[1])

    first_line_list = file.readline().split()
    rows = int(first_line_list[0])
    cols = int(first_line_list[1])
    start_position_tarzan = tuple(map(int, file.readline().split()))


    contents = []
    row = 1

    for line in file:
        contents = line.split()
        col = 1
        for direction in contents:
            graph_direction[row, col] = direction
            col += 1
        row += 1


    for key in graph_direction.keys():
        if graph_direction[key] != 'X':
            if graph_direction[key] == 'S': ##down
                graph_distances[key] = [{(key[0]+3,key[1]) : 3}] + [{(key[0]+4,key[1]) : 4}]
            if graph_direction[key] == 'N': ##up
                graph_distances[key] = [{(key[0]-3,key[1]) : 3}] + [{(key[0]-4,key[1]) : 4}]
            if graph_direction[key] == 'E':
                graph_distances[key] = [{(key[0],key[1]+3) : 3}] + [{(key[0],key[1]+4) : 4}]
            if graph_direction[key] == 'W':
                graph_distances[key] = [{(key[0],key[1]-3) : 3}] + [{(key[0],key[1]-4) : 4}]
            if graph_direction[key] == 'NE':
                graph_distances[key] = [{(key[0]-3,key[1]+3) : 3}] + [{(key[0]-4,key[1]+4) : 4}]
            if graph_direction[key] == 'NW':
                graph_distances[key] = [{(key[0]-3,key[1]-3) : 3}] + [{(key[0]-4,key[1]-4) : 4}]
            if graph_direction[key] == 'SE':
                graph_distances[key] = [{(key[0]+3,key[1]+3) : 3}] + [{(key[0]+4,key[1]+4) : 4}]
            if graph_direction[key] == 'SW':
                graph_distances[key] = [{(key[0]+3,key[1]-3) : 3}] + [{(key[0]+4,key[1]+4) : 4}]
            if graph_direction[key] == 'J':
                graph_distances[key] = [{(key[0],key[1]): 0}]

    #print(graph_distances)
    #print (graph_direction)

    for key in graph_direction.keys():
        if graph_direction[key] != 'X':
            if graph_direction[key] == 'S':  ##down
                graph[key] = [(key[0] + 3, key[1])] + [(key[0] + 4, key[1])]
            if graph_direction[key] == 'N':  ##up
                graph[key] = [(key[0] - 3, key[1])] + [(key[0] - 4, key[1])]
            if graph_direction[key] == 'E':
                graph[key] = [(key[0], key[1] + 3)] + [(key[0], key[1] + 4)]
            if graph_direction[key] == 'W':
                graph[key] = [(key[0], key[1] - 3)] + [(key[0], key[1] - 4)]
            if graph_direction[key] == 'NE':
                graph[key] = [(key[0] - 3, key[1] + 3)] + [(key[0] - 4, key[1] + 4)]
            if graph_direction[key] == 'NW':
                graph[key] = [(key[0] - 3, key[1] - 3)] + [(key[0] - 4, key[1] - 4)]
            if graph_direction[key] == 'SE':
                graph[key] = [(key[0] + 3, key[1] + 3)] + [(key[0] + 4, key[1] + 4)]
            if graph_direction[key] == 'SW':
                graph[key] = [(key[0] + 3, key[1] - 3)] + [(key[0] + 4, key[1] + 4)]
            if graph_direction[key] == 'J':
                graph[key] = (key[0], key[1])




    #return graph

    #print(graph)
    #print("\n")
    goal = ()
    #print(start_position_tarzan)

    for item in graph_direction.items():
        if 'J' in item:
            goal = item[0]


    start = start_position_tarzan
    #print(start)

    path = find_path(graph,start_position_tarzan,goal)
    #print(path)

    directions = ""
    output = ''
    distances = []
    list_of_dict = {}
    for node in path:
        directions += graph_direction[node]
        ##distances.append(graph_distances[node][0])
        list_of_dict = graph_distances[node]
        for dic in list_of_dict:
            if dic is type(dict):
                if dic.has_key(node):
                    directions += "-"+dic[node]
            for key in dic:
                if key in path:
                    distances.append(dic[key])

    outputfile = open('output.txt', 'w')

    for i in range(len(distances)):
        output += directions[i]+'-'+str(distances[i])+' '
        outputfile.write(output)


    outputfile.close()


    values = graph_direction.values()
    keys = graph_direction.keys()



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
