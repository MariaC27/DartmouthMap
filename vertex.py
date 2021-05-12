# Author: Maria Cristoforo
# Date: November 10, 2020
# Purpose: the vertex class

from cs1lib import *

RADIUS = 9
EDGE_WIDTH = 4


class Vertex:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adj = []


    def __str__(self):
        name_list = []
        for i in range(len(self.adj)):
            name_list.append(self.adj[i].name)

        return self.name + "; " + "Location: " + self.x + "," + self.y + "; " + "Adjacent Vertices: " + ", ".join(name_list)


    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)
        disable_stroke()
        draw_circle(int(self.x), int(self.y), RADIUS)

    def draw_edge(self, v, r, g, b):
        enable_stroke()
        set_stroke_width(EDGE_WIDTH)
        set_stroke_color(r, g, b)
        draw_line(int(self.x), int(self.y), int(v.x), int(v.y))

    def draw_edges_adjacent(self, r, g, b):
        for i in range(len(self.adj)):
            self.draw_edge(self.adj[i], r, g, b)


    # function to determine whether the mouse is in the smallest square
    # surrounding a vertex
    def within_square(self, x, y):
        if x > (int(self.x) - RADIUS) and x < (int(self.x) + RADIUS):
            if y > (int(self.y) - RADIUS) and y < (int(self.y) + RADIUS):
                return True

        return False


