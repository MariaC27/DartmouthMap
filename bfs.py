# Author: Maria Cristoforo
# Date: November 15, 2020
# Purpose: breadth first search algorithm

from collections import deque
from cs1lib import *

def bfs(start, goal):
    start.draw_vertex(1, 0, 0)
    goal.draw_vertex(1, 0, 0)

    # display names of the start and goal vertices
    enable_stroke()
    set_font_size(9)
    set_stroke_color(0, 0, 0)
    draw_text(start.name, int(start.x), int(start.y))
    draw_text(goal.name, int(goal.x), int(goal.y))


    frontier = deque()
    bp_dict = {}
    path = []

    frontier.append(start)
    bp_dict[start.name] = None

    if start is None or goal is None:
        return []

    while len(frontier) != 0:
        v = frontier.popleft()
        for i in range(len(v.adj)):
            u = v.adj[i]
            if u.name not in bp_dict:  # unvisited
                frontier.append(u)
                bp_dict[u.name] = v
        if goal in frontier:
            break

    if goal in frontier:  # if the goal has been reached
        curr = goal
        while curr is not None:
            path.append(curr)  # trace back and add to path
            curr = bp_dict[curr.name]

    return path

