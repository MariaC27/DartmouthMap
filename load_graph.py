# Author: Maria Cristoforo
# Date: November 11, 2020
# Purpose: process a file and return a dictionary of vertices

from DartmouthMap.vertex import Vertex


def load_graph(name):
    fp = open(name, "r")
    v_dict = {}

    # first pass over the file
    for line in fp:
        line = line.strip()
        w_list = line.split(";")  # first split up the line - name; adjacents; coordinates
        w_list[0] = w_list[0].strip() # the name of the location
        w_list[2] = w_list[2].strip() # the coordinates of the location
        xy_list = w_list[2].split(",")  # split up the coordinates into x and y and store in list
        v = Vertex(w_list[0], xy_list[0], xy_list[1])  # give name, x, and y to make Vertex
        v_dict[w_list[0]] = v  # store the vertex in the dictionary

    fp.close()


    # second pass over the file
    fp = open(name, "r")
    for line in fp:
        line = line.strip()
        w_list = line.split(";")
        w_list[0] = w_list[0].strip()
        list_adj = w_list[1]
        adj_list = list_adj.split(",")
        v = v_dict[w_list[0]]

        # adds the vertex objects in the adjacency list to the list instance variable "adj" of
        # the corresponding vertex object in the dictionary
        for n in adj_list:
            n = n.strip()
            adj_v = v_dict[n]
            v.adj.append(adj_v)
    fp.close()

    return v_dict
