# Author: Maria Cristoforo
# Date: November 12, 2020
# Purpose: draw the map and plot the shortest path between vertices selected by the user

from cs1lib import *
from DartmouthMap.load_graph import load_graph
from DartmouthMap.bfs import bfs

draw_once = True

vertex_dict = load_graph("dartmouth_graph.txt")
img = load_image("dartmouth_map.png")
start_vertex = None  # initialized to None
goal_vertex = None

# variables for keeping track of mouse
mouse_pressed = False
mouse_released = True
mouse_x = 0
mouse_y = 0
press_x = 0
press_y = 0
release_x = 0
release_y = 0


# functions for keeping track of mouse
def my_mouse_move(mx, my):
    global mouse_x, mouse_y
    mouse_x = mx
    mouse_y = my
    # keeps track of the mouse position at all times


def my_mouse_press(mx, my):
    global mouse_pressed, mouse_released
    mouse_pressed = True
    mouse_released = False


def my_mouse_release(mx, my):
    global mouse_pressed, mouse_released
    mouse_pressed = False
    mouse_released = True


def draw_graph():
    clear()  # clear so that only new names show up
    draw_image(img, 0, 0)
    for k in vertex_dict:
        l_vertex = vertex_dict[k]  # need to use actual vertex instead of string name
        l_vertex.draw_vertex(0, 0, 1)
        l_vertex.draw_edges_adjacent(0, 0, 1)


# if the mouse is clicked and released on a vertex, that is the starting vertex
def find_start():
    global press_x, press_y, release_x, release_y, start_vertex

    if mouse_pressed:
        press_x = mouse_x
        press_y = mouse_y
    if mouse_released:
        release_x = mouse_x
        release_y = mouse_y

    if press_x == release_x and press_y == release_y:  # mouse was pressed and released in same spot
        for k in vertex_dict:
            my_vertex = vertex_dict[k]

            # could have used either press or release - doesn't matter since they refer to the same point
            if my_vertex.within_square(press_x, press_y):
                start_vertex = my_vertex


# whichever vertex the mouse is hovering over is the goal vertex
def find_goal():
    global goal_vertex
    for k in vertex_dict:
        my_vertex = vertex_dict[k]
        if my_vertex.within_square(mouse_x, mouse_y) and start_vertex is not None:
            goal_vertex = my_vertex


def draw():
    global draw_once, start_vertex, goal_vertex
    if draw_once:   # to make sure the image is only loaded once
        set_clear_color(1, 1, 1)
        clear()
        draw_image(img, 0, 0)
        draw_once = False

    draw_graph()
    find_start()  # constantly check for new start and goal vertices
    find_goal()

    # draw start and goal vertices in red inside bfs function to avoid errors with None

    # draw red path
    path = []
    if start_vertex is not None and goal_vertex is not None:
        path = bfs(start_vertex, goal_vertex)

    for i in range(len(path)-1):
        path[i].draw_edge(path[i+1], 1, 0, 0)


start_graphics(draw, width=1012, height=811,mouse_press=my_mouse_press, mouse_release=my_mouse_release,
               mouse_move=my_mouse_move)

